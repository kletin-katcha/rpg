"""Árvores universais acessíveis a qualquer build."""
from .arvores_habilidades_massivas import gerar_ramificacoes

ARVORES_HABILIDADES_UNIVERSAIS = {
    "universal_combate": {"nome": "Constelação do Combate", "ramificacoes": gerar_ramificacoes("univ_combate", "Combate")},
    "universal_sobrevivencia": {"nome": "Constelação da Sobrevivência", "ramificacoes": gerar_ramificacoes("univ_sobrevivencia", "Sobrevivência")},
    "universal_metalurgia": {"nome": "Constelação da Metalurgia", "ramificacoes": gerar_ramificacoes("univ_metalurgia", "Metalurgia")},
    "universal_magia": {"nome": "Constelação Arcana", "ramificacoes": gerar_ramificacoes("univ_magia", "Magia")},
}
