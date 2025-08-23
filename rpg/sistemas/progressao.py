from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem
    from ..entidades.monstro import Monstro

def calcular_xp_final(jogador: 'Personagem', monstro: 'Monstro') -> int:
    """
    Calcula a quantidade final de XP a ser recompensada,
    ajustando com base na diferença de nível.
    """
    xp_base = monstro.xp_recompensa
    diferenca_nivel = monstro.nivel - jogador.nivel

    modificador = 1.0

    # Ganha mais XP de monstros de nível mais alto
    if diferenca_nivel > 0:
        modificador += diferenca_nivel * 0.1 # 10% a mais por nível de diferença
    # Ganha menos XP de monstros de nível muito mais baixo
    elif diferenca_nivel < -5:
        modificador -= abs(diferenca_nivel + 5) * 0.1 # 10% a menos para cada nível abaixo de 5 de diferença

    # Garante que o modificador não seja negativo
    modificador = max(0.1, modificador)

    xp_final = int(xp_base * modificador)

    return xp_final

def verificar_desbloqueios_classe(personagem: 'Personagem'):
    """
    Verifica se o personagem cumpre os requisitos para desbloquear novas classes.
    Esta função será expandida na Fase 4.
    """
    # Placeholder
    # Ex: if personagem.nivel >= 20 and personagem.classe.id == "guerreiro":
    #         print("Você pode evoluir para a classe 'Cavaleiro'!")
    pass
