"""API de criação de personagem, catálogos de conteúdo e progressão."""
from typing import TYPE_CHECKING, Dict, Any, List
import unicodedata
from ..entidades.personagem import Personagem
from ..dados.racas_base import RACAS
from ..dados.racas_expandidas import RACAS_EXPANDIDAS
from ..dados.racas_mvp_estruturadas import RACAS_MVP_ESTRUTURADAS
from ..dados.sub_racas_mvp_estruturadas import SUB_RACAS_MVP_ESTRUTURADAS
from ..dados.classes_iniciais import CLASSES_INICIAIS
from ..dados.classes_extras import CLASSES_EXTRAS
from ..dados.classes_unicas_raciais import CLASSES_UNICAS_RACIAIS
from ..dados.sub_racas_padrao import SUB_RACAS_PADRAO
from ..dados.arvores_habilidades_universais import ARVORES_HABILIDADES_UNIVERSAIS
from ..dados.arvores_habilidades_classes import ARVORES_HABILIDADES_CLASSES
from ..dados.arvores_habilidades_racas import ARVORES_HABILIDADES_RACAS
from ..dados.classes_iniciais_expandidas import CLASSES_INICIAIS_EXPANDIDAS
from ..dados.classes_evolucoes import CLASSES_EVOLUCOES
from ..dados.classes_secretas import CLASSES_SECRETAS
from ..dados.side_quests_classes_secretas import SIDE_QUESTS_CLASSES_SECRETAS
from ..dados.racas_expandidas import RACAS_EXPANDIDAS
from ..dados.racas_massivas import RACAS_MASSIVAS
from ..dados.classes_extras import CLASSES_EXTRAS
from ..dados.classes_unicas_raciais import CLASSES_UNICAS_SUBRACAIS
from ..dados.sub_racas_padrao import SUB_RACAS_PADRAO
from ..dados.arvores_habilidades_massivas import get_catalogo_arvores

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

# Este módulo foi refatorado para ser uma API de lógica de negócios,
# em vez de uma interface de console interativa. A UI (GUI ou Console)
# chamará essas funções para construir o personagem passo a passo.

def criar_personagem_base(nome: str) -> 'Personagem':
    """Cria a instância inicial de um personagem apenas com o nome."""
    if not nome:
        raise ValueError("O nome não pode estar em branco.")
    return Personagem(nome=nome)

def _gerar_sub_racas_padrao(nome_raca: str) -> List[Dict[str, Any]]:
    """Gera sub-raças padrão para raças que ainda não possuem variações explícitas."""
    return [
        {
            "nome": f"{nome_raca} {modelo['sufixo_nome']}",
            "descricao": modelo["descricao"],
            "modificadores_stats": dict(modelo["modificadores_stats"]),
        }
        for modelo in SUB_RACAS_PADRAO
    ]


def _enriquecer_raca_com_variacoes(id_raca: str, dados_raca: Dict[str, Any]) -> Dict[str, Any]:
    """Retorna uma cópia da raça garantindo que ela possua ao menos uma sub-raça."""
    dados = dict(dados_raca)
    variacoes = list(dados.get("variacoes", []))
    if not variacoes:
        nome_raca = dados.get("nome", id_raca.replace("_", " ").title())
        variacoes = _gerar_sub_racas_padrao(nome_raca)
    dados["variacoes"] = variacoes
    return dados


def get_dados_racas() -> Dict[str, Any]:
    """Retorna o dicionário completo de raças para a UI exibir."""
    racas = dict(RACAS)
    racas.update(RACAS_EXPANDIDAS)
    racas.update(RACAS_MVP_ESTRUTURADAS)
    racas.update(RACAS_MASSIVAS)
    return {id_raca: _enriquecer_raca_com_variacoes(id_raca, dados) for id_raca, dados in racas.items()}

def get_dados_classes() -> Dict[str, Any]:
    """Retorna o dicionário completo de classes para a UI exibir."""
    classes = dict(CLASSES_INICIAIS)
    classes.update(CLASSES_EXTRAS)
    classes.update(CLASSES_UNICAS_RACIAIS)
    classes.update(CLASSES_UNICAS_SUBRACAIS)
    return classes

