# RPG Surreal (novo repositório base)

Este repositório foi reiniciado para construir um RPG novo, com foco em:

- arquitetura modular
- evolução incremental (1 arquivo por vez)
- testes de sanidade desde o começo

## Estrutura inicial

- `docs/`: planejamento e decisões arquiteturais
- `rpg/`: código-fonte do jogo
- `tests/`: testes automatizados mínimos
- `scripts/`: utilitários de desenvolvimento

## Como rodar

```bash
python -m rpg.main
```

## Como validar

```bash
python scripts/verificar_sintaxe.py
python scripts/validar_content.py
python -m unittest discover tests
python scripts/relatorio_balance.py
python scripts/check_all.py
```

## Fase atual
- Fase 6 concluída: hardening com save/load e pipeline único de checagem.
