# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ███╗   ██╗ █████╗ ██████╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗     ██████╗ ██╗   ██╗   ##
##    ████╗  ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██╔══██╗╚██╗ ██╔╝   ##
##    ██╔██╗ ██║███████║██████╔╝██████╔╝███████║   ██║   ██║   ██║██████╔╝    ██████╔╝ ╚████╔╝    ##
##    ██║╚██╗██║██╔══██║██╔══██╗██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗    ██╔══██╗  ╚██╔╝     ##
##    ██║ ╚████║██║  ██║██║  ██║██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║    ██████╔╝   ██║      ##
##    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═════╝    ╚═╝      ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
MÓDULO DE NARRAÇÃO E APRESENTAÇÃO TEXTUAL
================================================================================================
Este módulo, `narrador.py`, é o coração da imersão textual do RPG. Ele é responsável
por toda a apresentação de texto ao jogador, desde diálogos e descrições de ambientes
até mensagens de combate. O objetivo é transformar simples `print()`s em uma experiência
narrativa rica e estilizada.

-------------------------
-- PROPÓSITO E ESCOPO --
-------------------------
As principais funcionalidades deste módulo incluem:
1.  **Narração Cadenciada:** Apresentar texto de forma lenta, simulando uma fala ou
    narração, com velocidade customizável.
2.  **Estilização de Texto:** Centralizar o uso de emojis, cores (futuramente) e outros
    elementos estilísticos para dar "sabor" ao texto.
3.  **Formatação de Conteúdo:** Criar cabeçalhos, separar parágrafos e formatar diálogos
    de maneira consistente em todo o jogo.
4.  **Abstração da Apresentação:** Isolar a lógica de como o texto é apresentado. Se no
    futuro quisermos que o texto apareça em uma caixa de GUI em vez do console, as
    mudanças seriam concentradas aqui, no "backend" da narração.

---------------------------------
-- ARQUITETURA E DESIGN --
---------------------------------
O `narrador.py` funcionará como uma API de apresentação para os outros módulos. Em vez de
um módulo de sistema (como o de combate) imprimir diretamente "Você causou 10 de dano!",
ele chamaria uma função como `narrador.narrar_evento_combate("Você causou 10 de dano! [dano]")`.
O narrador então se encarregaria de formatar a mensagem, talvez adicionar um emoji ⚔️,
e imprimi-la na tela de forma cadenciada.

Isso desacopla a lógica do jogo da sua apresentação, um princípio de design de software
fundamental para a manutenibilidade e expansão do projeto.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import sys
import time
from typing import Dict, List, Any

# Importa as funções gerais que podem ser úteis aqui.
# Usar um `try-except` é uma boa prática para garantir que, se o módulo for usado de
# forma isolada para testes, ele não quebre imediatamente.
try:
    from . import funcoes_gerais as geral
except ImportError:
    # Fallback para o caso de o módulo ser executado como script principal,
    # o que alteraria o contexto de importação.
    import funcoes_gerais as geral


# ==============================================================================================
# == SEÇÃO 2: CONSTANTES E CONFIGURAÇÕES DO NARRADOR ===========================================
# ==============================================================================================
# Dicionário para mapear contextos de jogo a emojis, centralizando a estilização.
# Adicionar um novo contexto ou mudar um emoji é fácil e não requer alterações na lógica.
MAPA_DE_EMOJIS: Dict[str, str] = {
    # Contextos de Combate
    "[dano]": "⚔️",
    "[cura]": "💖",
    "[defesa]": "🛡️",
    "[morte]": "💀",
    "[critico]": "💥",
    "[falha]": "💨",

    # Contextos de Exploração
    "[item]": "✨",
    "[tesouro]": "👑",
    "[porta]": "🚪",
    "[chave]": "🔑",
    "[perigo]": "⚠️",

    # Contextos de Interação
    "[dialogo]": "💬",
    "[missao]": "📜",
    "[recompensa]": "🏆",

    # Contextos Gerais
    "[sucesso]": "✅",
    "[erro]": "❌",
    "[info]": "ℹ️",
}

# Velocidades de texto padrão em segundos por caractere.
# Permite ajustar o ritmo da narração globalmente.
VELOCIDADE = {
    "lenta": 0.05,
    "normal": 0.03,
    "rapida": 0.01,
}

# ==============================================================================================
# == SEÇÃO 3: FUNÇÕES PRINCIPAIS DE NARRAÇÃO ===================================================
# ==============================================================================================

