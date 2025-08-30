# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ███████╗██╗   ██╗███╗   ██╗ ██████╗██╗██████╗ ██╗     ███████╗ ██████╗  █████╗ ██╗         ##
##    ██╔════╝██║   ██║████╗  ██║██╔════╝██║██╔══██╗██║     ██╔════╝██╔═══██╗██╔══██╗██║         ##
##    █████╗  ██║   ██║██╔██╗ ██║██║     ██║██████╔╝██║     █████╗  ██║   ██║███████║██║         ##
##    ██╔══╝  ██║   ██║██║╚██╗██║██║     ██║██╔═══╝ ██║     ██╔══╝  ██║   ██║██╔══██║██║         ##
##    ██║     ╚██████╔╝██║ ╚████║╚██████╗██║██║     ███████╗███████╗╚██████╔╝██║  ██║███████╗    ##
##    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝╚═╝     ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
MÓDULO DE FUNÇÕES GERAIS E UTILITÁRIAS
================================================================================================
Este módulo, `funcoes_gerais.py`, é a "caixa de ferramentas" central do projeto. Ele contém
um conjunto de funções auxiliares de propósito geral que são usadas por diversos outros
módulos, desde o `main.py` até os sistemas do `motor_jogo` e as telas da `interface_terminal`.

-------------------------
-- PROPÓSITO E ESCOPO --
-------------------------
O objetivo principal deste módulo é promover a reutilização de código e garantir a
consistência em operações comuns, como:
1.  **Interação com o Console:** Limpar a tela, fazer pausas, formatar texto.
2.  **Manipulação de Dados:** Funções para trabalhar com strings, números e outras
    estruturas de dados de forma padronizada.
3.  **Lógica de Jogo Genérica:** Funções que encapsulam mecânicas comuns, como rolar
    dados ou fazer sorteios baseados em probabilidade.
4.  **Depuração e Logging:** Ferramentas para ajudar no desenvolvimento e na identificação
    de problemas.

Ao centralizar essas funções aqui, evitamos a duplicação de código em diferentes partes
do projeto, o que torna a manutenção muito mais simples. Uma mudança em como a tela é
limpa, por exemplo, só precisa ser feita em um único lugar.

---------------------------------
-- PREPARAÇÃO PARA O FUTURO --
---------------------------------
Embora muitas funções aqui sejam focadas na interface de terminal, elas são projetadas
com a futura interface gráfica em mente. Funções de lógica pura (como `rolar_dados`)
podem ser usadas por qualquer interface. Funções de apresentação (como `desenhar_caixa`)
terão comentários indicando como poderiam ser adaptadas ou substituídas por um
equivalente gráfico (por exemplo, um widget de `Frame` em Tkinter).
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
# Importações da biblioteca padrão, necessárias para as funções deste módulo.
import os
import sys
import time
import random
from typing import List, Tuple, Any

# ==============================================================================================
# == SEÇÃO 2: FUNÇÕES DE CONTROLE DE TELA E RITMO ==============================================
# ==============================================================================================
# Este conjunto de funções lida com a manipulação básica do console e o controle do
# ritmo do jogo, que é crucial para a experiência do usuário em um RPG textual.

def limpar_tela():
    """
    Limpa a tela do terminal para criar uma transição de tela limpa.

    Esta função de utilidade detecta o sistema operacional em que o jogo está rodando
    e usa o comando de sistema apropriado para limpar o conteúdo do console.
    Isso é essencial para uma boa experiência de usuário em aplicações de terminal,
    evitando que o texto de telas antigas se misture com o conteúdo novo.

    Esta função foi movida de `main.py` para cá para ser centralizada.

    Detalhes da Implementação:
    - `os.name`: Uma variável do módulo `os` que retorna o nome do sistema operacional.
      - 'nt': Corresponde a sistemas Windows (NT Kernel).
      - 'posix': Corresponde a sistemas baseados em Unix, como Linux e macOS.
    - `os.system()`: Executa um comando no shell do sistema.
      - 'cls': O comando para limpar a tela no Windows.
      - 'clear': O comando para limpar a tela em sistemas POSIX.
    - `_ = ...`: A atribuição a um underscore `_` é uma convenção em Python para
      indicar que o valor de retorno do comando (geralmente um código de saída)
      não é importante para a lógica seguinte e pode ser ignorado.
    """
    # Bloco try-except para o caso de o ambiente ser tão restrito que `os.system`
    # não seja permitido, embora seja extremamente raro em consoles padrão.
    try:
        # Verifica se o sistema operacional é Windows
        if os.name == 'nt':
            # Se for Windows, executa o comando 'cls' para limpar a tela.
            _ = os.system('cls')
        # Caso contrário, assume-se um sistema POSIX (Linux, macOS)
        else:
            # Se for POSIX, executa o comando 'clear'.
            _ = os.system('clear')
    except Exception as e:
        # Em caso de erro, imprime uma mensagem no erro padrão para não poluir
        # a tela do jogo, mas ainda assim fornecer feedback de depuração.
        print(f"DEBUG: Falha ao limpar a tela: {e}", file=sys.stderr)


