# RPG Textual Colossal

Este repositório contém o código para um RPG textual massivo, modular e expansível, construído em Python. O objetivo é criar um dos maiores e mais profundos RPGs baseados em texto já feitos, com uma vasta gama de raças, classes, habilidades e um mundo gerado proceduralmente.

## Visão do Projeto

- **Escala Massiva:** Mais de 200.000 linhas de código e conteúdo.
- **Conteúdo Profundo:** Mais de 30 raças, 170 classes e 5.200 habilidades.
- **Mundo Dinâmico:** Geração procedural de áreas, dungeons e eventos.
- **Narrativa Épica:** Uma história principal dividida em 10 atos.
- **Sistemas Complexos:** Combate tático, crafting, economia viva e meta-progressão.

## Como Executar o Jogo

Este projeto é estruturado como um pacote Python. Para executá-lo corretamente, você deve usar o interpretador Python com a flag `-m`, que o trata como um módulo.

1.  Navegue até o diretório raiz do projeto (o diretório que contém a pasta `rpg`).
2.  Execute o seguinte comando no seu terminal:

    ```bash
    python -m rpg.main
    ```

Isso iniciará o jogo e exibirá o menu principal.

## Como Executar os Testes

O projeto inclui um conjunto de testes automatizados para garantir a estabilidade do código.

1.  Navegue até o diretório raiz do projeto.
2.  Execute o seguinte comando no seu terminal para rodar todos os testes na pasta `testes`:

    ```bash
    python -m unittest discover rpg/testes
    ```

    Ou, para um teste específico:

    ```bash
    python -m unittest rpg.testes.test_run
    ```

Isso executará todos os testes e relatará quaisquer problemas.
