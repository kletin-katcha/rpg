# ==============================================================================
# ARQUIVO DE DADOS: LOJAS
# ==============================================================================
#
# Este arquivo contém as definições para todas as lojas e vendedores do jogo.
#
# A estrutura é um dicionário onde a chave é o ID da loja e o valor é
# outro dicionário com os detalhes da loja.
#
# - nome_loja: O nome que será exibido na UI.
# - inventario: Uma lista de IDs de itens que a loja vende.
# - multiplicador_preco_compra: O preço base do item * este valor é o que
#   o jogador paga. (Ex: 1.25 = 25% de margem de lucro para a loja).
# - multiplicador_preco_venda: O preço base do item * este valor é o que
#   o jogador recebe ao vender. (Ex: 0.75 = jogador recebe 75% do valor).
#
# ==============================================================================

LOJAS = {
    "ferreiro_vila": {
        "nome_loja": "Forja 'O Aço Resoluto'",
        "inventario": [
            "espada_curta_ferro",
            "adaga_de_ferro",
            "machadinha",
            "maca_simples",
            "escudo_de_madeira",
            "peitoral_de_couro_batido",
            "armadura_de_couro_leve"
        ],
        "multiplicador_preco_compra": 1.3,
        "multiplicador_preco_venda": 0.7
    },

    "alquimista_vila": {
        "nome_loja": "Boticário da Elara",
        "inventario": [
            "pocao_cura_fraca",
            "pocao_mana_fraca"
        ],
        "multiplicador_preco_compra": 1.5,
        "multiplicador_preco_venda": 0.5
    }
}
