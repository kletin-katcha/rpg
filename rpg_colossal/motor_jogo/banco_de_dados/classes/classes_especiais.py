# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: CLASSES ESPECIAIS, SECRETAS E DE PRESTÍGIO
================================================================================================
"""
from typing import List, Dict

CLASSES_ESPECIAIS: List[Dict] = [
    {
        "id_classe": "lamina_sombria", "nome": "Lâmina Sombria",
        "descricao_curta": "Um assassino que fez um pacto com as sombras para poder.",
        "lore": "Ao encontrar um 'Fragmento do Vazio', o assassino pode oferecer parte de sua alma em troca do domínio sobre as trevas.",
        "requisitos": {
            "nivel_minimo": 20, "classe_base": "assassino",
            "item_possui": "fragmento_do_vazio",
            "evento_mundo": "noite_sem_estrelas"
        }
    },
    {
        "id_classe": "lich", "nome": "Lich",
        "descricao_curta": "Um mago que sacrificou sua alma pela imortalidade e poder necrótico.",
        "lore": "Através de um ritual profano e a criação de uma filactéria, um mestre da necromancia pode transcender a morte, tornando-se um Lich imortal.",
        "requisitos": {
            "nivel_minimo": 25, "classe_base": "necromante",
            "missao_concluida": "o_ritual_da_imortalidade",
            "alinhamento": ["Neutro e Mau", "Caótico e Mau"]
        }
    },
    {
        "id_classe": "avatar_da_natureza", "nome": "Avatar da Natureza",
        "descricao_curta": "Um druida que se fundiu com um espírito primordial da floresta.",
        "lore": "No coração de uma floresta ancestral, um druida de poder imenso pode se fundir com o espírito guardião, tornando-se a vontade viva da própria natureza.",
        "requisitos": {
            "nivel_minimo": 25, "classe_base": "circulo_da_terra",
            "missao_concluida": "o_despertar_do_espirito_ancestral",
            "reputacao_minima": {"circulo_dos_druidas": "Exaltado"}
        }
    },
    {
        "id_classe": "campeao_divino", "nome": "Campeão Divino",
        "descricao_curta": "O escolhido mortal de uma divindade, imbuído com seu poder direto.",
        "lore": "Em tempos de grande crise, uma divindade pode escolher um mortal para ser seu avatar no mundo, concedendo-lhe uma fração de seu poder.",
        "requisitos": {
            "nivel_minimo": 25, "classe_base": "vingador_sagrado",
            "evento_mundo": "a_guerra_celestial",
            "escolha_narrativa": "aceitar_o_dom_da_divindade"
        }
    },
    {
        "id_classe": "viajante_do_tempo", "nome": "Viajante do Tempo",
        "descricao_curta": "Um mago que desvendou os segredos do fluxo temporal.",
        "lore": "Após estudar os Manuscritos de Chronos, um arquimago pode aprender a dobrar o tempo, acelerando a si mesmo ou paralisando seus inimigos.",
        "requisitos": {
            "nivel_minimo": 30, "classe_base": "arquimago",
            "missao_concluida": "os_manuscritos_de_chronos"
        }
    },
    {
        "id_classe": "lorde_da_guerra", "nome": "Lorde da Guerra",
        "descricao_curta": "Um comandante cuja presença no campo de batalha inspira exércitos.",
        "lore": "Um Mestre das Armas que prova sua proeza tática liderando uma facção à vitória em uma grande batalha pode ascender a este título.",
        "requisitos": {
            "nivel_minimo": 30, "classe_base": "mestre_das_armas",
            "conquista": "vitoria_em_batalha_cerco"
        }
    }
]

INDICE_CLASSES_ESPECIAIS = {"by_id": {c["id_classe"]: c for c in CLASSES_ESPECIAIS}}
