# ==============================================================================
# ARQUIVO DE DADOS: DUNGEONS
# ==============================================================================
#
# Este arquivo contém as definições para as dungeons fixas (de história).
#
# ==============================================================================

from ..sistemas.dungeons import Room, Dungeon

DUNGEONS_FIXAS = {
    "ruinas_alkhem": {
        "nome": "Ruínas de Al'Khem",
        "descricao": "As ruínas de uma antiga fortaleza dos Guardiões, agora infestada de constructos e armadilhas.",
        "nivel_minimo": 15,
        "salas": [
            {
                "nome": "Salão de Entrada",
                "descricao": "Um grande salão com colunas quebradas. Poeira dança nos feixes de luz que entram por frestas no teto. O ar é pesado e silencioso.",
                "monstros": ["construto_guardiao_quebrado", "construto_guardiao_quebrado"]
            },
            {
                "nome": "Biblioteca Destruída",
                "descricao": "Estantes de livros tombaram e pergaminhos apodrecem no chão úmido. Construtos arcanos patrulham a área.",
                "monstros": ["construto_arcano", "construto_arcano"],
                "tesouros": [{"id_item": "grimorio_antigo_rasgado", "chance": 0.5}]
            },
            {
                "nome": "Corredor das Armadilhas",
                "descricao": "Um corredor estreito com placas de pressão visíveis no chão e buracos nas paredes.",
                "armadilhas": [{"tipo": "dardos_venenosos", "dificuldade": 12}, {"tipo": "fosso", "dificuldade": 10}]
            },
            {
                "nome": "Câmara do Altar",
                "descricao": "Uma câmara circular com um grande altar de pedra no centro. No altar, repousa um mapa antigo. Um construto massivo se ergue para proteger o local.",
                "monstros": ["construto_colosso"],
                "tesouros": [{"id_item": "mapa_das_sombras", "chance": 1.0}]
            }
        ]
    }
}

# Precisamos definir os monstros e itens em seus respectivos arquivos de dados
# Esta parte é apenas a estrutura da dungeon.
