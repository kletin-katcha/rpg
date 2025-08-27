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
    },

    "estilo_do_bebado": {
        "nome": "Estilo do Bêbado",
        "tipo": "passiva",
        "descricao": "Seus movimentos imprevisíveis tornam você mais difícil de acertar e seus golpes mais fortes. Concede um bônus em esquiva e ataque.",
        "efeitos": [
            {"tipo": "modificador_stat", "atributo": "esquiva", "valor": 10},
            {"tipo": "modificador_stat", "atributo": "ataque_fisico", "valor": 5}
        ]
    }
}
