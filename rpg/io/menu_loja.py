from typing import TYPE_CHECKING
from ..utilitarios import funcoes_gerais
from ..dados.lojas import LOJAS
from ..dados.itens import TODOS_OS_ITENS
from ..sistemas import loja as sistema_loja

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def loja_ui(jogador: 'Personagem', id_loja: str):
    """
    Interface principal para uma loja.
    """
    loja_data = LOJAS.get(id_loja)
    if not loja_data:
        print(f"Erro: Loja com ID '{id_loja}' não encontrada.")
        funcoes_gerais.pausar()
        return

    estado_atual = "principal" # pode ser 'principal', 'comprar', 'vender'
    mensagem_status = ""

    while True:
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho(loja_data["nome_loja"])
        print(f"Seu Ouro: {jogador.ouro}\n")

        if mensagem_status:
            print(f">> {mensagem_status}\n")
            mensagem_status = ""

        if estado_atual == "principal":
            print("1. Comprar")
            print("2. Vender")
            print("3. Sair")
            escolha = input("\n> ").strip()
            if escolha == '1':
                estado_atual = "comprar"
            elif escolha == '2':
                estado_atual = "vender"
            elif escolha == '3':
                print(f"\n'Volte sempre!'")
                funcoes_gerais.pausar()
                break
            else:
                mensagem_status = "Opção inválida."

        elif estado_atual == "comprar":
            print("--- Itens à Venda ---\n")
            inventario_loja = loja_data["inventario"]
            for i, id_item in enumerate(inventario_loja, 1):
                preco = sistema_loja.get_preco_compra(id_item, loja_data)
                nome_item = TODOS_OS_ITENS.get(id_item, {}).get("nome", "Item Desconhecido")
                print(f"{i}. {nome_item} - {preco} ouro")

            print(f"\n{len(inventario_loja) + 1}. Voltar")
            escolha = input("\nO que você quer comprar? > ").strip()

            if escolha.isdigit():
                idx_escolha = int(escolha) - 1
                if 0 <= idx_escolha < len(inventario_loja):
                    id_item_comprar = inventario_loja[idx_escolha]
                    # Por enquanto, compra apenas 1 por vez para simplificar
                    mensagem_status = sistema_loja.comprar_item(jogador, loja_data, id_item_comprar, 1)
                elif idx_escolha == len(inventario_loja):
                    estado_atual = "principal"
                else:
                    mensagem_status = "Opção inválida."
            else:
                mensagem_status = "Por favor, insira um número."

        elif estado_atual == "vender":
            print("--- Seus Itens para Vender ---\n")
            itens_vendaveis = list(jogador.inventario.items())
            if not itens_vendaveis:
                print("Você não tem nada para vender.")
                print("\n1. Voltar")
            else:
                for i, (id_item, dados_item) in enumerate(itens_vendaveis, 1):
                    preco = sistema_loja.get_preco_venda(id_item, loja_data)
                    nome_item = dados_item["item"].nome
                    quantidade = dados_item["quantidade"]
                    print(f"{i}. {nome_item} (x{quantidade}) - {preco} ouro cada")
                print(f"\n{len(itens_vendaveis) + 1}. Voltar")

            escolha = input("\nO que você quer vender? > ").strip()

            if escolha.isdigit():
                idx_escolha = int(escolha) - 1
                if 0 <= idx_escolha < len(itens_vendaveis):
                    id_item_vender, _ = itens_vendaveis[idx_escolha]
                    # Por enquanto, vende apenas 1 por vez para simplificar
                    mensagem_status = sistema_loja.vender_item(jogador, loja_data, id_item_vender, 1)
                elif idx_escolha == len(itens_vendaveis) or not itens_vendaveis:
                    estado_atual = "principal"
                else:
                    mensagem_status = "Opção inválida."
            else:
                mensagem_status = "Por favor, insira um número."