def formatar_emojis(texto: str) -> str:
    """
    Substitui tags de contexto no texto pelos emojis correspondentes.

    Esta função percorre o `MAPA_DE_EMOJIS` e substitui todas as ocorrências
    das chaves (ex: "[dano]") pelo seu valor de emoji correspondente (ex: "⚔️").
    Isso permite que o código de lógica do jogo use tags semânticas, e o narrador
    cuida da apresentação visual.

    Args:
        texto (str): A string de texto a ser formatada.

    Returns:
        str: O texto com as tags substituídas por emojis.

    Exemplo:
        >>> formatar_emojis("Você encontrou um item! [item]")
        'Você encontrou um item! ✨'
    """
    # Itera sobre o dicionário de emojis.
    for tag, emoji in MAPA_DE_EMOJIS.items():
        # Substitui todas as ocorrências da tag pelo emoji.
        texto = texto.replace(tag, emoji)
    return texto


def texto_lento(
    texto: str,
    velocidade: str = "normal",
    processar_emojis: bool = True,
    nova_linha: bool = True
) -> None:
    """
    Imprime um texto no console caractere por caractere para um efeito de narração.

    Esta é a função principal para apresentação de texto imersivo. Ela simula
    alguém digitando ou falando o texto, o que dá ao jogador tempo para ler e absorver
    a informação, melhorando drasticamente a experiência em um RPG textual.

    Args:
        texto (str): A string a ser impressa lentamente.
        velocidade (str, optional): A chave de velocidade a ser usada do dicionário
                                   `VELOCIDADE`. Padrão é "normal".
        processar_emojis (bool, optional): Se True, chama `formatar_emojis` antes de
                                           imprimir. Padrão é True.
        nova_linha (bool, optional): Se True, imprime uma quebra de linha após o
                                     texto terminar. Padrão é True.
    """
    # Primeiro, formata os emojis, se solicitado.
    if processar_emojis:
        texto = formatar_emojis(texto)

    # Obtém o valor numérico do delay a partir da chave de velocidade.
    # Usa `.get()` com um padrão para evitar erros se uma chave inválida for passada.
    delay = VELOCIDADE.get(velocidade, VELOCIDADE["normal"])

    # Itera sobre cada caractere da string.
    for char in texto:
        # Imprime o caractere.
        sys.stdout.write(char)
        # `flush=True` força a impressão imediata do caractere no console,
        # em vez de esperar o buffer encher. Essencial para o efeito funcionar.
        sys.stdout.flush()
        # Pausa a execução por um curto período de tempo.
        time.sleep(delay)

    # Se uma nova linha for desejada no final.
    if nova_linha:
        print() # `print()` por padrão adiciona uma quebra de linha.

# Fim da Parte 1 da criação do arquivo. Mais funções serão adicionadas abaixo.

# ==============================================================================================
# == SEÇÃO 4: FUNÇÕES DE NARRAÇÃO CONTEXTUAL ===================================================
# ==============================================================================================
# Esta seção constrói sobre as funções base para criar ferramentas de narração mais
# poderosas e contextuais, que podem ser usadas para criar cenas, diálogos e eventos.

# Dicionário para definir os "estilos" ou "personalidades" do narrador.
# Cada estilo pode ter uma velocidade de texto padrão e um prefixo/sufixo estilístico.
# Isso permite mudar o "tom" da narração com um simples parâmetro.
ESTILOS_NARRADOR = {
    "normal": {
        "velocidade": "normal",
        "prefixo": "",
        "sufixo": ""
    },
    "epico": {
        "velocidade": "normal",
        "prefixo": "📜 ",
        "sufixo": " 📜"
    },
    "sombrio": {
        "velocidade": "lenta",
        "prefixo": "💀 ",
        "sufixo": " 💀"
    },
    "pensamento": {
        "velocidade": "rapida",
        "prefixo": "💭 *(",
        "sufixo": ")*"
    },
    "sistema": {
        "velocidade": "rapida",
        "prefixo": "[SISTEMA] ",
        "sufixo": ""
    }
}

def narrar(
    texto: str,
    estilo: str = "normal",
    pausa_antes: float = 0.0,
    pausa_depois: float = 0.0,
    limpar: bool = False
) -> None:
    """
    Função de alto nível para narrar um evento ou fala no jogo.

    Esta é a principal interface que outros módulos devem usar para interagir com o
    sistema de narração. Ela combina `texto_lento`, estilos, pausas e limpeza de
    tela em uma única chamada conveniente.

    Args:
        texto (str): O texto principal a ser narrado.
        estilo (str, optional): O estilo de narração a ser usado (chave do
                               dicionário `ESTILOS_NARRADOR`). Padrão é "normal".
        pausa_antes (float, optional): Pausa em segundos ANTES de o texto ser exibido.
                                      Padrão é 0.0.
        pausa_depois (float, optional): Pausa em segundos APÓS o texto ser exibido.
                                       Padrão é 0.0.
        limpar (bool, optional): Se True, a tela será limpa antes da narração.
                                 Padrão é False.
    """
    # Se a limpeza de tela for solicitada.
    if limpar:
        geral.limpar_tela()

    # Se uma pausa antes for solicitada.
    if pausa_antes > 0:
        time.sleep(pausa_antes)

    # Obtém a configuração do estilo a partir do dicionário.
    # Usa `.get()` com o estilo "normal" como padrão para evitar erros.
    config_estilo = ESTILOS_NARRADOR.get(estilo, ESTILOS_NARRADOR["normal"])

    # Monta o texto final com prefixo e sufixo do estilo.
    texto_formatado = f"{config_estilo['prefixo']}{texto}{config_estilo['sufixo']}"

    # Chama a função de texto lento com a velocidade definida pelo estilo.
    texto_lento(texto_formatado, velocidade=config_estilo["velocidade"])

    # Se uma pausa depois for solicitada.
    if pausa_depois > 0:
        time.sleep(pausa_depois)


