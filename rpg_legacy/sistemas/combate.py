# rpg_legacy/sistemas/combate.py (fully documented)
from typing import List, TYPE_CHECKING, Dict, Any
import random

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

from ..entidades.efeito import Efeito
from ..dados.efeitos import TODOS_OS_EFEITOS

def aplicar_efeitos_habilidade(ator: 'Personagem', alvos: List['Personagem'], habilidade: Dict) -> list[str]:
    """
    Processa e aplica todos os efeitos contidos em uma habilidade a uma lista de alvos.
    Esta função é o coração da execução de habilidades, lidando com dano, cura,
    aplicação de buffs, debuffs e outros efeitos customizados.

    Args:
        ator ('Personagem'): O personagem que está usando a habilidade.
        alvos (List['Personagem']): A lista de personagens que serão afetados pela habilidade.
        habilidade (Dict): O dicionário de dados da habilidade que está sendo usada.

    Returns:
        list[str]: Um log de eventos descrevendo o que aconteceu, para ser exibido na UI.
    """
    log_eventos = [f"{ator.nome} usa {habilidade['nome']}!"]

    for efeito_data in habilidade.get("efeitos", []):
        tipo_efeito = efeito_data.get("tipo")

        for alvo in alvos:
            if not alvo.esta_vivo(): continue

            # Verifica a chance de aplicação do efeito, se houver.
            chance = efeito_data.get("chance", 1.0)
            if random.random() > chance:
                log_eventos.append(f"O efeito de {habilidade['nome']} falhou em {alvo.nome}!")
                continue

            # --- Lógica de Efeitos de Dano ---
            if tipo_efeito == "dano_fisico" or tipo_efeito == "dano_magico":
                escala_com = efeito_data.get("escala_com", "forca" if tipo_efeito == "dano_fisico" else "inteligencia")
                escala = getattr(ator, escala_com)
                dano_base = escala * efeito_data.get("multiplicador_dano", 1.0)
                penetracao = efeito_data.get("penetracao_armadura", 0.0)

                defesa_alvo = alvo.defesa_fisica if tipo_efeito == "dano_fisico" else alvo.defesa_magica
                defesa_final = defesa_alvo * (1 - penetracao)

                dano_final = max(0, int(dano_base - defesa_final))
                alvo.tomar_dano(dano_final, tipo_efeito)
                log_eventos.append(f"{alvo.nome} tomou {dano_final} de dano.")

            # --- Lógica de Efeitos de Cura ---
            elif tipo_efeito == "cura":
                escala = getattr(ator, efeito_data.get("escala_com", "sabedoria"))
                cura = int(escala * efeito_data.get("multiplicador_cura", 1.0))
                alvo.curar(cura)
                log_eventos.append(f"{alvo.nome} recuperou {cura} de HP.")

            # --- Lógica de Aplicação de Efeitos de Status (Buffs/Debuffs) ---
            elif tipo_efeito == "aplicar_efeito" or tipo_efeito == "aplicar_efeito_self":
                target = ator if tipo_efeito == "aplicar_efeito_self" else alvo
                id_efeito = efeito_data.get("id_efeito")
                dados_base_efeito = TODOS_OS_EFEITOS.get(id_efeito)

                if not dados_base_efeito:
                    log_eventos.append(f"[ERRO DE SISTEMA] Efeito desconhecido: {id_efeito}")
                    continue

                # Evita que o mesmo efeito seja aplicado múltiplas vezes.
                if any(e.id_efeito == id_efeito for e in target.efeitos_ativos):
                    log_eventos.append(f"{target.nome} já está sob o efeito de {dados_base_efeito['nome']}.")
                    continue

                # Cria uma nova instância do Efeito para este alvo.
                novo_efeito = Efeito(
                    id_efeito=id_efeito,
                    nome=dados_base_efeito["nome"],
                    descricao=dados_base_efeito["descricao"],
                    tipo=dados_base_efeito["tipo"],
                    duracao_turnos=efeito_data.get("duracao", 3),
                    modificadores=dados_base_efeito.get("modificadores"),
                    efeito_por_turno=dados_base_efeito.get("efeito_por_turno"),
                    aplicado_por=ator
                )

                target.efeitos_ativos.append(novo_efeito)
                target.recalcular_stats_completos() # Aplica os modificadores do efeito imediatamente.
                log_eventos.append(f"{target.nome} está sob o efeito de {novo_efeito.nome}!")

    return log_eventos

