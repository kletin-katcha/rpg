# -*- coding: utf-8 -*-
"""
################################################################################################
##                                                                                            ##
##    ██████╗  ██████╗ ███████╗███████╗    ██████╗ ███████╗██╗    ██████╗ ███████╗███╗   ███╗    ##
##    ██╔══██╗██╔═══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██║    ██╔══██╗██╔════╝████╗ ████║    ##
##    ██████╔╝██║   ██║███████╗███████╗    ██████╔╝█████╗  ██║    ██║  ██║█████╗  ██╔████╔██║    ##
##    ██╔══██╗██║   ██║╚════██║╚════██║    ██╔══██╗██╔══╝  ██║    ██║  ██║██╔══╝  ██║╚██╔╝██║    ##
##    ██║  ██║╚██████╔╝███████║███████║    ██║  ██║███████╗███████╗██████╔╝███████╗██║ ╚═╝ ██║    ##
##    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝    ##
##                                                                                            ##
################################################################################################
################################################################################################

================================================================================================
BANCO DE DADOS: BOSS FINAL - O REI DOS DEMÔNIOS
================================================================================================
Este arquivo contém a definição completa do chefe final do jogo, Malakor, o Rei dos
Demônios. Esta não é uma criatura comum; a luta é um evento de múltiplas fases,
com mecânicas únicas que exigem mais do que apenas força bruta para serem superadas.

---------------------------------
-- ESTRUTURA DE DADOS DO BOSS --
---------------------------------
A estrutura para um boss de múltiplas fases é mais complexa:

- `id` (str): Identificador único.
- `nome` (str): Nome do boss.
- `descricao` (str): Lore e descrição do confronto.
- `fases` (list): Uma lista de dicionários, onde cada dicionário representa uma fase.
  - `fase_id` (int): O número da fase (1, 2, 3...).
  - `hp` (int): Pontos de vida desta fase.
  - `limiar_hp` (float): A porcentagem de HP em que a transição para a próxima
                         fase ocorre (ex: 0.5 para 50%).
  - `habilidades` (list): Lista de `id` de habilidades usadas nesta fase.
  - `mecanicas_especiais` (list): Descrição das mecânicas únicas da fase.
  - `dialogos` (dict): Diálogos que o boss pode proferir em gatilhos específicos.
    - `inicio_fase`: Fala ao entrar na fase.
    - `meia_vida`: Fala ao atingir 50% de vida na fase.
    - `evento_especial`: Fala ao usar uma habilidade específica.
- `loot_final` (list): A recompensa pela derrota do boss.

---------------------------------
-- DESIGN DA LUTA: REI DOS DEMÔNIOS --
---------------------------------
A luta contra Malakor foi projetada para ser um teste de tudo o que o jogador aprendeu.

- **Fase 1: O Lorde Arrogante:** Malakor subestima o jogador, usando ataques poderosos,
  mas previsíveis. O objetivo é sobreviver ao seu dano e provar seu valor.

- **Fase 2: O Despertar do Poder:** Ao ser ferido, Malakor fica sério. Ele invoca
  ajudantes demoníacos e usa debuffs para enfraquecer o grupo. O foco muda de
  dano puro para controle de grupo e gerenciamento de debuffs.

- **Fase 3: A Forma do Caos:** Em desespero, Malakor libera seu poder total,
  tornando-se imune a dano convencional. Seu HP se torna astronômico. A única
  maneira de derrotá-lo é usar um item de missão especial (a "Lâmina da Alma Pura")
  para destruir os "Cristais do Caos" que o sustentam. Destruir os cristais
  causa dano massivo e direto a Malakor, ignorando sua imunidade.
"""

# ==============================================================================================
# == DEFINIÇÃO DO BOSS FINAL ===================================================================
# ==============================================================================================
BOSS_REI_DOS_DEMONIOS = {
    "id": "boss_malakor_rei_dos_demonios",
    "nome": "Malakor, o Rei dos Demônios",
    "descricao": "Uma entidade de pura malícia e poder caótico, aprisionada eras atrás e agora liberta para consumir Aetheria. Sua forma é uma amálgama de sombras, fogo infernal e desespero.",
    "fases": [
        # FASE 1
        {
            "fase_id": 1,
            "hp": 5000,
            "limiar_hp": 0.6, # Transição para a fase 2 aos 60% de HP
            "habilidades": ["sk_boss_malakor_garra_do_abismo", "sk_boss_malakor_fogo_infernal"],
            "mecanicas_especiais": ["Nenhuma nesta fase."],
            "dialogos": {
                "inicio_fase": "Mortal tolo... Ousa desafiar o soberano do Caos? Sua alma será a primeira que devorarei.",
                "meia_vida": "Sua resistência é... inesperada. Mas não passa de um inseto se debatendo!",
            }
        },
        # FASE 2
        {
            "fase_id": 2,
            "hp": 7500,
            "limiar_hp": 0.2, # Transição para a fase 3 aos 20% de HP
            "habilidades": ["sk_boss_malakor_invocar_diabretes", "sk_boss_malakor_maldicao_da_fraqueza"],
            "mecanicas_especiais": [
                "Invocar Diabretes: A cada 4 turnos, Malakor invoca 2 Diabretes Infernais para ajudar em combate.",
                "Aura de Pavor: Todos os jogadores recebem um debuff de precisão enquanto Malakor estiver acima de 50% de HP nesta fase."
            ],
            "dialogos": {
                "inicio_fase": "Chega de brincadeiras! Sinta o verdadeiro poder do Abismo!",
                "evento_especial": {
                    "gatilho": "sk_boss_malakor_invocar_diabretes",
                    "fala": "Ergam-se, meus servos! Consumam a luz deste verme!"
                }
            }
        },
        # FASE 3
        {
            "fase_id": 3,
            "hp": (7500 * 0.2) ** 3, # HP Astronômico, como solicitado
            "limiar_hp": 0.0,
            "habilidades": ["sk_boss_malakor_aniquilacao_caotica", "sk_boss_malakor_barreira_impenetravel"],
            "mecanicas_especiais": [
                "Barreira Impenetrável: Malakor fica imune a todo dano direto.",
                "Cristais do Caos: Três 'Cristais do Caos' aparecem no campo de batalha. Eles são os alvos reais.",
                "Vulnerabilidade: Destruir um Cristal do Caos causa 33% da vida máxima de Malakor como dano direto, ignorando sua barreira."
            ],
            "dialogos": {
                "inicio_fase": "NÃO! EU NÃO SEREI DERROTADO! TESTEMUNHEM MINHA VERDADEIRA FORMA! AETHERIA VAI QUEIMAR!",
                "evento_especial": {
                    "gatilho": "destruir_cristal_caos",
                    "fala": "ARGH! A LUZ... ELA QUEIMA! VOCÊ PAGARÁ POR ISSO!"
                },
                "morte": "Impossível... A escuridão... não pode... se apagar..."
            }
        }
    ],
    "loot_final": ["item_coroa_do_rei_demonio", "item_essencia_do_caos"]
}

# Em um arquivo real, a lista conteria todos os bosses, mas como este é dedicado,
# exportamos diretamente o dicionário.
BOSSES = [BOSS_REI_DOS_DEMONIOS]
INDICE_BOSSES = {"by_id": {boss["id"]: boss for boss in BOSSES}}
