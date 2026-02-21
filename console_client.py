from rpg.game_manager import GameManager


def main_loop() -> None:
    gm = GameManager()
    print("=== RPG Reboot ===")

    while gm.estado.etapa != "fim":
        meta = gm.opcoes_etapa()
        if meta["tipo"] == "input":
            valor = input("Nome do personagem: ")
        else:
            print(f"Opções de {meta['campo']}: {', '.join(meta['opcoes'])}")
            valor = input("Escolha: ").strip().lower()
        gm.processar(valor)

    p = gm.jogador
    print(f"Personagem criado: {p.nome} | {p.raca}/{p.sub_raca} | {p.classe}")


if __name__ == "__main__":
    main_loop()