def processar_efeitos_de_turno(personagem: 'Personagem') -> list[str]:
    """
    Processa todos os efeitos de status de um personagem (geralmente no início de seu turno).
    Esta função é responsável por:
    1. Aplicar efeitos contínuos como dano por turno (DoT) ou cura por turno (HoT).
    2. Decrementar a duração de todos os efeitos ativos.
    3. Remover efeitos que expiraram e recalcular os stats do personagem.

    Args:
        personagem ('Personagem'): O personagem cujos efeitos serão processados.

    Returns:
        list[str]: Um log de eventos descrevendo os efeitos aplicados ou removidos.
    """
    log_eventos = []
    efeitos_a_remover = []

    for efeito in personagem.efeitos_ativos:
        # O método tick() decrementa a duração e retorna o efeito por turno, se houver.
        efeito_por_turno = efeito.tick()

        if efeito_por_turno:
            tipo = efeito_por_turno.get("tipo")
            if tipo == "dano":
                dano = efeito_por_turno.get("quantidade", 0)
                tipo_dano = efeito_por_turno.get("dano_tipo", "neutro")
                personagem.tomar_dano(dano, tipo_dano)
                log_eventos.append(f"{personagem.nome} sofre {dano} de dano de {efeito.nome}!")
            elif tipo == "cura":
                cura = efeito_por_turno.get("quantidade", 0)
                personagem.curar(cura)
                log_eventos.append(f"{personagem.nome} recupera {cura} de vida de {efeito.nome}!")

        if efeito.expirou():
            log_eventos.append(f"O efeito '{efeito.nome}' acabou para {personagem.nome}.")
            efeitos_a_remover.append(efeito)

    if efeitos_a_remover:
        personagem.efeitos_ativos = [e for e in personagem.efeitos_ativos if e not in efeitos_a_remover]
        personagem.recalcular_stats_completos() # Recalcula stats após remover buffs/debuffs.

    return log_eventos


