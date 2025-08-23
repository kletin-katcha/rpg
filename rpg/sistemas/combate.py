from typing import List, TYPE_CHECKING
from ..utilitarios import funcoes_gerais, narrador
import random

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem
    from ..entidades.monstro import Monstro

def iniciar_batalha(jogador: 'Personagem', inimigos: List['Monstro']):
    """
    Gerencia o loop principal de uma batalha.
    """
    funcoes_gerais.imprimir_cabecalho(f"Batalha contra {[i.nome for i in inimigos]}!", nivel=2)

    combatentes = [jogador] + inimigos

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
        acao_jogador = menu_acao_jogador()

        if acao_jogador == "atacar":
            alvo = escolher_alvo(inimigos)
            if alvo:
                narrador.narrar(f"{jogador.nome} ataca {alvo.nome}!")
                # Lógica de dano simplificada
                dano = max(0, jogador.ataque_fisico - alvo.defesa_fisica)
                alvo.tomar_dano(dano)

        elif acao_jogador == "fugir":
            narrador.narrar("Você tenta fugir...")
            if random.random() < 0.3: # 30% de chance de fuga
                narrador.narrar("Você conseguiu escapar!")
                return # Encerra a função de batalha
            else:
                narrador.narrar("A fuga falhou!")

        # Verificar se a batalha terminou após o turno do jogador
        if not any(i.esta_vivo() for i in inimigos):
            break

        # Turno dos Inimigos
        for inimigo in inimigos:
            if inimigo.esta_vivo():
                funcoes_gerais.pausar()
                # A IA do inimigo decide a ação
                acao_inimigo = inimigo.decidir_acao(aliados=inimigos, inimigos=[jogador])

                # Processar ação do inimigo (placeholder)
                if acao_inimigo["tipo"] == "ataque_basico":
                    narrador.narrar(f"{inimigo.nome} ataca {jogador.nome}!")
                    dano = max(0, inimigo.ataque_fisico - jogador.defesa_fisica)
                    jogador.tomar_dano(dano)
                # TODO: Implementar lógica para 'usar_habilidade'

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

def menu_acao_jogador() -> str:
    """Exibe o menu de ações do jogador e retorna a escolha."""
    while True:
        print("\n--- AÇÕES ---")
        print("1. Atacar")
        print("2. Habilidade (não impl.)")
        print("3. Item (não impl.)")
        print("4. Fugir")

        escolha = input("O que você faz? ")
        if escolha == '1':
            return "atacar"
        elif escolha == '4':
            return "fugir"
        else:
            print("Ação inválida ou não implementada.")

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
