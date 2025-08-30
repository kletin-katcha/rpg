# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: HABILIDADES DE SUPORTE
================================================================================================
Este arquivo define as habilidades de Suporte, focadas em curas, buffs para aliados
e debuffs para inimigos. São o pilar da classe Clérigo.
"""
from typing import List, Dict

HABILIDADES_SUPORTE: List[Dict] = [
    # --- ÁRVORE DE HABILIDADES: CLÉRIGO (Níveis 1-20) ---
    {
        "id": "clerigo_cura_leve",
        "nome": "Cura Leve",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 1},
        "custo": {"mana": 10},
        "multiplicador": 1.5, "atributo_chave": "sabedoria",
        "efeitos": [{"tipo": "cura", "valor": "1d8+2"}],
        "descricao": "Uma prece que canaliza energia divina para curar ferimentos leves de um aliado."
    },
    {
        "id": "clerigo_protecao_divina",
        "nome": "Proteção Divina",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 2},
        "custo": {"mana": 10},
        "efeitos": [{"tipo": "buff", "atributo": "defesa_fisica", "valor": 5, "duracao": 3}],
        "descricao": "Abençoa um aliado, aumentando sua defesa física por um curto período."
    },
    {
        "id": "clerigo_golpe_sagrado",
        "nome": "Golpe Sagrado",
        "tipo": "ativa", "categoria": "magico", "requisitos": {"nivel": 3},
        "custo": {"mana": 8},
        "multiplicador": 1.2, "atributo_chave": "sabedoria", "precisao": 0.95, "tipo_dano": "divino",
        "descricao": "Infunde a arma com poder divino, causando dano sagrado no próximo ataque."
    },
    {
        "id": "clerigo_afastar_mortos_vivos",
        "nome": "Afastar Mortos-Vivos",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 5},
        "custo": {"mana": 20}, "area_de_efeito": "todos_inimigos_mortos_vivos",
        "efeitos": [{"tipo": "medo", "duracao": 2, "chance": 0.8}],
        "descricao": "Canaliza energia divina positiva que aterroriza mortos-vivos, fazendo-os recuar."
    },
    {
        "id": "clerigo_oracao_da_fortitude",
        "nome": "Oração da Fortitude",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 8},
        "custo": {"mana": 30}, "area_de_efeito": "todos_aliados",
        "efeitos": [{"tipo": "buff", "atributo": "hp_max", "valor_percentual": 0.15, "duracao": 5}],
        "descricao": "Uma oração em grupo que aumenta a vida máxima de todos os aliados por um período."
    },
    {
        "id": "clerigo_remover_maldicao",
        "nome": "Remover Maldição",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 12},
        "custo": {"mana": 25},
        "efeitos": [{"tipo": "remover_debuff_tipo", "tipo_debuff": "maldicao"}],
        "descricao": "Pede a intervenção divina para remover maldições e outros efeitos mágicos negativos de um aliado."
    },
    {
        "id": "clerigo_aura_sagrada",
        "nome": "Aura Sagrada",
        "tipo": "passiva", "categoria": "suporte", "requisitos": {"nivel": 15},
        "efeitos": [{"tipo": "cura_por_turno_area", "valor": "1d4", "alvos": "aliados"}],
        "descricao": "Uma aura de fé constantemente emana do clérigo, curando levemente os aliados próximos a cada turno."
    },
    {
        "id": "clerigo_ressurreicao",
        "nome": "Ressurreição",
        "tipo": "ativa", "categoria": "suporte", "requisitos": {"nivel": 20},
        "custo": {"mana": 100}, "cooldown": 10,
        "efeitos": [{"tipo": "reviver", "hp_restaurado_percentual": 0.5}],
        "descricao": "Um milagre poderoso que traz um aliado caído de volta à vida com metade de seus pontos de vida."
    }
]

# Construção do índice para acesso rápido
GRIMORIO_SUPORTE = {"by_id": {h["id"]: h for h in HABILIDADES_SUPORTE}}
