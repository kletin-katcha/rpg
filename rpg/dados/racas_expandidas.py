RACAS_EXPANDIDAS = {
    "fae": {
        "nome": "Fae",
        "descricao": "Seres feéricos com grande afinidade mágica e mobilidade elevada.",
        "modificadores_stats": {"destreza": 2, "inteligencia": 2, "constituicao": -1},
        "habilidades_raciais": ["passo_etereo"],
        "variacoes": [
            {"nome": "Luz-da-Aurora", "descricao": "Fae ligados à luz e cura.", "modificadores_stats": {"sabedoria": 1}},
            {"nome": "Véu Noturno", "descricao": "Fae sombrios de emboscada.", "modificadores_stats": {"destreza": 1}},
        ],
    },
    "draconato": {
        "nome": "Draconato",
        "descricao": "Descendentes de dragões, resistentes e poderosos em combate direto.",
        "modificadores_stats": {"forca": 2, "constituicao": 2, "carisma": 1},
        "habilidades_raciais": ["sopro_draconico"],
        "variacoes": [
            {"nome": "Escama Rubra", "descricao": "Draconatos voltados ao fogo.", "modificadores_stats": {"forca": 1}},
            {"nome": "Escama Azure", "descricao": "Draconatos focados em resistência arcana.", "modificadores_stats": {"defesa_magica": 1}},
        ],
    },
}
