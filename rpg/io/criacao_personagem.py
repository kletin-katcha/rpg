from typing import TYPE_CHECKING, Dict, Any, List
from ..entidades.personagem import Personagem
from ..dados.racas_base import RACAS
from ..dados.classes_iniciais import CLASSES_INICIAIS

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

def get_dados_racas() -> Dict[str, Any]:
    """Retorna o dicionário completo de raças para a UI exibir."""
    return RACAS

def get_dados_classes() -> Dict[str, Any]:
    """Retorna o dicionário completo de classes para a UI exibir."""
    return CLASSES_INICIAIS

def aplicar_raca(personagem: 'Personagem', id_raca: str):
    """Aplica os modificadores e habilidades de uma raça ao personagem."""
    if id_raca not in RACAS:
        raise ValueError(f"Raça inválida: {id_raca}")

    personagem.raca = id_raca
    raca_data = RACAS[id_raca]

    for stat, mod in raca_data.get('modificadores_stats', {}).items():
        base_stat_nome = 'base_' + stat
        if hasattr(personagem, base_stat_nome):
            setattr(personagem, base_stat_nome, getattr(personagem, base_stat_nome) + mod)

    for habilidade in raca_data.get('habilidades_raciais', []):
        personagem.habilidades.append(habilidade)

    # Recalcula os stats para refletir as mudanças da raça
    personagem.recalcular_stats_completos()

def aplicar_classe(personagem: 'Personagem', id_classe: str):
    """Aplica as habilidades e equipamentos iniciais de uma classe ao personagem."""
    if id_classe not in CLASSES_INICIAIS:
        raise ValueError(f"Classe inválida: {id_classe}")

    personagem.classe = id_classe
    classe_data = CLASSES_INICIAIS[id_classe]

    for habilidade in classe_data.get('habilidades_iniciais', []):
        personagem.habilidades.append(habilidade)

    equipamento_inicial = classe_data.get('equipamento_inicial', {})
    for slot, id_item in equipamento_inicial.items():
        # Adiciona o item e o equipa. O método equipar já lida com a remoção do inventário.
        personagem.adicionar_item(id_item, 1)
        personagem.equipar_item(id_item) # equipar_item já chama recalcular_stats_completos

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
