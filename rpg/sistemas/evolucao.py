from typing import TYPE_CHECKING, List, Dict, Any

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

from ..dados.classes_avancadas import CLASSES_AVANCADAS

def get_evolucoes_disponiveis(personagem: 'Personagem') -> Dict[str, Dict]:
    """
    Verifica e retorna um dicionário de classes avançadas disponíveis para o personagem.
    """
    evolucoes = {}
    for id_classe_av, dados_classe in CLASSES_AVANCADAS.items():
        if dados_classe["classe_base"] == personagem.classe and \
           personagem.nivel >= dados_classe["nivel_necessario"]:
            evolucoes[id_classe_av] = dados_classe

    return evolucoes

def evoluir_classe(personagem: 'Personagem', id_classe_avancada: str) -> list[str]:
    """
    Evolui a classe do personagem, aplicando os bônus e novas habilidades.
    Retorna uma lista de logs.
    """
    logs = []

    evolucoes = get_evolucoes_disponiveis(personagem)
    if id_classe_avancada not in evolucoes:
        logs.append("Você não cumpre os requisitos para esta evolução.")
        return logs

    dados_evolucao = evolucoes[id_classe_avancada]

    # Atualiza a classe do personagem
    personagem.classe = id_classe_avancada
    logs.append(f"Você evoluiu para {dados_evolucao['nome']}!")

    # Concede novas habilidades
    habilidades = dados_evolucao.get("habilidades_concedidas", [])
    if habilidades:
        logs.append("Você aprendeu novas habilidades:")
        for id_habilidade in habilidades:
            personagem.habilidades.append(id_habilidade)
            logs.append(f"  - {id_habilidade.replace('_', ' ').title()}")

    # Aplica bônus de stats permanentes
    bonus_stats = dados_evolucao.get("bonus_stats", {})
    if bonus_stats:
        logs.append("Seus atributos base foram fortalecidos:")
        for stat, bonus in bonus_stats.items():
            base_stat_nome = f"base_{stat}"
            if hasattr(personagem, base_stat_nome):
                valor_antigo = getattr(personagem, base_stat_nome)
                setattr(personagem, base_stat_nome, valor_antigo + bonus)
                logs.append(f"  - {stat.capitalize()}: +{bonus}")

    # Recalcula todos os stats derivados
    personagem.recalcular_stats_completos()
    logs.append("Seu poder aumentou!")

    return logs
