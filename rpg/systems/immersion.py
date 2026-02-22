from rpg.content.loader import load_catalog


CLIMAS = ["ensolarado", "chuvoso", "neblina", "tempestade_arcana"]


def periodo_do_dia(hora: int) -> str:
    h = hora % 24
    if 6 <= h < 12:
        return "manha"
    if 12 <= h < 18:
        return "tarde"
    if 18 <= h < 22:
        return "noite"
    return "madrugada"


def avancar_tempo(hora_atual: int, passo: int = 6) -> int:
    return (hora_atual + passo) % 24


def atualizar_clima(dia: int) -> str:
    return CLIMAS[dia % len(CLIMAS)]


def registrar_jornal(jornal: list[str], texto: str, limite: int = 20) -> list[str]:
    jornal.append(texto)
    if len(jornal) > limite:
        del jornal[:-limite]
    return jornal


def desbloquear_lore(codex: set[str], entrada_id: str) -> set[str]:
    codex.add(entrada_id)
    return codex


def codex_base() -> set[str]:
    faccoes = load_catalog("faccoes")
    return {f"faccao:{fid}" for fid in faccoes.keys()}
