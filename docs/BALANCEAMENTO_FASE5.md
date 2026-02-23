# Fase 5 — Balanceamento e Regressão

## Objetivo
Consolidar uma malha de testes e métricas para detectar regressões de progressão e combate.

## Métricas iniciais
- Turnos médios para derrotar `lobo_cinzento` e `goblin_batedor`
- HP restante após sequência de combates
- Evolução de nível após rodada fixa de encontros

## Critérios de sanidade
- Personagem base não deve morrer em 1 turno contra monstro de nível equivalente
- Combate inicial deve terminar em até 10 turnos
- Progressão mínima: após 3 vitórias em encontros de nível baixo, personagem deve ganhar XP

## Uso
```bash
python scripts/relatorio_balance.py
```
