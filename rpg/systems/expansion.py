from random import Random


def regioes_base() -> dict[str, dict]:
    return {
        "vila_aurora": {"custo_energia": 0, "risco": 0, "recompensa_base": 0},
        "fronteira_norte": {"custo_energia": 2, "risco": 1, "recompensa_base": 8},
        "ruinas_antigas": {"custo_energia": 3, "risco": 2, "recompensa_base": 14},
    }


def viajar_para_regiao(regiao_atual: str, destino: str, energia: int) -> dict:
    regioes = regioes_base()
    if destino not in regioes:
        return {"ok": False, "motivo": "destino_invalido", "regiao": regiao_atual, "energia": energia}

    custo = regioes[destino]["custo_energia"]
    if energia < custo:
        return {"ok": False, "motivo": "energia_insuficiente", "regiao": regiao_atual, "energia": energia}

    return {
        "ok": True,
        "regiao": destino,
        "energia": energia - custo,
        "custo": custo,
        "risco": regioes[destino]["risco"],
    }


def gerar_dungeon(dia: int, regiao: str) -> dict:
    cfg = regioes_base().get(regiao, {"risco": 1, "recompensa_base": 10})
    rng = Random(f"{dia}:{regiao}")
    salas = rng.randint(3 + cfg["risco"], 6 + cfg["risco"])
    dificuldade = max(1, salas - 2)
    return {
        "id": f"dg_{regiao}_{dia}",
        "regiao": regiao,
        "salas": salas,
        "dificuldade": dificuldade,
        "recompensa_base": cfg["recompensa_base"],
        "concluida": False,
    }


def explorar_dungeon(hp_atual: int, dungeon: dict) -> dict:
    dificuldade = max(1, dungeon.get("dificuldade", 1))
    salas = max(1, dungeon.get("salas", 3))
    perda_hp = min(max(0, hp_atual - 1), dificuldade * 3 + salas // 2) if hp_atual > 1 else 0
    xp = 20 + salas * 5 + dificuldade * 3
    ouro = dungeon.get("recompensa_base", 10) + dificuldade * 4
    return {"hp_final": max(1, hp_atual - perda_hp), "xp": xp, "ouro": ouro, "concluida": True}


def simular_agenda_faccoes(reputacoes: dict[str, int], dia: int) -> list[str]:
    eventos: list[str] = []
    for fid in sorted(reputacoes.keys()):
        variacao = 1 if (dia + len(fid)) % 2 == 0 else -1
        reputacoes[fid] = reputacoes.get(fid, 0) + variacao
        eventos.append(f"{fid}:{'subiu' if variacao > 0 else 'caiu'}")
    return eventos


def iniciar_arco_longo(titulo: str) -> dict:
    return {"titulo": titulo, "ato": 1, "max_atos": 3, "concluido": False, "recompensa_final_ouro": 60}


def avancar_arco_longo(arco: dict) -> dict:
    if arco.get("concluido"):
        return arco
    arco["ato"] += 1
    if arco["ato"] >= arco.get("max_atos", 3):
        arco["concluido"] = True
        arco["ato"] = arco.get("max_atos", 3)
    return arco


def gerar_pacote_expansao(prefixo: str, quantidade: int = 5) -> dict[str, list[str]]:
    qtd = max(1, quantidade)
    pacote = {
        "itens": [f"{prefixo}_item_{i}" for i in range(1, qtd + 1)],
        "monstros": [f"{prefixo}_monstro_{i}" for i in range(1, qtd + 1)],
        "contratos": [f"{prefixo}_contrato_{i}" for i in range(1, qtd + 1)],
    }
    # defesa simples de qualidade de pacote
    for ids in pacote.values():
        if len(ids) != len(set(ids)):
            raise ValueError("Pacote com IDs duplicados")
    return pacote


def simular_balance_headless(rodadas: int = 20, seed: int = 42) -> dict:
    rodadas = max(1, rodadas)
    rng = Random(seed)
    vitorias = 0
    hp_final_total = 0

    for _ in range(rodadas):
        poder = rng.randint(7, 15)
        ameaca = rng.randint(6, 15)
        venceu = poder >= ameaca
        if venceu:
            vitorias += 1
            hp_final_total += rng.randint(35, 90)
        else:
            hp_final_total += rng.randint(1, 30)

    derrotas = rodadas - vitorias
    return {
        "rodadas": rodadas,
        "vitorias": vitorias,
        "derrotas": derrotas,
        "taxa_vitoria": round(vitorias / rodadas, 3),
        "hp_final_medio": round(hp_final_total / rodadas, 2),
    }



def validar_estado_expansao(state: dict) -> dict:
    """Validação leve de consistência para estados das fases 21-25."""
    erros: list[str] = []

    energia = state.get("energia_viagem", 0)
    if energia < 0 or energia > 10:
        erros.append("energia_viagem_fora_intervalo")

    regiao = state.get("regiao_atual", "vila_aurora")
    if regiao not in regioes_base():
        erros.append("regiao_atual_invalida")

    descobertas = state.get("regioes_descobertas", set())
    if isinstance(descobertas, list):
        descobertas = set(descobertas)
    if "vila_aurora" not in descobertas:
        erros.append("regiao_inicial_nao_descoberta")

    dungeon = state.get("dungeon_ativa")
    if dungeon is not None:
        if dungeon.get("regiao") not in regioes_base():
            erros.append("dungeon_regiao_invalida")
        if dungeon.get("salas", 0) <= 0:
            erros.append("dungeon_salas_invalidas")

    arco = state.get("arco_longo")
    if arco is not None:
        ato = arco.get("ato", 1)
        max_atos = arco.get("max_atos", 3)
        if ato < 1 or ato > max_atos:
            erros.append("arco_ato_invalido")

    return {"ok": not erros, "erros": erros}
