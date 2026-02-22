# Planejamento Mestre — RPG Surreal

## Visão
Criar um RPG expansível com sistemas de progressão, exploração, cidade e crafting, sem herdar acoplamentos antigos.

## Fases

### Fase 0 — Fundação (agora)
- Estrutura de repositório limpa
- Entrypoint funcional
- Testes mínimos de sanidade
- Documento de arquitetura base

### Fase 1 — Núcleo jogável
- Criação de personagem (nome, raça, classe)
- Estado de jogo em memória
- Loop de cidade inicial

### Fase 2 — Combate e progressão
- Sistema de combate por turnos
- XP, níveis e atributos derivados
- Primeiros inimigos e loot

### Fase 3 — Economia, forja e cidade
- Inventário robusto
- Receitas e forja
- Melhorias de cidade e automação inicial

### Fase 4 — Conteúdo massivo e UX
- Catálogos expandidos (raças/classes/árvores)
- Melhorias de interface (console/gui)
- Balanceamento e testes de regressão

## Regras de execução
1. Implementar em fatias pequenas.
2. Cada mudança com testes.
3. Sem mega-commits de reescrita total.


## Status atual
- Contratos do núcleo definidos.
- Loader de conteúdo e schemas iniciais implementados (raças, classes, itens).

- Domínios iniciais implementados: `systems/character` e `systems/inventory` com service/rules/testes.

- Fase 1 concluída: criação de personagem + estado em memória + loop de cidade inicial.
- Fase 2 concluída: combate por turnos, XP/níveis em combate e primeiros inimigos com loot.
