# -*- coding: utf-8 -*-
"""
================================================================================================
MOTOR: UTILITÁRIOS - ROLADOR DE DADOS
================================================================================================
Este módulo fornece uma função para rolar dados baseada em uma string de notação
padrão de RPG (ex: "1d6", "2d4+2").
"""

import random
import re

def rolar_dados(notacao_dado: str) -> int:
    """
    Rola dados com base em uma string de notação (ex: "1d6", "2d8+4").

    Args:
        notacao_dado (str): A string no formato 'NdX+M' ou 'NdX'.

    Returns:
        int: O resultado da rolagem. Retorna 0 se a notação for inválida.
    """
    # Regex para capturar os componentes: (N)d(X)+(M)
    padrao = re.compile(r"(\d+)d(\d+)(?:\+(\d+))?")
    match = padrao.match(notacao_dado.lower())

    if not match:
        # Se for apenas um número fixo (ex: "15")
        if notacao_dado.isdigit():
            return int(notacao_dado)
        print(f"AVISO: Notação de dado inválida: '{notacao_dado}'. Retornando 0.")
        return 0

    numero_de_dados = int(match.group(1))
    lados_do_dado = int(match.group(2))
    modificador = int(match.group(3)) if match.group(3) else 0

    resultado_total = 0
    for _ in range(numero_de_dados):
        resultado_total += random.randint(1, lados_do_dado)

    return resultado_total + modificador

# Bloco de teste
if __name__ == "__main__":
    testes = ["1d6", "2d4+2", "1d20", "3d8+5", "10", "invalido", "d6"]
    for teste in testes:
        resultado = rolar_dados(teste)
        print(f"Rolando '{teste}': Resultado = {resultado}")
