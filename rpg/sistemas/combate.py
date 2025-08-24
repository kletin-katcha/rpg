from typing import List, TYPE_CHECKING, Dict, Any
from ..utilitarios import funcoes_gerais, narrador
import random
from ..entidades.efeito import Efeito
from ..dados.habilidades import TODAS_HABILIDADES

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem
    from ..entidades.monstro import Monstro

def aplicar_efeitos_habilidade(ator: 'Personagem', alvos: List['Personagem'], habilidade: Dict):
    """Aplica todos os efeitos de uma habilidade em uma lista de alvos."""
    narrador.narrar(f"{ator.nome} usa {habilidade['nome']}!")

    for efeito_data in habilidade.get("efeitos", []):
        tipo_efeito = efeito_data.get("tipo")

        for alvo in alvos:
            # Lógica de chance
            chance = efeito_data.get("chance", 1.0)
            if random.random() > chance:
                narrador.narrar(f"O efeito de {habilidade['nome']} falhou em {alvo.nome}!")
                continue

            if tipo_efeito == "dano_fisico":
                escala = getattr(ator, efeito_data.get("escala_com", "forca"))
                dano_base = escala * efeito_data.get("multiplicador_dano", 1.0)
                penetracao = efeito_data.get("penetracao_armadura", 0.0)
                defesa_alvo = alvo.defesa_fisica * (1 - penetracao)
                dano_final = max(0, dano_base - defesa_alvo)
                alvo.tomar_dano(int(dano_final), tipo_efeito)

            elif tipo_efeito == "dano_magico":
                escala = getattr(ator, efeito_data.get("escala_com", "inteligencia"))
                dano_base = escala * efeito_data.get("multiplicador_dano", 1.0)
                penetracao = efeito_data.get("penetracao_armadura", 0.0)
                defesa_alvo = alvo.defesa_magica * (1 - penetracao)
                dano_final = max(0, dano_base - defesa_alvo)
                alvo.tomar_dano(int(dano_final), tipo_efeito)

            elif tipo_efeito == "cura":
                escala = getattr(ator, efeito_data.get("escala_com", "sabedoria"))
                cura = escala * efeito_data.get("multiplicador_cura", 1.0)
                alvo.curar(int(cura))

            elif tipo_efeito == "aplicar_efeito":
                # TODO: Criar e registrar objetos de Efeito a partir dos IDs
                narrador.narrar(f"{alvo.nome} é afetado por {efeito_data.get('id_efeito')}!")

            elif tipo_efeito == "aplicar_efeito_self":
                 narrador.narrar(f"{ator.nome} é afetado por {efeito_data.get('id_efeito')}!")

def executar_acao(ator: 'Personagem', acao: Dict, todos_aliados: List['Personagem'], todos_inimigos: List['Personagem']):
    """Processa uma ação decidida pelo jogador ou IA."""
    tipo_acao = acao.get("tipo")
    alvo_entidade = acao.get("alvo")

    if tipo_acao == "ataque_basico":
        narrador.narrar(f"{ator.nome} ataca {alvo_entidade.nome}!")
        dano = max(0, ator.ataque_fisico - alvo_entidade.defesa_fisica)
        alvo_entidade.tomar_dano(dano)

    elif tipo_acao == "usar_habilidade":
        habilidade = acao.get("habilidade")

        # Deduz o custo da habilidade
        custo = habilidade.get("custo_valor", 0)
        recurso_tipo = habilidade.get("custo_tipo")
        if recurso_tipo == "mp":
            ator.mp_atual -= custo
        elif recurso_tipo == "stamina":
            ator.stamina_atual -= custo

        # Determina os alvos com base no tipo_alvo da habilidade
        tipo_alvo_hab = habilidade.get("tipo_alvo")
        alvos = []
        if tipo_alvo_hab == "inimigo_unico":
            alvos = [alvo_entidade]
        elif tipo_alvo_hab == "inimigos_area":
            alvos = todos_inimigos
        elif tipo_alvo_hab == "aliado_unico":
            alvos = [alvo_entidade]
        elif tipo_alvo_hab == "aliados_area":
            alvos = todos_aliados
        elif tipo_alvo_hab == "self":
            alvos = [ator]

        aplicar_efeitos_habilidade(ator, alvos, habilidade)

