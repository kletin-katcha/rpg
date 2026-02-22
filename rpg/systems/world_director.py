from rpg.systems.immersion import periodo_do_dia


MUTADORES = [
    "escassez_metal",
    "bencao_mercantil",
    "noite_sem_fim",
    "caos_arcano",
]


def iniciar_memoria_faccoes(reputacoes: dict[str, int]) -> dict[str, list[str]]:
    return {fid: [] for fid in reputacoes}


def gerar_arco_mundo(reputacoes: dict[str, int], clima: str, hora: int) -> dict:
    faccao_foco = max(reputacoes, key=reputacoes.get)
    periodo = periodo_do_dia(hora)
    tensao = "alta" if reputacoes.get(faccao_foco, 0) < 5 else "estavel"
    titulo = f"Arco de {faccao_foco} em clima {clima}"
    descricao = f"A facção {faccao_foco} move peças na {periodo}. Tensão {tensao}."
    return {"titulo": titulo, "descricao": descricao, "faccao_foco": faccao_foco, "tensao": tensao}


def escolher_mutador(dia_economico: int) -> str:
    return MUTADORES[dia_economico % len(MUTADORES)]


def aplicar_mutador_mercado(mercado: dict[str, float], mutador: str) -> dict[str, float]:
    if mutador == "escassez_metal":
        for item in ("sucata_metal", "barra_metal", "liga_metal"):
            if item in mercado:
                mercado[item] = round(mercado[item] * 1.2, 2)
    elif mutador == "bencao_mercantil":
        for item in list(mercado.keys()):
            mercado[item] = round(mercado[item] * 1.05, 2)
    return mercado


def registrar_memoria(memoria_faccoes: dict[str, list[str]], faccao_id: str, evento: str, limite: int = 10) -> None:
    memoria_faccoes.setdefault(faccao_id, []).append(evento)
    if len(memoria_faccoes[faccao_id]) > limite:
        del memoria_faccoes[faccao_id][:-limite]
