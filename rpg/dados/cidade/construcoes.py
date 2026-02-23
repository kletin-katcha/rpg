"""Definições de construções da cidade e pré-requisitos de expansão."""
PROJETOS_CONSTRUCAO = {
    "oficina_basica": {
        "nome": "Oficina Básica",
        "custo_ouro": 80,
        "materiais": {"caco_de_arma_enferrujada": 4},
        "descricao": "Permite melhorar processos de produção local.",
    },
    "automacao_coleta": {
        "nome": "Autômato de Coleta",
        "custo_ouro": 120,
        "materiais": {"barra_metal_reciclado": 2},
        "descricao": "Coleta recursos simples diariamente.",
        "requisito_estrutura": "oficina_basica",
    },
    "laboratorio_alquimico": {
        "nome": "Laboratório Alquímico",
        "custo_ouro": 150,
        "materiais": {"gosma_de_slime": 4, "ferrao_de_vespa": 2},
        "descricao": "Libera automações de insumos alquímicos.",
        "requisito_estrutura": "oficina_basica",
    },
    "automacao_refino": {
        "nome": "Autômato de Refino",
        "custo_ouro": 220,
        "materiais": {"barra_metal_reciclado": 3, "caco_de_arma_enferrujada": 6},
        "descricao": "Refina sucata automaticamente em barras por ciclo.",
        "requisito_estrutura": "oficina_basica",
    },
}