def iniciar_batalha(jogador: 'Personagem', inimigos: List['Monstro']) -> bool:
    """
    Gerencia o loop principal de uma batalha.
    Retorna True se o jogador venceu, False caso contrário.
    """
    funcoes_gerais.imprimir_cabecalho(f"Batalha contra {[i.nome for i in inimigos]}!", nivel=2)

    # Loop de batalha
    while jogador.esta_vivo() and any(i.esta_vivo() for i in inimigos):
        # Exibir status
        print("\n" + "="*20)
        print(f"{jogador.nome}: {jogador.hp_atual}/{jogador.hp_max} HP | {jogador.mp_atual}/{jogador.mp_max} MP")
        for inimigo in inimigos:
            if inimigo.esta_vivo():
                print(f"{inimigo.nome}: {inimigo.hp_atual}/{inimigo.hp_max} HP")
        print("="*20)

        # Turno do Jogador
        acao_jogador_dict = menu_acao_jogador(jogador, [jogador], inimigos)
        if acao_jogador_dict:
            if acao_jogador_dict.get("tipo") == "fugir":
                narrador.narrar("Você tenta fugir...")
                if random.random() < 0.3:
                    narrador.narrar("Você conseguiu escapar!")
                    return False
                else:
                    narrador.narrar("A fuga falhou!")
            else:
                executar_acao(jogador, acao_jogador_dict, [jogador], inimigos)
        else:
            continue

        vivos = [i for i in inimigos if i.esta_vivo()]
        if not vivos:
            break
        inimigos = vivos

        # Turno dos Inimigos
        for inimigo in inimigos:
            if inimigo.esta_vivo() and jogador.esta_vivo():
                funcoes_gerais.pausar()
                acao_inimigo = inimigo.decidir_acao(aliados=inimigos, inimigos=[jogador])
                executar_acao(inimigo, acao_inimigo, inimigos, [jogador])

    funcoes_gerais.imprimir_cabecalho("Fim da Batalha", nivel=2)
    if jogador.esta_vivo():
        narrador.narrar("Você venceu a batalha!")
        xp_total = sum(i.xp_recompensa for i in inimigos)
        ouro_total = sum(i.ouro for i in inimigos)

        jogador.ganhar_xp(xp_total)
        jogador.ouro += ouro_total
        narrador.narrar(f"Você ganhou {ouro_total} de ouro.")
    else:
        narrador.narrar("Você foi derrotado...")

    return jogador.esta_vivo()

def menu_acao_jogador(jogador: 'Personagem', aliados: List['Personagem'], inimigos: List['Monstro']) -> Dict:
    """Exibe o menu de ações do jogador e retorna a ação como um dicionário."""
    while True:
        print("\n--- AÇÕES ---")
        print("1. Atacar")
        print("2. Habilidade")
        print("3. Item (não impl.)")
        print("4. Fugir")

        escolha = input("O que você faz? ")
        if escolha == '1':
            alvo = escolher_alvo(inimigos)
            if alvo:
                return {"tipo": "ataque_basico", "alvo": alvo}
            return None
        elif escolha == '2':
            return menu_escolher_habilidade(jogador, aliados, inimigos)
        elif escolha == '4':
            return {"tipo": "fugir"}
        else:
            print("Ação inválida ou não implementada.")
            return None

def menu_escolher_habilidade(ator: 'Personagem', aliados: List['Personagem'], inimigos: List['Monstro']) -> Dict:
    """Exibe as habilidades ativas do jogador e retorna a ação de usar habilidade."""
    habilidades_ativas = [hab_id for hab_id in ator.habilidades if TODAS_HABILIDADES.get(hab_id, {}).get("tipo") == "ativa"]

    if not habilidades_ativas:
        narrador.narrar("Você não tem nenhuma habilidade ativa para usar em combate!")
        funcoes_gerais.pausar()
        return None

    while True:
        print("\n--- HABILIDADES ---")
        for i, hab_id in enumerate(habilidades_ativas, 1):
            habilidade = TODAS_HABILIDADES.get(hab_id)
            if habilidade:
                custo = habilidade.get('custo_valor', 0)
                recurso = habilidade.get('custo_tipo', 'N/A').upper()
                print(f"{i}. {habilidade['nome']} (Custo: {custo} {recurso})")
        print("0. Voltar")

        escolha = input("Escolha uma habilidade: ")
        if not escolha.isdigit():
            print("Entrada inválida.")
            continue

        escolha_idx = int(escolha)
        if escolha_idx == 0:
            return None

        if not 1 <= escolha_idx <= len(habilidades_ativas):
            print("Escolha inválida.")
            continue

        hab_id_escolhido = habilidades_ativas[escolha_idx - 1]
        habilidade = TODAS_HABILIDADES[hab_id_escolhido]

        # Verificar custo
        custo = habilidade.get('custo_valor', 0)
        recurso = habilidade.get('custo_tipo')
        if recurso == 'mp' and ator.mp_atual < custo:
            narrador.narrar("Você não tem Mana suficiente!")
            continue
        elif recurso == 'stamina' and ator.stamina_atual < custo:
            narrador.narrar("Você não tem Vigor suficiente!")
            continue

        # Escolher alvo
        alvo = None
        tipo_alvo_hab = habilidade.get("tipo_alvo")
        if "inimigo" in tipo_alvo_hab:
            alvo = escolher_alvo(inimigos)
        elif "aliado" in tipo_alvo_hab:
            alvo = escolher_alvo(aliados) # Reutiliza a função, funciona para qualquer lista de 'Personagem'
        elif tipo_alvo_hab == "self":
            alvo = ator

        if alvo:
            return {"tipo": "usar_habilidade", "habilidade": habilidade, "alvo": alvo}
        else:
            # Se a seleção de alvo foi cancelada ou falhou
            return None

def escolher_alvo(entidades: List['Personagem']) -> 'Personagem':
    """Permite ao jogador escolher um alvo entre uma lista de entidades vivas."""
    vivos = [e for e in entidades if e.esta_vivo()]
    if not vivos:
        return None
    if len(vivos) == 1:
        return vivos[0]

    while True:
        print("\nEscolha um alvo:")
        for idx, entidade in enumerate(vivos, 1):
            print(f"{idx}. {entidade.nome}")
        print("0. Cancelar")

        escolha = input("Alvo: ")
        if escolha.isdigit():
            idx_escolhido = int(escolha) - 1
            if idx_escolhido == -1:
                return None
            if 0 <= idx_escolhido < len(vivos):
                return vivos[idx_escolhido]
        print("Alvo inválido.")
