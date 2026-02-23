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
python scripts/validar_referencias_content.py
python -m unittest discover tests
python scripts/relatorio_balance.py
python scripts/gate_kpis.py
python scripts/load_test_systems.py
python scripts/check_all.py
python scripts/auditar_fases.py
```

Runbook operacional: `docs/RUNBOOK_OPERACIONAL.txt`.

## Fase atual
- Fase 25 concluída: expansão massiva entregue com regiões, dungeons, agenda faccional, arcos longos e ferramentas headless.
- Fase 20 concluída: crises urbanas dinâmicas reativas à tensão de facções e ao clima.

## Auditoria de fases (1-25)
- Execute `python scripts/auditar_fases.py` para validar uma trilha funcional representativa do progresso completo, incluindo expansão 21-25 e teste end-to-end.

- Comando `diagnostico_fases_1_25` no jogo para snapshot de consistência funcional (inclui validação da expansão 21-25).
