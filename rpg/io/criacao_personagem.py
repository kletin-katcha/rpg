"""Compat shim legado para criação de personagem."""

from rpg.game import Game


def criar_personagem_interativo(game: Game, nome: str, raca: str, classe: str):
    return game.criar_jogador(nome, raca, classe)
