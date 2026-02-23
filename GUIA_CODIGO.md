# Guia rápido da base de código

## Visão geral
- O projeto é um RPG textual em Python com arquitetura modular em camadas.
- A lógica de jogo fica centralizada em `GameManager`, enquanto interfaces (console/GUI) atuam como clientes dessa API.
- O conteúdo (raças, classes, habilidades, monstros, itens, quests) é majoritariamente orientado a dados em dicionários no pacote `rpg/dados`.

## Estrutura principal
- `console_client.py`: cliente de terminal com loop principal e interação do jogador.
- `rpg/game_manager.py`: orquestra estados do jogo (`main_menu`, `character_creation`, `in_game`, `combat`) e expõe métodos para UI.
- `rpg/entidades`: modelos centrais (`Personagem`, `Monstro`, `Quest`, `Item`, etc.).
- `rpg/sistemas`: regras de domínio (combate, quests, crafting, progressão, economia...).
- `rpg/io`: API de criação e telas/menus da interface textual (inventário, equipamento, save/load).
- `rpg/fabricas`: fábricas para instanciar entidades a partir de dados (ex.: monstros).
- `rpg/dados`: banco de conteúdo do jogo em Python (JSON-like).
- `rpg/testes`: suíte de testes `unittest` cobrindo combate, criação, inventário, quests e equipamentos.

## Fluxo arquitetural (resumido)
1. UI chama `GameManager`.
2. `GameManager` delega regras para módulos de `rpg/sistemas` e `rpg/io`.
3. Entidades em `rpg/entidades` mantêm estado e comportamento base.
4. Conteúdo é carregado de `rpg/dados` e instanciado por fábricas.

## Pontos importantes para onboarding
- Priorize compreender `GameManager` antes de alterar sistemas isolados.
- Trate `rpg/dados` como fonte de verdade para balanceamento e expansão de conteúdo.
- Ao mexer em cálculo de atributos/efeitos, valide regressão em `Personagem.recalcular_stats_completos`.
- Ao mexer no combate, siga o pipeline: regeneração -> ação do jogador -> checagem de vitória -> turno inimigo -> checagem de derrota.
- Mantenha a separação: UI não deve conter regra de negócio; só orquestra entrada/saída.

## Como aprender mais rápido
- Comece lendo nesta ordem:
  1. `README.md`
  2. `console_client.py`
  3. `rpg/game_manager.py`
  4. `rpg/entidades/personagem.py`
  5. `rpg/sistemas/combate.py`
  6. `rpg/io/criacao_personagem.py`
  7. `rpg/testes/*`
- Depois, faça pequenas mudanças orientadas a teste (ex.: ajustar um efeito e rodar suíte).
- Adicione conteúdo primeiro em `rpg/dados` e só depois altere código, quando realmente necessário.

## Comandos úteis
```bash
python -m unittest discover rpg/testes
python console_client.py
```
