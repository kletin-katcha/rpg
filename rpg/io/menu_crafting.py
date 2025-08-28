from typing import TYPE_CHECKING
from ..utilitarios import funcoes_gerais
from ..dados.receitas import RECEITAS
from ..dados.itens import TODOS_OS_ITENS
from ..sistemas import crafting as sistema_crafting

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def crafting_ui(jogador: 'Personagem', tipo_estacao: str):
    """
    Interface principal para uma estação de trabalho de crafting.
    """
    mensagem_status = ""

    while True:
        funcoes_gerais.limpar_tela()
        nome_estacao = tipo_estacao.replace('_', ' ').title()
        funcoes_gerais.imprimir_cabecalho(f"Estação: {nome_estacao}")

        if mensagem_status:
            print(f">> {mensagem_status}\n")
            mensagem_status = ""

        # Filtra as receitas para a estação atual
        receitas_disponiveis = {
            id_receita: dados for id_receita, dados in RECEITAS.items()
            if dados["tipo_estacao"] == tipo_estacao
        }

        if not receitas_disponiveis:
            print("Não há receitas disponíveis para esta estação.")
            funcoes_gerais.pausar()
            return

        print("Receitas disponíveis (as que você pode criar estão em verde):\n")

        receitas_listadas = list(receitas_disponiveis.values())
        for i, receita in enumerate(receitas_listadas, 1):
            pode_criar = sistema_crafting.pode_criar(jogador, receita)
            cor = funcoes_gerais.COR_VERDE if pode_criar else funcoes_gerais.COR_BRANCA

            nome_item_criado = TODOS_OS_ITENS.get(receita["id_item_criado"], {}).get("nome", receita["id_item_criado"])
            print(f"{cor}{i}. {nome_item_criado}{funcoes_gerais.COR_RESET}")

            for ingrediente in receita["ingredientes"]:
                id_ingrediente = ingrediente["id_item"]
                qtd_necessaria = ingrediente["quantidade"]

                dados_ingrediente = jogador.inventario.get(id_ingrediente, {"quantidade": 0})
                qtd_jogador = dados_ingrediente["quantidade"]
                nome_ingrediente = TODOS_OS_ITENS.get(id_ingrediente, {}).get("nome", id_ingrediente)

                cor_ingrediente = funcoes_gerais.COR_VERDE if qtd_jogador >= qtd_necessaria else funcoes_gerais.COR_VERMELHA
                print(f"  - {nome_ingrediente}: {cor_ingrediente}{qtd_jogador}/{qtd_necessaria}{funcoes_gerais.COR_RESET}")
            print("-" * 20)

        print(f"\n{len(receitas_listadas) + 1}. Sair")
        escolha = input("\nEscolha uma receita para criar ou saia: > ").strip()

        if escolha.isdigit():
            idx_escolha = int(escolha) - 1
            if 0 <= idx_escolha < len(receitas_listadas):
                receita_escolhida = receitas_listadas[idx_escolha]
                mensagem_status = sistema_crafting.criar_item(jogador, receita_escolhida)
            elif idx_escolha == len(receitas_listadas):
                break # Sair
            else:
                mensagem_status = "Opção inválida."
        else:
            mensagem_status = "Por favor, insira um número."
