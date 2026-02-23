from ...dados.cidade.construcoes import PROJETOS_CONSTRUCAO


def _tem_materiais(jogador, materiais: dict[str, int]) -> bool:
    for id_item, quantidade in materiais.items():
        if jogador.inventario.get(id_item, {}).get("quantidade", 0) < quantidade:
            return False
    return True


def _consumir_materiais(jogador, materiais: dict[str, int]):
    for id_item, quantidade in materiais.items():
        jogador.remover_item(id_item, quantidade)


def construir_estrutura(jogador, id_projeto: str):
    estruturas = getattr(jogador, "estruturas_construidas", set())

    if id_projeto in estruturas:
        return {"tipo": "feedback", "log": ["Essa estrutura já foi construída."]}

    projeto = PROJETOS_CONSTRUCAO.get(id_projeto)
    if not projeto:
        return {"tipo": "feedback", "log": ["Projeto de construção desconhecido."]}

    requisito = projeto.get("requisito_estrutura")
    if requisito and requisito not in estruturas:
        return {"tipo": "feedback", "log": [f"Você precisa construir '{requisito}' antes."]}

    if jogador.ouro < projeto["custo_ouro"]:
        return {"tipo": "feedback", "log": ["Ouro insuficiente para esta construção."]}

    if not _tem_materiais(jogador, projeto.get("materiais", {})):
        return {"tipo": "feedback", "log": ["Materiais insuficientes para esta construção."]}

    jogador.ouro -= projeto["custo_ouro"]
    _consumir_materiais(jogador, projeto.get("materiais", {}))
    estruturas.add(id_projeto)
    jogador.estruturas_construidas = estruturas
    if id_projeto not in jogador.niveis_estruturas:
        jogador.niveis_estruturas[id_projeto] = 1

    return {"tipo": "feedback", "log": [f"Construção concluída: {projeto['nome']}"]}
