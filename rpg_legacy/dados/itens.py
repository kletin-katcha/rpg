# ==============================================================================
# ARQUIVO DE DADOS: REGISTRO CENTRAL DE ITENS
# ==============================================================================
#
# Este arquivo irá carregar todos os itens de outros arquivos de dados
# e centralizá-los em um único dicionário para fácil acesso em todo o jogo.
#
# ==============================================================================

# Importa os dicionários de itens de arquivos específicos
from .itens_comuns import ITENS_COMUNS
# Futuramente, importaremos de outros arquivos também:
# from .itens_raros import ITENS_RAROS
# from .itens_lendarios import ITENS_LENDARIOS

# Cria o registro central
TODOS_OS_ITENS = {}
TODOS_OS_ITENS.update(ITENS_COMUNS)
# TODOS_OS_ITENS.update(ITENS_RAROS)
# TODOS_OS_ITENS.update(ITENS_LENDARIOS)
