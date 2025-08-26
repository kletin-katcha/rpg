import random
from typing import List, Dict, Any, Optional

from ..dados.monstros_area1 import MONSTROS_AREA1
from ..dados.monstros_area2 import MONSTROS_AREA2
from ..fabricas.fabrica_monstros import criar_monstro_por_id

class Room:
    """
    Representa uma única sala ou área dentro de uma dungeon.
    """
    def __init__(self, nome: str, descricao: str, monstros: Optional[List[str]] = None, tesouros: Optional[List[Dict]] = None, armadilhas: Optional[List[Dict]] = None):
        self.nome = nome
        self.descricao = descricao
        self.monstros = monstros if monstros else []
        self.tesouros = tesouros if tesouros else []
        self.armadilhas = armadilhas if armadilhas else []
        self.visitada = False
        self.concluida = False # Monstros derrotados, tesouros pegos, etc.

class Dungeon:
    """
    Representa uma dungeon, que é uma coleção de salas interligadas.
    """
    def __init__(self, id_dungeon: str, nome: str, descricao: str, nivel_minimo: int, salas: List[Room]):
        self.id_dungeon = id_dungeon
        self.nome = nome
        self.descricao = descricao
        self.nivel_minimo = nivel_minimo
        self.salas = salas
        self.sala_atual_idx = 0

    @property
    def sala_atual(self) -> Room:
        return self.salas[self.sala_atual_idx]

    def avancar_sala(self) -> bool:
        """Avança para a próxima sala, se possível. Retorna True se avançou."""
        if self.sala_atual_idx < len(self.salas) - 1:
            self.sala_atual_idx += 1
            return True
        return False

    def esta_concluida(self) -> bool:
        """Verifica se todas as salas da dungeon foram concluídas."""
        return all(s.concluida for s in self.salas)

def gerar_dungeon_aleatoria(nivel_jogador: int) -> Dungeon:
    """
    Gera uma dungeon procedural simples.
    """
    num_salas = random.randint(3, 5)

    # Seleciona a lista de monstros com base no nível do jogador
    if nivel_jogador < 10:
        pool_monstros = MONSTROS_AREA1
    else:
        pool_monstros = MONSTROS_AREA2 # Simplificação, poderia ser uma união

    salas = []
    for i in range(num_salas):
        nome_sala = f"Câmara {i+1}"
        descricao_sala = "Uma sala úmida e escura. O som de água pingando ecoa."

        # Adiciona monstros a todas as salas, exceto a última
        monstros_na_sala = []
        if i < num_salas - 1:
            num_monstros = random.randint(1, 2)
            for _ in range(num_monstros):
                monstros_na_sala.append(random.choice(list(pool_monstros.keys())))

        salas.append(Room(nome=nome_sala, descricao=descricao_sala, monstros=monstros_na_sala))

    # Adiciona um mini-chefe na última sala
    id_chefe = random.choice(list(pool_monstros.keys()))
    chefe = criar_monstro_por_id(id_chefe)
    chefe.nome = f"{chefe.nome} Ameaçador(a)"
    chefe.nivel = int(chefe.nivel * 1.5)
    chefe.recalcular_stats_completos() # Atualiza stats com base no novo nível
    # TODO: Precisamos de uma forma de adicionar este monstro modificado ao combate.
    # Por enquanto, vamos usar o ID original.
    salas[-1].monstros = [id_chefe]
    salas[-1].nome = "Covil do Guardião"
    salas[-1].descricao = "Uma câmara maior com ossos espalhados pelo chão. Uma criatura ameaçadora guarda a saída."

    return Dungeon(
        id_dungeon=f"random_dungeon_{random.randint(1000, 9999)}",
        nome="Caverna Misteriosa",
        descricao="Uma caverna que apareceu subitamente.",
        nivel_minimo=nivel_jogador,
        salas=salas
    )
