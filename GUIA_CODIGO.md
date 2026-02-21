# Guia de Código

## Princípios
1. Um arquivo por responsabilidade.
2. Dados de catálogo separados da lógica.
3. GameManager apenas orquestra fluxo.
4. Sem side-effects implícitos em import.

## Estrutura
- `rpg/catalog.py`: dados base do jogo.
- `rpg/domain.py`: entidades e estado.
- `rpg/engine.py`: regras puras.
- `rpg/game_manager.py`: fluxo de criação/jogo.
- `console_client.py`: interface terminal.
