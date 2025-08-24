# ==============================================================================
# ARQUIVO DE DADOS: HABILIDADES DE SUPORTE
# ==============================================================================
#
# Este arquivo contém as definições para habilidades de suporte, como curas,
# buffs, debuffs e outras utilidades.
#
# ==============================================================================

HABILIDADES_SUPORTE = {
    # Exemplo de habilidade de cura
    "cura_leve": {
        "nome": "Cura Leve",
        "custo_tipo": "mp",
        "custo_valor": 10,
        "descricao": "Cura uma pequena quantidade de ferimentos em um alvo.",
        "tipo_alvo": "aliado_unico",
        "efeitos": [
            {"tipo": "cura", "escala_com": "sabedoria", "multiplicador_cura": 1.5}
        ]
    },
    # Exemplo de buff
    "grito_de_guerra": {
        "nome": "Grito de Guerra",
        "custo_tipo": "stamina",
        "custo_valor": 15,
        "descricao": "Um grito poderoso que aumenta o ataque do grupo.",
        "tipo_alvo": "aliados_area",
        "efeitos": [
            {"tipo": "aplicar_efeito", "id_efeito": "buff_ataque_pequeno", "duracao": 3}
        ]
    }
}
