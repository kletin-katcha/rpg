# -*- coding: utf-8 -*-
"""
Módulo para a tela de criação de personagem na interface de terminal.

Este módulo será responsável por toda a interação com o usuário para a
criação de um novo personagem, incluindo a escolha de nome, raça, classe
e a distribuição de atributos.
"""
from typing import Dict, Any, Optional
import time

def exibir_criacao_personagem() -> Optional[Dict[str, Any]]:
    """
    Função placeholder para simular a criação de um personagem.

    No futuro, esta função conterá um loop complexo para guiar o jogador
    através da criação do personagem.

    Por enquanto, ela apenas exibe uma mensagem, espera um pouco e retorna
    um dicionário de dados de um personagem "mock" para que o fluxo do
    jogo em `main.py` possa continuar.

    Returns:
        Optional[Dict[str, Any]]: Um dicionário representando o personagem criado,
                                  ou None se a criação for cancelada.
    """
    print("\n" + "="*80)
    print(" " * 25 + "TELA DE CRIAÇÃO DE PERSONAGEM")
    print("="*80)
    print("\n... Carregando dados de raças e classes ...")
    time.sleep(1)
    print("... Apresentando opções ao jogador ...")
    time.sleep(1)
    print("\nJogador está escolhendo nome, raça, classe e atributos...")
    time.sleep(2)
    print("\nPersonagem criado com sucesso!")
    time.sleep(1.5)

    # Este é um "mock" ou "dublê" de um objeto de personagem.
    # A estrutura real será definida em `motor_jogo/entidades/personagem.py`.
    personagem_mock = {
        "nome": "Aethelred",
        "nivel": 1,
        "vida_max": 100,
        "vida_atual": 100,
        "raca": "Humano",
        "classe": "Guerreiro",
        "atributos": {
            "forca": 12,
            "destreza": 10,
            "inteligencia": 8
        }
    }

    return personagem_mock
