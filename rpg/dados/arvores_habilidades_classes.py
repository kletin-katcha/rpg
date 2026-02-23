"""Árvores específicas de classes iniciais, extras e raciais."""
from .arvores_habilidades_massivas import gerar_ramificacoes
from .classes_iniciais import CLASSES_INICIAIS
from .classes_extras import CLASSES_EXTRAS
from .classes_unicas_raciais import CLASSES_UNICAS_RACIAIS

ARVORES_HABILIDADES_CLASSES = {}
for id_classe in list(CLASSES_INICIAIS.keys()) + list(CLASSES_EXTRAS.keys()) + list(CLASSES_UNICAS_RACIAIS.keys()):
    ARVORES_HABILIDADES_CLASSES[id_classe] = {
        "nome": f"Trilha de {id_classe.replace('_', ' ').title()}",
        "ramificacoes": gerar_ramificacoes(f"classe_{id_classe}", id_classe),
    }
