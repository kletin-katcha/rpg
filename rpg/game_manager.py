"""Orquestra fluxo de criação de personagem do reboot."""

from .catalog import RACAS, CLASSES
from .domain import EstadoJogo
from . import engine


class GameManager:
    def __init__(self):
        self.estado = EstadoJogo()

    @property
    def jogador(self):
        return self.estado.jogador

    def opcoes_etapa(self) -> dict:
        etapa = self.estado.etapa
        if etapa == "nome":
            return {"tipo": "input", "campo": "nome"}
        if etapa == "raca":
            return {"tipo": "selecao", "campo": "raca", "opcoes": list(RACAS.keys())}
        if etapa == "sub_raca":
            return {
                "tipo": "selecao",
                "campo": "sub_raca",
                "opcoes": list(engine.listar_sub_racas(self.jogador.raca).keys()),
            }
        if etapa == "classe":
            return {"tipo": "selecao", "campo": "classe", "opcoes": list(CLASSES.keys())}
        return {"tipo": "fim"}

    def processar(self, valor: str) -> None:
        etapa = self.estado.etapa
        if etapa == "nome":
            self.estado.jogador = engine.criar_personagem(valor)
            self.estado.etapa = "raca"
        elif etapa == "raca":
            engine.aplicar_raca(self.jogador, valor)
            self.estado.etapa = "sub_raca"
        elif etapa == "sub_raca":
            engine.aplicar_sub_raca(self.jogador, valor)
            self.estado.etapa = "classe"
        elif etapa == "classe":
            engine.aplicar_classe(self.jogador, valor)
            self.estado.etapa = "fim"