def executar_acao(ator: 'Personagem', acao: Dict, todos_aliados: List['Personagem'], todos_inimigos: List['Personagem']) -> list[str]:
    """
    Função central que processa uma única ação de combate, seja de um jogador ou de um monstro.
    Ela interpreta o dicionário de ação e chama as funções apropriadas para aplicar os resultados.

    Args:
        ator ('Personagem'): O personagem que está realizando a ação.
        acao (Dict): Um dicionário que descreve a ação (ex: {"tipo": "ataque_basico", ...}).
        todos_aliados (List['Personagem']): Lista de todos os aliados do ator.
        todos_inimigos (List['Personagem']): Lista de todos os inimigos do ator.

    Returns:
        list[str]: Um log de eventos com o resultado da ação.
    """
    tipo_acao = acao.get("tipo")
    alvo_entidade = acao.get("alvo")
    log_eventos = []

    if tipo_acao == "passar_turno":
        log_eventos.append(f"{ator.nome} não faz nada.")
        return log_eventos

    if tipo_acao == "defender":
        log_eventos.append(f"{ator.nome} assume uma postura defensiva para recuperar o fôlego.")
        # TODO: Aplicar um buff de defesa por 1 turno.
        return log_eventos

    if tipo_acao == "ataque_basico":
        ataque = acao.get("ataque")
        if not ataque or not alvo_entidade:
            log_eventos.append(f"{ator.nome} tenta atacar, mas algo deu errado.")
            return log_eventos

        log_eventos.append(f"{ator.nome} usa {ataque['nome']} em {alvo_entidade.nome}!")

        # Consome o recurso (stamina) para o ataque.
        custo = ataque.get("custo_stamina", 0)
        if ator.stamina_atual < custo:
            log_eventos.append(f"{ator.nome} não tem vigor suficiente para {ataque['nome']}!")
            return log_eventos
        ator.stamina_atual -= custo

        # Lógica de Acerto vs. Esquiva
        chance_acerto_base = ator.precisao / (ator.precisao + alvo_entidade.esquiva) if (ator.precisao + alvo_entidade.esquiva) > 0 else 0.5
        chance_acerto_final = min(0.95, max(0.10, chance_acerto_base * ataque.get("mod_precisao", 1.0)))

        if random.random() > chance_acerto_final:
            log_eventos.append(f"{alvo_entidade.nome} se esquiva do ataque de {ator.nome}!")
            return log_eventos

        # Lógica de Cálculo de Dano
        multiplicador_dano = ataque.get("multiplicador_dano", 1.0)
        tipo_dano = ataque.get("tipo_dano", "fisico")

        if tipo_dano == "fisico":
            dano_base_personagem = ator.ataque_fisico + ator.dano_arma_bonus
            dano_base = dano_base_personagem * multiplicador_dano
            defesa_alvo = alvo_entidade.defesa_fisica
        else: # dano_magico
            dano_base = ator.poder_magico * multiplicador_dano
            defesa_alvo = alvo_entidade.defesa_magica

        dano_final = max(0, int(dano_base - defesa_alvo))

        # Lógica de Acerto Crítico
        if random.random() < ator.chance_critico:
            dano_final = int(dano_final * ator.multiplicador_critico)
            log_eventos.append(f"ACERTO CRÍTICO! 🔥")

        alvo_entidade.tomar_dano(dano_final, tipo_dano)
        log_eventos.append(f"{alvo_entidade.nome} tomou {dano_final} de dano.")

    elif tipo_acao == "usar_habilidade":
        habilidade = acao.get("habilidade")

        # Consome o recurso (MP ou Stamina) para a habilidade.
        custo = habilidade.get("custo_valor", 0)
        recurso_tipo = habilidade.get("custo_tipo")
        if recurso_tipo == "mp":
            ator.mp_atual -= custo
        elif recurso_tipo == "stamina":
            ator.stamina_atual -= custo

        # Determina os alvos com base no tipo_alvo da habilidade.
        tipo_alvo_hab = habilidade.get("tipo_alvo")
        alvos = []
        if tipo_alvo_hab == "inimigo_unico": alvos = [alvo_entidade]
        elif tipo_alvo_hab == "inimigos_area": alvos = [i for i in todos_inimigos if i.esta_vivo()]
        elif tipo_alvo_hab == "aliado_unico": alvos = [alvo_entidade]
        elif tipo_alvo_hab == "aliados_area": alvos = [a for a in todos_aliados if a.esta_vivo()]
        elif tipo_alvo_hab == "self": alvos = [ator]

        log_eventos.extend(aplicar_efeitos_habilidade(ator, alvos, habilidade))

    return log_eventos

def _regenerar_recursos(personagem: 'Personagem') -> list[str]:
    """
    Restaura uma pequena quantidade de Vigor e Mana no início do turno de um personagem
    e também processa os efeitos de status ativos.

    Args:
        personagem ('Personagem'): O personagem cujos recursos serão regenerados.

    Returns:
        list[str]: Um log de eventos com os resultados (pode ser vazio se nada acontecer).
    """
    # Regeneração de Vigor: 10% do máximo + um bônus de Constituição.
    vigor_regen = int(personagem.stamina_max * 0.10 + personagem.constituicao / 2)
    personagem.stamina_atual = min(personagem.stamina_max, personagem.stamina_atual + vigor_regen)

    # Regeneração de Mana: 3% do máximo + um bônus de Sabedoria.
    mana_regen = int(personagem.mp_max * 0.03 + personagem.sabedoria / 2)
    personagem.mp_atual = min(personagem.mp_max, personagem.mp_atual + mana_regen)

    # Processa buffs, debuffs, DoTs, HoTs, etc.
    log_efeitos = processar_efeitos_de_turno(personagem)
    return log_efeitos