def get_classes_secundarias_disponiveis(id_classe_principal: str | None) -> List[str]:
    """Retorna opções de classe secundária válidas para a classe principal atual."""
    if not id_classe_principal:
        return list(get_dados_classes().keys())
    return [id_classe for id_classe in get_dados_classes().keys() if id_classe != id_classe_principal]

def _normalizar_id_sub_raca(nome: str) -> str:
    """Converte nome de variação para um ID estável sem acentos."""
    texto = unicodedata.normalize("NFD", nome)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto.lower().replace(" ", "_")

def get_dados_sub_racas(id_raca: str) -> Dict[str, Any]:
    """Retorna sub-raças de uma raça; usa arquivo dedicado para o catálogo MVP estruturado."""
    """Retorna variações (sub-raças) de uma raça em formato indexado por ID."""
    racas = get_dados_racas()
    if id_raca not in racas:
        raise ValueError(f"Raça inválida: {id_raca}")

    if id_raca in SUB_RACAS_MVP_ESTRUTURADAS:
        return dict(SUB_RACAS_MVP_ESTRUTURADAS[id_raca])

    variacoes = racas[id_raca].get("variacoes", [])
    resultado: Dict[str, Any] = {}
    for variacao in variacoes:
        id_sub_raca = variacao.get("id") or _normalizar_id_sub_raca(variacao["nome"])
        resultado[id_sub_raca] = variacao

    return resultado

def aplicar_raca(personagem: 'Personagem', id_raca: str):
    """Aplica os modificadores e habilidades de uma raça ao personagem."""
    racas = get_dados_racas()
    if id_raca not in racas:
        raise ValueError(f"Raça inválida: {id_raca}")

    personagem.raca = id_raca
    raca_data = racas[id_raca]

    for stat, mod in raca_data.get('modificadores_stats', {}).items():
        base_stat_nome = 'base_' + stat
        if hasattr(personagem, base_stat_nome):
            setattr(personagem, base_stat_nome, getattr(personagem, base_stat_nome) + mod)

    for habilidade in raca_data.get('habilidades_raciais', []):
        personagem.habilidades.append(habilidade)

    # Recalcula os stats para refletir as mudanças da raça
    personagem.recalcular_stats_completos()

def aplicar_sub_raca(personagem: 'Personagem', id_sub_raca: str):
    """Aplica uma variação/sub-raça baseada na raça atual do personagem."""
    if not personagem.raca:
        raise ValueError("Defina a raça antes da sub-raça.")

    sub_racas = get_dados_sub_racas(personagem.raca)
    if id_sub_raca not in sub_racas:
        raise ValueError(f"Sub-raça inválida para '{personagem.raca}': {id_sub_raca}")

    personagem.sub_raca = id_sub_raca
    dados_sub_raca = sub_racas[id_sub_raca]

    for stat, mod in dados_sub_raca.get('modificadores_stats', {}).items():
        base_stat_nome = 'base_' + stat
        if hasattr(personagem, base_stat_nome):
            setattr(personagem, base_stat_nome, getattr(personagem, base_stat_nome) + mod)

    personagem.recalcular_stats_completos()

def aplicar_classe(personagem: 'Personagem', id_classe: str):
    """Aplica as habilidades e equipamentos iniciais de uma classe ao personagem."""
    classes = get_dados_classes()
    if id_classe not in classes:
        raise ValueError(f"Classe inválida: {id_classe}")

    personagem.classe = id_classe
    classe_data = classes[id_classe]

    for habilidade in classe_data.get('habilidades_iniciais', []):
        personagem.habilidades.append(habilidade)

    equipamento_inicial = classe_data.get('equipamento_inicial', {})
    for slot, id_item in equipamento_inicial.items():
        # Adiciona o item e o equipa. O método equipar já lida com a remoção do inventário.
        personagem.adicionar_item(id_item, 1)
        personagem.equipar_item(id_item) # equipar_item já chama recalcular_stats_completos