def criar_cabecalho_narrativo(titulo: str, subtitulo: str = "", estilo_char: str = '#') -> None:
    """
    Cria e exibe um cabeçalho narrativo estilizado para grandes eventos ou capítulos.

    Esta função é usada para momentos de grande impacto, como o início de um capítulo,
    a entrada em uma nova região ou o começo de uma batalha de chefe.

    Args:
        titulo (str): O título principal do cabeçalho (ex: "Capítulo I").
        subtitulo (str, optional): Um subtítulo opcional (ex: "O Despertar da Sombra").
                                  Padrão é "".
        estilo_char (str, optional): O caractere a ser usado para a borda ornamental.
                                     Padrão é '#'.
    """
    largura = 80
    geral.limpar_tela()
    print(estilo_char * largura)
    print(titulo.center(largura))
    if subtitulo:
        print(subtitulo.center(largura))
    print(estilo_char * largura)
    geral.pausar_tela("\nPressione Enter para iniciar...")

# Fim da Parte 2 da criação do arquivo.

# ==============================================================================================
# == SEÇÃO 5: SISTEMAS DE DIÁLOGO E ARTE =======================================================
# ==============================================================================================
# Esta seção lida com apresentações mais complexas que combinam texto e outros
# elementos visuais, como nomes de personagens ou arte ASCII.

def exibir_dialogo(nome_personagem: str, falas: List[str], cor_personagem: Any = None) -> None:
    """
    Formata e exibe um bloco de diálogo para um NPC ou personagem.

    Esta função cria um formato de diálogo consistente, mostrando o nome do
    personagem e depois narrando suas falas uma a uma. No futuro, o argumento
    `cor_personagem` seria usado para colorir o nome do personagem.

    Args:
        nome_personagem (str): O nome do personagem que está falando.
        falas (List[str]): Uma lista de strings, onde cada string é uma linha
                           de diálogo a ser narrada.
        cor_personagem (Any, optional): Placeholder para um futuro sistema de cores.
                                        Não utilizado no momento.
    """
    # Cria um cabeçalho simples para o nome do personagem.
    # Ex: "Ferreiro Thorgar diz:"
    cabecalho = f"🗣️  {nome_personagem.upper()} diz:"
    print(cabecalho)
    print("-" * (len(cabecalho) + 2)) # Linha sob o nome.

    # Itera sobre cada linha do diálogo e a narra.
    for linha in falas:
        # Usa o estilo "normal" de narração para diálogos.
        # Adiciona um pequeno recuo para separar visualmente a fala do nome.
        narrar(f"   “{linha}”", estilo="normal", pausa_depois=0.5)

    # Pausa no final para que o jogador possa ler a última fala.
    geral.pausar_tela()


def exibir_arte_narrativa(caminho_arte: str, legenda: str) -> None:
    """
    Exibe uma arte ASCII de um arquivo e a acompanha com uma legenda narrada.

    Útil para momentos em que uma imagem visual é importante, como ao encontrar
    um monstro pela primeira vez ou ao chegar em uma cidade nova.

    Args:
        caminho_arte (str): O caminho para o arquivo .txt contendo a arte ASCII.
                            Deve ser um caminho completo.
        legenda (str): O texto narrativo que descreve ou acompanha a arte.
    """
    geral.limpar_tela()

    # Carrega a arte ASCII do arquivo.
    # A função `carregar_arte_ascii` já está em `main.py`, mas para um
    # design mais limpo, ela pertenceria a `funcoes_gerais.py`.
    # Assumindo que será movida para lá.
    try:
        from .funcoes_gerais import carregar_arte_ascii as carregar_arte_geral
        arte = carregar_arte_geral(caminho_arte)
    except (ImportError, NameError):
        # Fallback caso a função ainda não tenha sido movida.
        arte = f"[ARTE DE '{caminho_arte}' NÃO PÔDE SER CARREGADA]"

    # Exibe a arte.
    print(arte)
    print("\n" * 2)

    # Narra a legenda usando um estilo de "pensamento" ou observação.
    narrar(legenda, estilo="pensamento")

    geral.pausar_tela()

# Fim da criação do arquivo `narrador.py`.
