from typing import List, TYPE_CHECKING, Dict, Any
from ..utilitarios import funcoes_gerais, narrador
import random
from ..entidades.efeito import Efeito # Importar a classe Efeito

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem
    from ..entidades.monstro import Monstro

def aplicar_efeito(ator: 'Personagem', alvo: 'Personagem', efeito_data: Dict):
    """Aplica um único efeito de uma habilidade."""
    tipo_efeito = efeito_data.get("tipo")

    if tipo_efeito == "dano_fisico":
        # TODO: Implementar lógica de escala e multiplicadores
        dano_base = ator.ataque_fisico * efeito_data.get("multiplicador_dano", 1.0)
        dano_final = max(0, dano_base - alvo.defesa_fisica)
        alvo.tomar_dano(int(dano_final))

    elif tipo_efeito == "dano_magico":
        # TODO: Implementar lógica de escala e multiplicadores
        dano_base = ator.poder_magico * efeito_data.get("multiplicador_dano", 1.0)
        dano_final = max(0, dano_base - alvo.defesa_magica)
        alvo.tomar_dano(int(dano_final))

    elif tipo_efeito == "cura":
        # TODO: Implementar lógica de escala e multiplicadores
        cura = ator.poder_magico * efeito_data.get("multiplicador_cura", 1.0)
        alvo.curar(int(cura))

    elif tipo_efeito == "aplicar_efeito":
        # TODO: Criar e registrar objetos de Efeito a partir dos IDs
        narrador.narrar(f"{alvo.nome} é afetado por {efeito_data.get('id_efeito')}!")

def executar_acao(ator: 'Personagem', acao: Dict, todos_aliados: List['Personagem'], todos_inimigos: List['Personagem']):
    """Processa uma ação decidida pelo jogador ou IA."""
    tipo_acao = acao.get("tipo")
    alvo = acao.get("alvo")

    if not alvo:
        narrador.narrar(f"{ator.nome} não encontrou um alvo válido e perdeu o turno.")
        return

    if tipo_acao == "ataque_basico":
        narrador.narrar(f"{ator.nome} ataca {alvo.nome}!")
        dano = max(0, ator.ataque_fisico - alvo.defesa_fisica)
        alvo.tomar_dano(dano)

    elif tipo_acao == "usar_habilidade":
        habilidade = acao.get("habilidade")
        narrador.narrar(f"{ator.nome} usa {habilidade['nome']} em {alvo.nome}!")

        # Deduz o custo da habilidade
        custo = habilidade.get("custo_valor", 0)
        if habilidade.get("custo_tipo") == "mp":
            ator.mp_atual -= custo
        elif habilidade.get("custo_tipo") == "stamina":
            ator.stamina_atual -= custo

        # Aplica os efeitos da habilidade
        for efeito_data in habilidade.get("efeitos", []):
            aplicar_efeito(ator, alvo, efeito_data)

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
        acao_jogador_dict = menu_acao_jogador(jogador, inimigos)
        if acao_jogador_dict:
            if acao_jogador_dict.get("tipo") == "fugir":
                narrador.narrar("Você tenta fugir...")
                if random.random() < 0.3: # 30% de chance de fuga
                    narrador.narrar("Você conseguiu escapar!")
                    return False # Fuga não é vitória
                else:
                    narrador.narrar("A fuga falhou!")
            else:
                executar_acao(jogador, acao_jogador_dict, [jogador], inimigos)
        else:
            continue # Pula o turno se a ação foi inválida

        # Verificar se a batalha terminou após o turno do jogador
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

    # Fim da batalha
    funcoes_gerais.imprimir_cabecalho("Fim da Batalha", nivel=2)
    if jogador.esta_vivo():
        narrador.narrar("Você venceu a batalha!")
        # Distribuir recompensas
        xp_total = sum(i.xp_recompensa for i in inimigos)
        ouro_total = sum(i.ouro for i in inimigos)

        jogador.ganhar_xp(xp_total)
        jogador.ouro += ouro_total
        narrador.narrar(f"Você ganhou {ouro_total} de ouro.")

        # TODO: Gerar e distribuir loot
    else:
        narrador.narrar("Você foi derrotado...")
        # TODO: Implementar lógica de game over ou meta-progressão

    return jogador.esta_vivo()

def menu_acao_jogador(jogador: 'Personagem', inimigos: List['Monstro']) -> Dict:
    """Exibe o menu de ações do jogador e retorna a ação como um dicionário."""
    while True:
        print("\n--- AÇÕES ---")
        print("1. Atacar")
        print("2. Habilidade (não impl.)")
        print("3. Item (não impl.)")
        print("4. Fugir")

        escolha = input("O que você faz? ")
        if escolha == '1':
            alvo = escolher_alvo(inimigos)
            if alvo:
                return {"tipo": "ataque_basico", "alvo": alvo}
            return None # Cancelou a escolha de alvo
        elif escolha == '4':
            return {"tipo": "fugir"}
        else:
            print("Ação inválida ou não implementada.")
            return None

def escolher_alvo(inimigos: List['Monstro']) -> 'Monstro':
    """Permite ao jogador escolher um alvo entre os inimigos vivos."""
    inimigos_vivos = [i for i in inimigos if i.esta_vivo()]
    if not inimigos_vivos:
        return None
    if len(inimigos_vivos) == 1:
        return inimigos_vivos[0]

    while True:
        print("\nEscolha um alvo:")
        for idx, inimigo in enumerate(inimigos_vivos, 1):
            print(f"{idx}. {inimigo.nome}")

        escolha = input("Alvo: ")
        if escolha.isdigit():
            idx_escolhido = int(escolha) - 1
            if 0 <= idx_escolhido < len(inimigos_vivos):
                return inimigos_vivos[idx_escolhido]
        print("Alvo inválido.")
