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

### Fase 5 — Estabilização e telemetria de balanceamento
- Relatórios de balanceamento automatizados
- Testes de regressão de métricas de combate/progressão
- Critérios de sanidade para tuning contínuo

### Fase 6 — Hardening e readiness
- Save/Load de sessão
- Pipeline único de checagem local
- Reforço de regressão para fluxo de estado

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
- Fase 3 concluída: inventário robusto inicial, forja por receita e automação inicial da cidade.
- Fase 4 concluída: expansão de catálogos, árvore de habilidades base e melhorias de UX com aliases/ajuda/histórico.
- Fase 5 concluída: relatório de balanceamento automatizado e testes de regressão de métricas.
- Fase 6 concluída: persistência (save/load), comando integrado no loop e pipeline de checks local.

### Fase 7 — Meta-sistemas e mundo dinâmico
- Facções e reputação inicial
- Eventos dinâmicos de mundo
- Contratos procedurais
- Fase 7 concluída: facções/reputação base, eventos de mundo e contratos aleatórios integrados.

### Fase 8 — Progressão de habilidades em runtime
- Desbloqueio de nós em árvore de habilidades com pré-requisitos
- Aplicação de efeitos simples no estado do personagem
- Ações de cidade para visualizar árvore e desbloquear habilidades
- Fase 8 concluída: desbloqueio da árvore `combate_base` integrado no loop com persistência.


### Fase 9 — Contratos executáveis e reputação progressiva
- Contrato aleatório vira contrato ativo no estado do jogo
- Conclusão de contrato concede XP, ouro e reputação por facção
- Persistência do contrato ativo no save/load
- Fase 9 concluída: contratos agora fecham o loop de progressão meta e economia.
