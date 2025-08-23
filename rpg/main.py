import random
from typing import TYPE_CHECKING

# Importação dos módulos do projeto
from .entidades.personagem import Personagem
from .entidades.monstro import Monstro
from .io import menu, criacao_personagem, salvar_carregar
from .sistemas import combate
from .utilitarios import funcoes_gerais
from .dados.monstros_area1 import MONSTROS_AREA1

if TYPE_CHECKING:
    from entidades.personagem import Personagem

# --- Fábricas de Entidades (Funções de Ajuda) ---

def criar_monstro_por_id(id_monstro: str) -> Monstro:
    """Cria uma instância de Monstro a partir dos dados do dicionário."""
    dados_monstro = MONSTROS_AREA1.get(id_monstro)
    if not dados_monstro:
        raise ValueError(f"Monstro com ID '{id_monstro}' não encontrado.")

    # Habilidades são apenas strings por enquanto, vamos passar a lista
    habilidades = dados_monstro.get("habilidades", [])

    # A classe Monstro espera uma lista de dicionários para a loot table
    loot_table = dados_monstro.get("loot_table", [])

    return Monstro(
        id_monstro=id_monstro,
        nome=dados_monstro["nome"],
        nivel=dados_monstro["nivel"],
        familia=dados_monstro["familia"],
        xp_recompensa=dados_monstro["xp_recompensa"],
        ouro_recompensa=dados_monstro["ouro_recompensa"],
        stats_base=dados_monstro["stats_base"],
        habilidades_ids=habilidades,
        loot_table=loot_table,
        comportamento_ia=dados_monstro.get("comportamento_ia", "agressivo")
    )


# --- Loops de Jogo ---

def jogar(jogador: 'Personagem'):
    """O loop principal de gameplay para um personagem ativo."""
    while jogador.esta_vivo():
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho("FLORESTA DOS Sussurros", nivel=2)
        print("Você está na entrada de uma floresta escura. O ar é pesado e úmido.")
        print("\nO que você faz?")
        print("1. Explorar a floresta")
        print("2. Ver status do personagem")
        print("3. Salvar Jogo")
        print("4. Sair para o Menu Principal")

        escolha = input("\nSua escolha: ")

        if escolha == '1':
            if random.random() < 0.75: # 75% de chance de encontro
                id_monstro_encontrado = random.choice(list(MONSTROS_AREA1.keys()))
                monstro = criar_monstro_por_id(id_monstro_encontrado)
                combate.iniciar_batalha(jogador, [monstro])
            else:
                print("\nVocê explora a floresta, mas não encontra nada de interessante, apenas o som do vento nas árvores.")
            funcoes_gerais.pausar()

        elif escolha == '2':
            funcoes_gerais.limpar_tela()
            funcoes_gerais.imprimir_cabecalho("Status do Personagem", nivel=2)
            print(jogador)
            funcoes_gerais.pausar()

        elif escolha == '3':
            nome_save = input("Digite o nome para o seu save: ").strip()
            if nome_save:
                salvar_carregar.salvar_jogo(jogador, nome_save)
            else:
                print("Nome de save inválido.")
            funcoes_gerais.pausar()

        elif escolha == '4':
            print("\nVoltando ao menu principal...")
            funcoes_gerais.pausar()
            break

        else:
            print("\nEscolha inválida.")
            funcoes_gerais.pausar()

    if not jogador.esta_vivo():
        funcoes_gerais.imprimir_cabecalho("FIM DE JOGO", nivel=1)
        # TODO: Chamar sistema de meta.py aqui
        print("Sua jornada termina aqui, mas seu legado pode continuar...")
        funcoes_gerais.pausar()


def main():
    """O loop principal do jogo, que gerencia os menus."""
    while True:
        escolha_menu = menu.exibir_menu_principal()

        if escolha_menu == "novo_jogo":
            jogador_ativo = criacao_personagem.iniciar_criacao_personagem()
            jogar(jogador_ativo)

        elif escolha_menu == "carregar_jogo":
            nome_save = menu.menu_carregar_jogo()
            if nome_save:
                jogador_ativo = salvar_carregar.carregar_jogo(nome_save)
                if jogador_ativo:
                    jogar(jogador_ativo)

        elif escolha_menu == "sair":
            funcoes_gerais.limpar_tela()
            print("\nObrigado por jogar!\n")
            break

if __name__ == "__main__":
    main()
