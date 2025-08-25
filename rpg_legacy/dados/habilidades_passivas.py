# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES PASSIVAS
# ==============================================================================
#
# Este arquivo contém as definições para habilidades passivas, que concedem
# bônus permanentes ou se ativam automaticamente sob certas condições.
#
# ==============================================================================

HABILIDADES_PASSIVAS = {
    # Exemplo de habilidade passiva
    "pele_de_pedra_passiva": {
        "nome": "Pele de Pedra",
        "descricao": "Sua pele é naturalmente mais resistente, concedendo um bônus permanente de defesa.",
        "tipo": "passiva",
        "efeitos": [
            {"tipo": "modificador_stat", "atributo": "defesa_fisica", "valor": 5}
        ]
    }
}
