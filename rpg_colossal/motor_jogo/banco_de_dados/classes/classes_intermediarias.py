# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: CLASSES INTERMEDIÁRIAS
================================================================================================
"""
from typing import List, Dict

CLASSES_INTERMEDIARIAS: List[Dict] = [
    # --- Evoluções de Guerreiro ---
    {"id_classe": "guardiao", "nome": "Guardião", "requisitos": {"classe_base": "guerreiro", "nivel_minimo": 10}, "descricao_curta": "Mestre da defesa, um protetor inabalável."},
    {"id_classe": "berserker", "nome": "Berserker", "requisitos": {"classe_base": "guerreiro", "nivel_minimo": 10}, "descricao_curta": "Canaliza a fúria para uma ofensiva brutal."},

    # --- Evoluções de Bárbaro ---
    {"id_classe": "frenetico", "nome": "Frenético", "requisitos": {"classe_base": "barbaro", "nivel_minimo": 10}, "descricao_curta": "Um combatente que ataca com velocidade e selvageria puras."},
    {"id_classe": "totemico", "nome": "Guerreiro Totêmico", "requisitos": {"classe_base": "barbaro", "nivel_minimo": 10}, "descricao_curta": "Invoca o poder de espíritos animais para ganhar suas forças."},

    # --- Evoluções de Monge ---
    {"id_classe": "mao_aberta", "nome": "Caminho da Mão Aberta", "requisitos": {"classe_base": "monge", "nivel_minimo": 10}, "descricao_curta": "Usa técnicas que manipulam o chi para controlar e debilitar inimigos."},
    {"id_classe": "sombra", "nome": "Caminho da Sombra", "requisitos": {"classe_base": "monge", "nivel_minimo": 10}, "descricao_curta": "Mestre da furtividade e do teletransporte, atacando das sombras."},

    # --- Evoluções de Ladino ---
    {"id_classe": "assassino", "nome": "Assassino", "requisitos": {"classe_base": "ladino", "nivel_minimo": 10}, "descricao_curta": "Especialista em causar dano massivo em um único golpe mortal."},
    {"id_classe": "trapaceiro", "nome": "Trapaceiro", "requisitos": {"classe_base": "ladino", "nivel_minimo": 10}, "descricao_curta": "Usa magia de ilusão e encanto para confundir e manipular."},

    # --- Evoluções de Bardo ---
    {"id_classe": "colegio_do_conhecimento", "nome": "Colégio do Conhecimento", "requisitos": {"classe_base": "bardo", "nivel_minimo": 10}, "descricao_curta": "Um erudito que usa seu vasto conhecimento para debilitar inimigos e ajudar aliados."},
    {"id_classe": "colegio_da_valentia", "nome": "Colégio da Valentia", "requisitos": {"classe_base": "bardo", "nivel_minimo": 10}, "descricao_curta": "Um bardo marcial que inspira coragem no campo de batalha e luta ao lado de guerreiros."},

    # --- Evoluções de Mago ---
    {"id_classe": "piromante", "nome": "Piromante", "requisitos": {"classe_base": "mago", "nivel_minimo": 10}, "descricao_curta": "Especialista no poder destrutivo do fogo."},
    {"id_classe": "criomante", "nome": "Criomante", "requisitos": {"classe_base": "mago", "nivel_minimo": 10}, "descricao_curta": "Mestre do gelo, focado em controle e dano de frio."},

    # --- Evoluções de Feiticeiro ---
    {"id_classe": "linhagem_draconica", "nome": "Linhagem Dracônica", "requisitos": {"classe_base": "feiticeiro", "nivel_minimo": 10}, "descricao_curta": "Desperta o poder dos dragões em seu sangue, ganhando escamas e poder elemental."},
    {"id_classe": "magia_selvagem", "nome": "Magia Selvagem", "requisitos": {"classe_base": "feiticeiro", "nivel_minimo": 10}, "descricao_curta": "Canaliza o caos da magia pura, com resultados imprevisíveis e poderosos."},

    # --- Evoluções de Bruxo ---
    {"id_classe": "pacto_da_lamina", "nome": "Pacto da Lâmina", "requisitos": {"classe_base": "bruxo", "nivel_minimo": 10}, "descricao_curta": "Seu patrono lhe concede uma arma mágica, permitindo lutar corpo a corpo."},
    {"id_classe": "pacto_do_tomo", "nome": "Pacto do Tomo", "requisitos": {"classe_base": "bruxo", "nivel_minimo": 10}, "descricao_curta": "Recebe um grimório que lhe concede magias adicionais de qualquer escola."},

    # --- Evoluções de Clérigo ---
    {"id_classe": "sacerdote", "nome": "Sacerdote", "requisitos": {"classe_base": "clerigo", "nivel_minimo": 10}, "descricao_curta": "Focado no poder da cura e da proteção divina para seus aliados."},
    {"id_classe": "inquisidor", "nome": "Inquisidor", "requisitos": {"classe_base": "clerigo", "nivel_minimo": 10}, "descricao_curta": "Um caçador de hereges e monstros que usa poder divino para o ataque."},

    # --- Evoluções de Druida ---
    {"id_classe": "circulo_da_lua", "nome": "Círculo da Lua", "requisitos": {"classe_base": "druida", "nivel_minimo": 10}, "descricao_curta": "Mestre da transformação, capaz de assumir formas de feras de combate mais poderosas."},
    {"id_classe": "circulo_da_terra", "nome": "Círculo da Terra", "requisitos": {"classe_base": "druida", "nivel_minimo": 10}, "descricao_curta": "Conjurador que extrai poder do próprio terreno, com magias que variam com o bioma."},

    # --- Evoluções de Paladino ---
    {"id_classe": "juramento_da_devocao", "nome": "Juramento da Devoção", "requisitos": {"classe_base": "paladino", "nivel_minimo": 10}, "descricao_curta": "O arquétipo do cavaleiro de armadura brilhante, um bastião da honra e da justiça."},
    {"id_classe": "juramento_da_vinganca", "nome": "Juramento da Vingança", "requisitos": {"classe_base": "paladino", "nivel_minimo": 10}, "descricao_curta": "Um caçador implacável do mal, que usa quaisquer meios para punir os culpados."}
]

INDICE_CLASSES_INTERMEDIARIAS = {"by_id": {c["id_classe"]: c for c in CLASSES_INTERMEDIARIAS}}
