from typing import TYPE_CHECKING
from decimal import Decimal, ROUND_HALF_UP

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def criar_descendente(personagem_anterior: 'Personagem') -> 'Personagem':
    """
    Cria um novo personagem "descendente" que herda uma pequena porção
    do poder do personagem anterior.
    """
    from ..entidades.personagem import Personagem

    print("\nO legado do seu herói continua...")
    print("Você pode começar uma nova vida como um descendente direto,")
    print("carregando uma centelha do poder de seu ancestral.")

    # 1. Criar um novo personagem com um novo nome
    novo_nome = input("Digite o nome do descendente: ").strip()
    if not novo_nome:
        novo_nome = f"Descendente de {personagem_anterior.nome}"

    descendente = Personagem(nome=novo_nome, nivel=1)

    # 2. Herdar 5% dos atributos base
    atributos_herdaveis = [
        "forca", "destreza", "constituicao",
        "inteligencia", "sabedoria", "carisma"
    ]

    print("\nO sangue do herói corre em suas veias, concedendo-lhe força inata:")
    for attr in atributos_herdaveis:
        valor_anterior = getattr(personagem_anterior, attr)
        bonus = valor_anterior * Decimal('0.05')

        # Arredonda para o inteiro mais próximo, com .5 indo para cima.
        bonus_arredondado = int(bonus.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        if bonus_arredondado > 0:
            valor_atual = getattr(descendente, attr)
            setattr(descendente, attr, valor_atual + bonus_arredondado)
            print(f"  + {bonus_arredondado} em {attr.capitalize()}")

    # 3. Herdar passivas fracas (placeholder)
    # TODO: Implementar um sistema de Habilidades e Passivas.
    # Ex: passivas_fracas = [p for p in personagem_anterior.passivas if p.tag == "fraca"]
    # if passivas_fracas:
    #     heranca_passiva = random.choice(passivas_fracas)
    #     descendente.passivas.append(heranca_passiva)
    #     print(f"Você herdou a habilidade passiva: {heranca_passiva.nome}")

    # 4. Recalcular stats e curar o personagem
    descendente.recalcular_stats_completos()
    descendente.hp_atual = descendente.hp_max
    descendente.mp_atual = descendente.mp_max

    print("\nUm novo começo, com o peso e a promessa de um grande legado.")
    return descendente
