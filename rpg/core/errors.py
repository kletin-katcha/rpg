class RPGError(Exception):
    """Erro base da aplicação."""


class RegraNegocioError(RPGError):
    """Violação de regra do domínio."""


class RecursoInsuficienteError(RegraNegocioError):
    """Falha por recurso insuficiente (ouro, energia, materiais)."""
