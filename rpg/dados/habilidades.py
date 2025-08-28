# ==============================================================================
# ARQUIVO DE DADOS: REGISTRO CENTRAL DE HABILIDADES
# ==============================================================================
#
# Este arquivo importa todas as listas de habilidades de outros arquivos
# e as une em um único dicionário para fácil acesso em todo o jogo.
#
# ==============================================================================

from .habilidades_fisicas import HABILIDADES_FISICAS
from .habilidades_magicas import HABILIDADES_MAGICAS
from .habilidades_raciais import HABILIDADES_RACIAIS
from .habilidades_suporte import HABILIDADES_SUPORTE
from .habilidades_passivas import HABILIDADES_PASSIVAS
from .habilidades_monstros import HABILIDADES_MONSTROS

# Dicionário mestre com todas as habilidades do jogo
TODAS_HABILIDADES = {}
TODAS_HABILIDADES.update(HABILIDADES_FISICAS)
TODAS_HABILIDADES.update(HABILIDADES_MAGICAS)
TODAS_HABILIDADES.update(HABILIDADES_RACIAIS)
TODAS_HABILIDADES.update(HABILIDADES_SUPORTE)
TODAS_HABILIDADES.update(HABILIDADES_PASSIVAS)
TODAS_HABILIDADES.update(HABILIDADES_MONSTROS)