def pausar_tela(mensagem: str = "Pressione Enter para continuar...") -> None:
    """
    Pausa a execução do programa e aguarda o jogador pressionar a tecla Enter.

    Esta função é vital para controlar o ritmo da narrativa e da apresentação de
    informações. Ela exibe uma mensagem customizável e impede que o programa

    continue até que o jogador esteja pronto, garantindo que ele tenha tempo para
    ler textos importantes, como descrições de itens, diálogos ou resultados de combate.

    Args:
        mensagem (str, optional): A mensagem a ser exibida para o jogador.
                                  O padrão é "Pressione Enter para continuar...".
                                  Pode ser alterada para algo mais contextual, como
                                  "Pressione Enter para rolar os dados..." ou
                                  "Pressione Enter para abrir o baú...".

    Exemplo de Uso:
        >>> print("Você encontrou uma espada mágica!")
        >>> pausar_tela()
        # O programa irá parar aqui até que o jogador pressione Enter.
    """
    # Bloco try-except para lidar com ambientes não-interativos onde `input()`
    # pode falhar (como visto no "smoke test" anterior).
    try:
        # Imprime uma linha em branco antes da mensagem para dar um espaçamento visual.
        print()
        # A função `input()` exibe a `mensagem` e aguarda a entrada do usuário.
        # O valor retornado pela entrada não é necessário, então o ignoramos.
        input(mensagem)
    except EOFError:
        # Em um ambiente não-interativo, um EOFError ocorrerá. Em vez de quebrar
        # o programa, nós o capturamos e simplesmente continuamos a execução.
        # Isso permite que testes automatizados ou execuções em lote não travem.
        print("\nDEBUG: EOFError capturado em pausar_tela(). Continuando sem pausa.", file=sys.stderr)
        # Uma pequena pausa para simular o tempo que um jogador levaria.
        time.sleep(0.1)
    except Exception as e:
        # Captura outras exceções inesperadas durante a entrada.
        print(f"\nDEBUG: Erro inesperado em pausar_tela(): {e}", file=sys.stderr)

# Fim da Parte 1 da criação do arquivo. Mais funções serão adicionadas abaixo.

# ==============================================================================================
# == SEÇÃO 3: FUNÇÕES DE FORMATAÇÃO DE TEXTO ===================================================
# ==============================================================================================
# Esta seção é dedicada a funções que ajudam a formatar e apresentar texto de maneira
# esteticamente agradável no terminal. Uma boa apresentação visual é fundamental para a
# imersão em um RPG textual.

def criar_cabecalho(texto: str, estilo: str = '=', largura: int = 80) -> str:
    """
    Cria uma string de cabeçalho formatada para seções do jogo.

    Esta função gera um cabeçalho visualmente distinto para separar seções
    importantes da interface, como "INVENTÁRIO", "STATUS DO PERSONAGEM", etc.
    Ela centraliza o texto e o envolve com um caractere de estilo.

    Args:
        texto (str): O texto a ser exibido no centro do cabeçalho.
        estilo (str, optional): O caractere a ser usado para a linha do cabeçalho.
                               Padrão é '='.
        largura (int, optional): A largura total do cabeçalho em caracteres.
                                 Padrão é 80, um tamanho comum para terminais.

    Returns:
        str: Uma string multi-linha contendo o cabeçalho formatado.

    Exemplo de Uso:
        >>> print(criar_cabecalho("Inventário"))
        ================================================================================
                                        Inventário
        ================================================================================
    """
    # Garante que o caractere de estilo não seja vazio.
    if not estilo:
        estilo = '='

    # Cria a linha superior e inferior do cabeçalho.
    linha = estilo * largura

    # Centraliza o texto. O `str.center(width, fillchar)` é perfeito para isso.
    # Adicionamos espaços em branco para garantir que o texto não toque nas bordas.
    texto_centralizado = f" {texto.upper()} ".center(largura, ' ')

    # Monta a string final com quebras de linha.
    return f"{linha}\n{texto_centralizado}\n{linha}"


