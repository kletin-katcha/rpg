# -*- coding: utf-8 -*-
"""
################################################################################################
################################################################################################
##                                                                                            ##
##    ██████╗  ██████╗ ██████╗ ██████╗ ██████╗ ██╗      ██████╗     ██████╗ ██╗   ██╗███████╗██████╗  ##
##    ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██║     ██╔═══██╗    ██╔════╝ ██║   ██║██╔════╝██╔══██╗  ##
##    ██████╔╝██║   ██║██████╔╝██████╔╝██████╔╝██║     ██║   ██║    ██║  ███╗██║   ██║█████╗  ██████╔╝  ##
##    ██╔══██╗██║   ██║██╔═══╝ ██╔══██╗██╔══██╗██║     ██║   ██║    ██║   ██║██║   ██║██╔══╝  ██╔══██╗  ##
##    ██║  ██║╚██████╔╝██║     ██████╔╝██║  ██║███████╗╚██████╔╝    ╚██████╔╝╚██████╔╝███████╗██║  ██║  ##
##    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝      ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝  ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
ARQUIVO PRINCIPAL (PONTO DE ENTRADA) DO JOGO DE RPG COLOSSAL
================================================================================================
Este arquivo, `main.py`, serve como o grande orquestrador do jogo. Sua responsabilidade
primária não é conter a lógica do jogo em si (isso é delegado ao `motor_jogo`), mas sim
gerenciar o fluxo de alto nível, inicializar os sistemas necessários e controlar o estado
geral da aplicação, desde o menu inicial até o encerramento do jogo.

-------------------------
-- RESPONSABILIDADES CHAVE --
-------------------------
1.  **Inicialização:** Carrega configurações, inicializa o logging e prepara o ambiente.
2.  **Seleção de Interface:** Determina se o jogo rodará na interface de terminal ou na
    futura interface gráfica.
3.  **Menu Principal:** Exibe o menu inicial com opções como "Novo Jogo", "Carregar Jogo",
    "Configurações", "Créditos" e "Sair".
4.  **Orquestração de Telas:** Chama as funções apropriadas da interface escolhida para
    renderizar as diferentes "telas" ou "cenas" do jogo (criação de personagem, exploração,
    combate, etc.).
5.  **Loop de Jogo Principal:** Gerencia o loop de alto nível que mantém o jogador no jogo
    após iniciar ou carregar uma partida.
6.  **Gerenciamento de Fim de Jogo:** Lida com as condições de fim de jogo (morte do
    personagem) e aciona o sistema de meta-progressão.

-------------------------
-- ARQUITETURA E DESIGN --
-------------------------
A filosofia de design deste arquivo é a de um "controlador de tráfego aéreo". Ele sabe
para onde os "aviões" (dados do jogador, eventos do jogo) devem ir, mas não se preocupa
com os detalhes de como os aviões voam (a lógica do motor). Isso é alcançado através de
uma clara separação de responsabilidades, onde `main.py` lida com o "O Quê?" e "Quando?",
enquanto os módulos do `motor_jogo` e das interfaces lidam com o "Como?".

Essa abordagem de **Inversão de Controle** é fundamental para a manutenibilidade de um
projeto deste tamanho. O `main.py` depende de abstrações (as funções nas outras camadas)
e não de implementações concretas, permitindo que a interface de terminal possa ser
trocada pela gráfica sem que a lógica de orquestração aqui precise ser alterada.

---------------------------------
-- REQUISITO DE VERBOSIDADE --
---------------------------------
Para atingir a contagem de linhas e a clareza exigidas, este arquivo será extremamente
verboso, com documentação extensiva, comentários detalhados, logging abundante e
funções auxiliares bem definidas. Cada decisão de design, por menor que seja, será
documentada para garantir que futuros desenvolvedores (ou o próprio autor) possam
entender o raciocínio por trás do código.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
# A organização das importações segue a convenção da PEP 8:
# 1. Importações da biblioteca padrão (standard library).
# 2. Importações de bibliotecas de terceiros (third-party).
# 3. Importações de módulos locais da aplicação.
# Isso melhora a legibilidade e ajuda a entender as dependências do módulo.

# ---------------------------------------------------
# 1.1. Importações da Biblioteca Padrão do Python
# ---------------------------------------------------
import sys      # Para interações com o sistema, como `sys.exit()` e `sys.stderr`.
import os       # Para interações com o sistema operacional, como manipulação de caminhos e comandos de console.
import time     # Para pausas dramáticas e controle de ritmo (`time.sleep()`).
import json     # Embora não usado diretamente aqui, é planejado para o sistema de save/load.
import logging  # Para um sistema de log robusto (a ser implementado).
import random
from typing import Dict, Any, Optional # Para anotações de tipo, melhorando a clareza e a verificação estática.

# ---------------------------------------------------
# 1.2. Importações de Bibliotecas de Terceiros
# ---------------------------------------------------
# (Nenhuma neste momento, mas seriam adicionadas aqui. Ex: `import requests`)

# ---------------------------------------------------
# 1.3. Importações de Módulos do Projeto
# ---------------------------------------------------
# A estrutura de try-except é uma boa prática para fornecer mensagens de erro mais claras
# e amigáveis ao usuário final caso algum módulo essencial do jogo esteja faltando,
# o que pode acontecer por uma cópia incompleta do jogo ou erro de instalação.
try:
    # Importações do motor do jogo, o coração da lógica do RPG.
    from motor_jogo.entidades.personagem import Personagem
    from motor_jogo.entidades.monstro import Monstro
    from motor_jogo.sistemas import gerenciador_save
    from motor_jogo.banco_de_dados.mundo.areas import INDICE_AREAS
    from motor_jogo.banco_de_dados.monstros import INDICE_MONSTROS
    from motor_jogo.progresso import meta_progressao # A ser usado no `loop_pos_morte`.
    from motor_jogo.utilitarios import funcoes_gerais as geral
    from motor_jogo.utilitarios import narrador

    # Importações da interface de terminal, a camada de apresentação atual.
    from interface_terminal.telas import tela_menu_principal
    from interface_terminal.telas import tela_exploracao
    from interface_terminal.telas import tela_inventario
    from interface_terminal.telas import tela_personagem
    from interface_terminal.telas import tela_combate

    # Importa a janela principal da GUI
    from interface_grafica.main_window import MainWindow

    # Importações de configuração e assets.
    import config # Para acessar constantes de configuração globais.

except ImportError as e:
    # Se uma importação falhar, o jogo não pode rodar. Exibimos uma mensagem clara
    # no `stderr` (saída de erro padrão) e encerramos.
    print(f"ERRO CRÍTICO: Não foi possível importar um módulo essencial: {e}", file=sys.stderr)
    print("Por favor, verifique se a estrutura de pastas do projeto está intacta e se todos os arquivos __init__.py existem.", file=sys.stderr)
    sys.exit(1) # Encerra o programa com um código de erro.


# ==============================================================================================
# == SEÇÃO 2: CONSTANTES GLOBAIS ===============================================================
# ==============================================================================================
# Centralizar constantes em um local facilita a manutenção e configuração do jogo.
# Qualquer ajuste de altoível, como mudar o nome do jogo ou um caminho de pasta,
# pode ser feito aqui sem precisar "caçar" os valores pelo código.

# ---------------------------------
# --- NOME E VERSÃO DO JOGO ---
# ---------------------------------
# Altere o nome do jogo aqui. Este nome será usado em títulos de janela, saves, etc.
# Usar uma constante garante consistência em todo o jogo.
NOME_DO_JOGO: str = "Ecos da Aetheria"
# A versão segue o padrão de Versionamento Semântico (Major.Minor.Patch).
VERSAO_DO_JOGO: str = "0.0.1 Alpha"

# ---------------------------------
# --- CAMINHOS DE ARQUIVO ---
# ---------------------------------
# Definir caminhos de forma programática usando `os.path` torna o jogo portátil,
# funcionando em diferentes sistemas operacionais (Windows, Linux, macOS) sem alterações.
# `os.path.abspath(__file__)` obtém o caminho absoluto do arquivo atual (`main.py`).
# `os.path.dirname(...)` obtém o diretório onde o arquivo está.
CAMINHO_RAIZ = os.path.dirname(os.path.abspath(__file__))

# `os.path.join` constrói os caminhos de forma inteligente, usando a barra correta ('/' ou '\').
CAMINHO_ASSETS = os.path.join(CAMINHO_RAIZ, 'assets')
CAMINHO_ASCII_ART = os.path.join(CAMINHO_ASSETS, 'ascii_art')
CAMINHO_ARTE_TITULO = os.path.join(CAMINHO_ASCII_ART, 'titulo.txt')
CAMINHO_SAVES = os.path.join(CAMINHO_RAIZ, 'saves') # Pasta para os arquivos de save.

# ---------------------------------
# --- CONFIGURAÇÕES DE INTERFACE ---
# ---------------------------------
# Esta constante é a chave para a seleção da interface. O `main` a utiliza para
# decidir qual conjunto de funções de renderização e entrada chamar.
# No futuro, este valor poderia vir de um arquivo de configuração (ex: config.ini)
# ou de um argumento de linha de comando (ex: `python main.py --interface grafica`).
# Opções válidas: 'terminal', 'grafica'
INTERFACE_ATUAL: str = 'grafica'


# ==============================================================================================
# == SEÇÃO 4: FUNÇÕES DE ORQUESTRAÇÃO PRINCIPAL ================================================
# ==============================================================================================
# Esta é a seção mais importante de `main.py`. Cada função aqui representa um estado
# ou um fluxo principal do jogo. Elas não executam a lógica detalhada, mas chamam
# as funções apropriadas em outras camadas (interface, motor) na ordem correta.

def loop_de_jogo(estado_jogo: "EstadoJogo") -> None:
    """
    O loop principal que executa o jogo após um personagem ser criado ou carregado.

    Este é o coração do jogo em execução. Ele continuará em loop enquanto o jogador
    estiver vivo e não tiver escolhido sair para o menu principal.

    Args:
        estado_jogo ("EstadoJogo"): O objeto de estado do jogo, contendo o personagem e
                                    outros dados relevantes.
    """
    geral.limpar_tela()
    narrador.narrar(f"A aventura de {estado_jogo.personagem.nome} começa! ⚔️", estilo="epico", pausa_depois=1)

    continuar_jogo = True
    while continuar_jogo:
        # ETAPA 1: Delega a renderização e a entrada para a interface de exploração.
        # A tela agora retorna uma ação estruturada.
        if INTERFACE_ATUAL == 'terminal':
            acao = tela_exploracao.exibir_exploracao(estado_jogo.personagem)
        else:
            narrador.narrar("Aguardando evento da interface gráfica...", estilo="debug")
            time.sleep(2)
            acao = {"tipo": "esperar"}

        # ETAPA 2: Processa a ação estruturada recebida.
        geral.limpar_tela()
        narrador.narrar(f"Ação recebida: {acao}", estilo="debug")

        tipo_acao = acao.get("tipo")

        if tipo_acao == "mover":
            destino = acao.get("destino", "lugar nenhum")
            narrador.narrar(f"Viajando para {destino}...", pausa_depois=1)
            estado_jogo.personagem.localizacao_atual = destino

            # Lógica de Encontro / Transição de Tela
            dados_nova_area = INDICE_AREAS["by_id"].get(destino)
            if not dados_nova_area:
                narrador.narrar(f"Erro: Área '{destino}' não existe.", estilo="erro", pausa_depois=1)
            # Se for uma dungeon ou área selvagem com monstros
            elif dados_nova_area.get("monstros"):
                narrador.narrar(f"Você adentra {dados_nova_area['nome']}...", estilo="sombrio", pausa_depois=1)
                # Chance de 40% de encontrar um monstro
                if random.random() < 0.40:
                    id_monstro = random.choice(dados_nova_area["monstros"])
                    dados_monstro = INDICE_MONSTROS["by_id"].get(id_monstro)
                    if dados_monstro:
                        narrador.narrar(f"Um(a) {dados_monstro['nome']} selvagem aparece!", estilo="perigo", pausa_depois=1)
                        monstro = Monstro(dados_monstro)
                        tela_combate.exibir_combate(estado_jogo.personagem, [monstro])
                        # Após o combate, o loop principal continua
                    else:
                        narrador.narrar(f"DEBUG: Monstro ID '{id_monstro}' não encontrado no índice.", estilo="erro")
            # Se for uma cidade (placeholder para a tela de cidade)
            elif dados_nova_area.get("bioma") == "Cidade":
                 narrador.narrar(f"Bem-vindo a {dados_nova_area['nome']}!", estilo="epico", pausa_depois=1)
                 # tela_cidade.exibir_cidade(estado_jogo) # Chamada futura
                 geral.pausar_tela("Pressione ENTER para explorar a cidade (não implementado)...")

        elif tipo_acao == "abrir_tela":
            tela = acao.get("tela")
            if tela == "personagem":
                tela_personagem.exibir_tela_personagem(estado_jogo.personagem)
            elif tela == "inventario":
                tela_inventario.exibir_inventario(estado_jogo.personagem)
            else:
                narrador.narrar(f"Tela desconhecida: {tela}", estilo="erro", pausa_depois=1)

        elif tipo_acao == "sair":
            narrador.narrar("Você decide encerrar sua jornada por enquanto.", pausa_depois=1)
            # A lógica de salvar antes de sair seria adicionada aqui.
            narrador.narrar("Retornando ao menu principal...", estilo="sistema")
            time.sleep(2)
            continuar_jogo = False

        elif tipo_acao == "erro":
            narrador.narrar(f"Ocorreu um erro: {acao.get('mensagem')}", estilo="erro", pausa_depois=2)
            continuar_jogo = False # Encerra em caso de erro grave

        else:
            narrador.narrar(f"Ação desconhecida: {tipo_acao}", estilo="erro")
            time.sleep(1.5)

        # ETAPA 3: Verifica as condições de fim de jogo após cada ação.
        if not estado_jogo.personagem.esta_vivo():
            continuar_jogo = False
            narrador.narrar("Você morreu! [morte]", estilo="sombrio", limpar=True, pausa_depois=2)
            # A lógica de pós-morte agora pode ser chamada a partir do loop principal em main()
            # loop_pos_morte() # Desativado para um fluxo mais limpo

    narrador.narrar("Sessão de jogo encerrada.", estilo="sistema", limpar=True)
    time.sleep(2)

# ==============================================================================================
# 5. PONTO DE ENTRADA (MAIN)
# ==============================================================================================
# A seção a seguir é o ponto de partida de todo o programa.

def main() -> None:
    """
    O ponto de entrada principal e função orquestradora do programa.
    """
    try:
        print(f"Bem-vindo a {NOME_DO_JOGO} v{VERSAO_DO_JOGO}!")
        print("Inicializando sistemas...")

        if not os.path.exists(CAMINHO_SAVES):
            print(f"Pasta de saves não encontrada. Criando em: {CAMINHO_SAVES}")
            os.makedirs(CAMINHO_SAVES)

        if INTERFACE_ATUAL == 'terminal':
            print("Interface de terminal selecionada.")

            # O loop principal da aplicação agora vive aqui.
            while True:
                menu = tela_menu_principal.MenuPrincipalTela()
                resultado_menu = menu.exibir()

                if resultado_menu == "sair":
                    break

                elif hasattr(resultado_menu, 'personagem'):
                    loop_de_jogo(resultado_menu)

                else:
                    print("Retornando ao menu principal devido a um estado inesperado.", file=sys.stderr)

        elif INTERFACE_ATUAL == 'grafica':
            print("Interface gráfica selecionada.")
            app = MainWindow()
            app.start()

        else:
            raise ValueError(f"Interface desconhecida: '{INTERFACE_ATUAL}'. Verifique a constante INTERFACE_ATUAL.")

    except KeyboardInterrupt:
        print("\nSaindo do jogo a pedido do usuário. Adeus!")
        sys.exit(0)
    except Exception as e:
        print(f"\nERRO INESPERADO: {e}", file=sys.stderr)
        # logging.exception("Ocorreu um erro fatal:")
        sys.exit(1)


if __name__ == "__main__":
    # Este bloco padrão do Python garante que a função main() seja chamada
    # apenas quando o script é executado diretamente.
    main()