def aplicar_classe_secundaria(personagem: 'Personagem', id_classe: str):
    """Aplica uma classe secundária de forma leve (sem trocar equipamento)."""
    if personagem.classe_secundaria:
        raise ValueError("Personagem já possui classe secundária.")

    if id_classe == personagem.classe:
        raise ValueError("Classe secundária não pode ser igual à classe principal.")

    classes = get_dados_classes()
    if id_classe not in classes:
        raise ValueError(f"Classe inválida: {id_classe}")

    personagem.classe_secundaria = id_classe
    classe_data = classes[id_classe]

    # MVP: herda apenas a primeira habilidade inicial para não inflar poder.
    habilidades = classe_data.get('habilidades_iniciais', [])
    if habilidades:
        habilidade = habilidades[0]
        if habilidade not in personagem.habilidades:
            personagem.habilidades.append(habilidade)

    personagem.recalcular_stats_completos()

def aplicar_atributos(personagem: 'Personagem', pontos: Dict[str, int]):
    """
    Distribui os pontos de atributo no personagem.
    `pontos` é um dicionário como {'forca': 5, 'destreza': 5, ...}
    """
    pontos_gastos = sum(pontos.values())
    if pontos_gastos > 20: # A regra de negócio de 20 pontos
        raise ValueError(f"Tentativa de gastar {pontos_gastos} pontos, mas o limite é 20.")

    for stat, valor in pontos.items():
        base_stat_nome = 'base_' + stat
        if hasattr(personagem, base_stat_nome):
            setattr(personagem, base_stat_nome, getattr(personagem, base_stat_nome) + valor)

    personagem.recalcular_stats_completos()

def finalizar_criacao(personagem: 'Personagem') -> 'Personagem':
    """
    Realiza os cálculos finais e garante que o personagem está pronto para o jogo.
    """
    # Garante que o personagem comece com os recursos no máximo após todos os cálculos.
    # Esta chamada já existe no __init__ do Personagem, mas uma chamada extra aqui
    # garante o estado final correto após todas as modificações.
    personagem.recalcular_stats_completos()
    personagem.hp_atual = personagem.hp_max
    personagem.mp_atual = personagem.mp_max
    personagem.stamina_atual = personagem.stamina_max
    return personagem


def get_classes_unicas_por_raca(id_raca: str) -> List[str]:
    """Retorna classes únicas raciais (não sub-raciais) para o catálogo estruturado."""
    racas = get_dados_racas()
    if id_raca not in racas:
        raise ValueError(f"Raça inválida: {id_raca}")

    classe = racas[id_raca].get("classe_unica_racial")
    return [classe] if classe else []


def get_catalogo_classes_progressao() -> Dict[str, Any]:
    """Retorna classes iniciais, evoluções e secretas com suas referências."""
    return {
        "iniciais": CLASSES_INICIAIS_EXPANDIDAS,
        "evolucoes": CLASSES_EVOLUCOES,
        "secretas": CLASSES_SECRETAS,
        "side_quests_secretas": SIDE_QUESTS_CLASSES_SECRETAS,
    }
def get_classes_unicas_por_sub_raca(id_raca: str, id_sub_raca: str) -> List[str]:
    """Retorna as classes únicas disponíveis para uma sub-raça específica."""
    sub_racas = get_dados_sub_racas(id_raca)
    if id_sub_raca not in sub_racas:
        raise ValueError(f"Sub-raça inválida para '{id_raca}': {id_sub_raca}")
    return list(sub_racas[id_sub_raca].get("classes_unicas_sub_raca", []))


def get_catalogo_arvores_habilidades() -> Dict[str, Dict[str, Dict[str, Any]]]:
    """Retorna o catálogo consolidado de árvores universais, de classe e de raça."""
    return {
        "universais": ARVORES_HABILIDADES_UNIVERSAIS,
        "classes": ARVORES_HABILIDADES_CLASSES,
        "racas": ARVORES_HABILIDADES_RACAS,
    }
    return get_catalogo_arvores()
