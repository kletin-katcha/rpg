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
}
