"""Catálogos centrais do jogo reboot."""

RACAS = {
    "humano": {"nome": "Humano", "bonus": {"forca": 1}},
    "elfo": {"nome": "Elfo", "bonus": {"inteligencia": 1}},
    "anao": {"nome": "Anão", "bonus": {"constituicao": 1}},
}

SUB_RACAS = {
    "humano": {
        "nordico": {"nome": "Nórdico", "bonus": {"constituicao": 1}},
        "imperial": {"nome": "Imperial", "bonus": {"carisma": 1}},
    },
    "elfo": {
        "alto": {"nome": "Alto Elfo", "bonus": {"inteligencia": 1}},
        "silvestre": {"nome": "Elfo Silvestre", "bonus": {"destreza": 1}},
    },
    "anao": {
        "montanha": {"nome": "Anão da Montanha", "bonus": {"forca": 1}},
        "profundo": {"nome": "Anão Profundo", "bonus": {"sabedoria": 1}},
    },
}

CLASSES = {
    "guerreiro": {"nome": "Guerreiro", "habilidades": ["ataque_poderoso"]},
    "mago": {"nome": "Mago", "habilidades": ["misseis_arcanos"]},
    "ladino": {"nome": "Ladino", "habilidades": ["ataque_furtivo"]},
}
