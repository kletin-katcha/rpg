"""Catálogo de cidades e reinos para expansão de conteúdo e navegação."""

CIDADES_REINOS = {
    "vila_aurora": {"nome": "Vila Aurora", "reino": "valedourado", "descricao": "Centro inicial de comércio e treino."},
    "forte_ferreo": {"nome": "Forte Férreo", "reino": "martelo_negro", "descricao": "Cidade-fortaleza focada em metalurgia."},
    "porto_névoa": {"nome": "Porto Névoa", "reino": "talassar", "descricao": "Porto de mercadores e contrabandistas."},
    "santuario_celeste": {"nome": "Santuário Celeste", "reino": "luminar", "descricao": "Templos e ordens sagradas."},
    "cripta_rubra": {"nome": "Cripta Rubra", "reino": "nocthar", "descricao": "Centro de alquimia proibida e relíquias."},
}

REINOS = {
    "valedourado": {"nome": "Vale Dourado", "capital": "vila_aurora"},
    "martelo_negro": {"nome": "Martelo Negro", "capital": "forte_ferreo"},
    "talassar": {"nome": "Talassar", "capital": "porto_névoa"},
    "luminar": {"nome": "Luminar", "capital": "santuario_celeste"},
    "nocthar": {"nome": "Nocthar", "capital": "cripta_rubra"},
}
