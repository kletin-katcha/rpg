"""Regras de melhoria de estruturas urbanas e automações."""
MELHORIAS_ESTRUTURAS = {
    "oficina_basica": {
        "nivel_maximo": 3,
        "custos_por_nivel": {
            2: {"ouro": 120, "materiais": {"barra_metal_reciclado": 2}},
            3: {"ouro": 200, "materiais": {"barra_metal_reciclado": 4}},
        },
    },
    "automacao_coleta": {
        "nivel_maximo": 3,
        "custos_por_nivel": {
            2: {"ouro": 180, "materiais": {"barra_metal_reciclado": 3}},
            3: {"ouro": 260, "materiais": {"barra_metal_reciclado": 5}},
        },
    },
    "laboratorio_alquimico": {
        "nivel_maximo": 2,
        "custos_por_nivel": {
            2: {"ouro": 200, "materiais": {"gosma_de_slime": 6, "ferrao_de_vespa": 3}},
        },
    },
    "automacao_refino": {
        "nivel_maximo": 2,
        "custos_por_nivel": {
            2: {"ouro": 260, "materiais": {"barra_metal_reciclado": 4}},
        "nivel_maximo": 2,
        "custos_por_nivel": {
            2: {"ouro": 180, "materiais": {"barra_metal_reciclado": 3}},
        },
    },
}