def desenhar_caixa(
    titulo: str,
    conteudo: List[str],
    largura: int = 80,
    simbolos: Tuple[str, str, str, str, str, str] = ('╔', '╗', '╚', '╝', '═', '║')
) -> str:
    """
    Desenha uma caixa de texto estilizada com título e conteúdo.

    Esta função é extremamente útil para exibir informações de forma organizada,
    como status de personagem, descrições de itens ou menus contextuais.
    Ela usa caracteres de desenho de caixa para um visual mais refinado.

    Args:
        titulo (str): O título a ser exibido na borda superior da caixa.
        conteudo (List[str]): Uma lista de strings, onde cada string é uma linha
                              de conteúdo a ser exibida dentro da caixa.
        largura (int, optional): A largura total da caixa. Padrão é 80.
        simbolos (Tuple[str, ...], optional): Uma tupla de 6 caracteres para
            desenhar a caixa: canto superior esquerdo, superior direito,
            inferior esquerdo, inferior direito, linha horizontal, linha vertical.
            Permite customizar o estilo da caixa.

    Returns:
        str: Uma string multi-linha contendo a caixa de texto completa.
    """
    # Desempacota a tupla de símbolos para variáveis nomeadas, melhorando a legibilidade.
    canto_se, canto_sd, canto_ie, canto_id, linha_h, linha_v = simbolos

    # Calcula o espaço interno para o conteúdo.
    largura_interna = largura - 4  # 2 para as bordas verticais, 2 para o espaçamento interno.

    # Monta a linha do título
    # Ex: "╔═══ Título ══════╗"
    titulo_formatado = f" {titulo} "
    tamanho_titulo = len(titulo_formatado)
    preenchimento = largura - tamanho_titulo - 2 # -2 para os cantos
    linha_titulo = f"{canto_se}{linha_h * 2}{titulo_formatado}{linha_h * (preenchimento - 2)}{canto_sd}"

    # Inicia a construção da string da caixa com a linha do título.
    resultado = [linha_titulo]

    # Adiciona cada linha de conteúdo, formatada dentro das bordas verticais.
    for linha in conteudo:
        # Garante que a linha não exceda a largura interna.
        linha_truncada = linha[:largura_interna]
        # Adiciona padding à direita para alinhar a borda.
        linha_formatada = f"{linha_v} {linha_truncada.ljust(largura_interna)} {linha_v}"
        resultado.append(linha_formatada)

    # Adiciona a linha inferior da caixa.
    linha_inferior = f"{canto_ie}{linha_h * (largura - 2)}{canto_id}"
    resultado.append(linha_inferior)

    # Junta todas as linhas em uma única string com quebras de linha.
    return "\n".join(resultado)

# Fim da Parte 2 da criação do arquivo.

