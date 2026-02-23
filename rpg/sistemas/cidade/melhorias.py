from ...dados.cidade.melhorias import MELHORIAS_ESTRUTURAS


def _tem_materiais(jogador, materiais: dict[str, int]) -> bool:
    for id_item, quantidade in materiais.items():
        if jogador.inventario.get(id_item, {}).get("quantidade", 0) < quantidade:
            return False
    return True


def _consumir_materiais(jogador, materiais: dict[str, int]):
    for id_item, quantidade in materiais.items():
        jogador.remover_item(id_item, quantidade)


def melhorar_estrutura(jogador, id_estrutura: str):
    if id_estrutura not in jogador.estruturas_construidas:
        return {"tipo": "feedback", "log": ["Você precisa construir essa estrutura antes de melhorá-la."]}

    dados = MELHORIAS_ESTRUTURAS.get(id_estrutura)
    if not dados:
        return {"tipo": "feedback", "log": ["Essa estrutura não possui melhorias cadastradas."]}

    nivel_atual = jogador.niveis_estruturas.get(id_estrutura, 1)
    nivel_alvo = nivel_atual + 1

    if nivel_atual >= dados["nivel_maximo"]:
        return {"tipo": "feedback", "log": ["Estrutura já está no nível máximo."]}

    custo = dados["custos_por_nivel"].get(nivel_alvo)
    if not custo:
        return {"tipo": "feedback", "log": ["Custo de melhoria não encontrado."]}

    if jogador.ouro < custo["ouro"]:
        return {"tipo": "feedback", "log": ["Ouro insuficiente para melhoria."]}

    if not _tem_materiais(jogador, custo.get("materiais", {})):
        return {"tipo": "feedback", "log": ["Materiais insuficientes para melhoria."]}

    jogador.ouro -= custo["ouro"]
    _consumir_materiais(jogador, custo.get("materiais", {}))
    jogador.niveis_estruturas[id_estrutura] = nivel_alvo

    return {"tipo": "feedback", "log": [f"{id_estrutura} melhorada para nível {nivel_alvo}."]}