def carregar_arte_ascii(caminho: str) -> str:
    """
    Lê e retorna o conteúdo de um arquivo de texto, ideal para carregar arte ASCII.

    Esta função encapsula a lógica de abertura e leitura de arquivos de texto,
    incluindo um tratamento de erro básico. Ao centralizar essa lógica, evitamos
    repetir blocos `try...except` em vários lugares do código. A arte ASCII é
    mantida em arquivos `.txt` separados para não poluir o código fonte Python.

    Args:
        caminho (str): O caminho absoluto para o arquivo de texto (`.txt`) a ser lido.

    Returns:
        str: Uma string contendo todo o conteúdo do arquivo lido. Se o arquivo
             não for encontrado ou ocorrer outro erro de leitura, uma string
             de erro formatada é retornada para ser exibida na tela, facilitando
             a depuração de caminhos de arquivo incorretos.

    Exemplo de Uso:
        >>> arte_do_titulo = carregar_arte_ascii('/caminho/para/titulo.txt')
        >>> print(arte_do_titulo)
    """
    try:
        # O gerenciador de contexto `with` garante que o arquivo seja fechado
        # automaticamente, mesmo que ocorram erros.
        # `encoding='utf-8'` é especificado para garantir a compatibilidade com
        # caracteres especiais que possam estar na arte ASCII.
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        # Se o arquivo não existir no caminho especificado, informamos o erro.
        return f"\n!!! ERRO DE DEBUG: ARTE ASCII NÃO ENCONTRADA EM '{caminho}' !!!\n"
    except Exception as e:
        # Captura qualquer outro erro que possa ocorrer durante a leitura do arquivo.
        return f"\n!!! ERRO DE DEBUG: ERRO AO CARREGAR ARTE ASCII: {e} !!!\n"

# ==============================================================================================
# == SEÇÃO 4: FUNÇÕES DE LÓGICA DE JOGO GENÉRICA ===============================================
# ==============================================================================================
# Esta seção contém funções que implementam lógica de jogo comum e reutilizável,
# principalmente relacionada a aleatoriedade, que é a base de muitos sistemas de RPG.

def rolar_dados(numero_dados: int, lados_dado: int, bonus: int = 0) -> int:
    """
    Simula a rolagem de um ou mais dados e adiciona um bônus.

    Esta é uma função fundamental para qualquer sistema de RPG. Ela encapsula a
    lógica de rolar um número específico de dados com um certo número de lados
    (ex: 2d6, 1d20) e somar um modificador ao resultado final.

    Args:
        numero_dados (int): A quantidade de dados a serem rolados (o '2' em "2d6").
        lados_dado (int): O número de lados que cada dado possui (o '6' em "2d6").
        bonus (int, optional): Um modificador a ser somado ao resultado total.
                               Pode ser positivo ou negativo. Padrão é 0.

    Returns:
        int: A soma total das rolagens dos dados mais o bônus.

    Exemplo de Uso:
        >>> # Simula um ataque com uma espada longa (1d8) e +3 de força.
        >>> dano = rolar_dados(1, 8, 3)
    """
    # Validação de entrada para evitar erros lógicos.
    if numero_dados <= 0 or lados_dado <= 0:
        # Retorna 0 ou levanta um erro se os parâmetros forem inválidos.
        # Retornar o bônus pode ser uma opção, dependendo da regra do jogo.
        return bonus

    # Usa uma list comprehension para gerar todas as rolagens de uma vez.
    # `random.randint(a, b)` gera um número inteiro N tal que a <= N <= b.
    rolagens = [random.randint(1, lados_dado) for _ in range(numero_dados)]

    # Soma os resultados das rolagens e adiciona o bônus.
    resultado_total = sum(rolagens) + bonus

    return resultado_total


def log_simples(mensagem: str, nivel: str = "INFO") -> None:
    """
    Imprime uma mensagem de log formatada no console.

    Este é um sistema de logging muito rudimentar, usado para depuração durante o
    desenvolvimento. Ele anexa um nível à mensagem (ex: [INFO], [DEBUG], [AVISO])
    e a imprime. Em um projeto real, isso seria substituído pelo módulo `logging`
    do Python para um controle muito mais robusto.

    Args:
        mensagem (str): A mensagem a ser registrada.
        nivel (str, optional): O nível da mensagem (ex: "INFO", "DEBUG", "ERRO").
                               Padrão é "INFO".
    """
    # A implementação real poderia verificar uma flag global de debug.
    # from config import MODO_DEBUG
    MODO_DEBUG = True # Placeholder

    if MODO_DEBUG:
        # Obtém a hora atual para o timestamp do log.
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # Imprime a mensagem formatada na saída de erro padrão para não
        # interferir na interface do jogador.
        print(f"[{timestamp}] [{nivel.upper()}] - {mensagem}", file=sys.stderr)

# Fim da criação do arquivo `funcoes_gerais.py`.
