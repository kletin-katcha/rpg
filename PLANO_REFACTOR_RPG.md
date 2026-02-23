# Plano de refatoração total do RPG (com interface moderna + expansão de conteúdo)

## Resposta curta
Sim — dá para refazer o RPG com uma interface muito melhor e escalar bastante o conteúdo.

A forma **mais segura** não é “jogar tudo fora”, e sim fazer uma migração em fases:
1. isolar o núcleo de regras,
2. construir uma nova UI por cima,
3. migrar conteúdo para pipeline de dados validado,
4. expandir sistemas com testes e telemetria.

---

## Objetivo de produto
- Interface moderna (desktop/web) com UX clara para combate, inventário, quests e progressão.
- Core engine desacoplado da interface para permitir múltiplos clientes (CLI, GUI, web).
- Conteúdo expansível (raças/classes/habilidades/itens/áreas/quests) com validação automática.
- Base preparada para crescimento contínuo sem quebrar balanceamento.

---

## Arquitetura-alvo (alto nível)

### 1) Camadas
- **Core (domínio):** regras puras de jogo (combate, efeitos, progressão, economia, quests).
- **Application (casos de uso):** fluxo de ações (iniciar combate, usar habilidade, concluir quest).
- **Adapters (infra/UI):** armazenamento, serialização, UI desktop/web, API opcional.
- **Content pipeline:** carregamento de dados versionados e validados.

### 2) Contratos estáveis
- Definir DTOs/eventos para UI consumir (`GameStateSnapshot`, `CombatEvent`, `QuestEvent`).
- Nenhuma regra de negócio dentro da UI.

### 3) Modelo orientado a dados
- Mover conteúdo para arquivos de dados (JSON/YAML) com schema (Pydantic/JSON Schema).
- Validar tudo no CI: IDs únicos, referências válidas, ranges de balanceamento.

---

## UI recomendada (duas opções)

### Opção A — Web app (recomendada)
- Backend Python (FastAPI) expondo estado/eventos do jogo.
- Frontend React + TypeScript para interface rica (inventário drag-and-drop, tooltips, logs filtráveis).
- Vantagens: iteração rápida, visual moderno, fácil distribuição.

### Opção B — Desktop Python
- PySide6/Qt com arquitetura MVVM.
- Vantagens: stack única em Python; desvantagem: ecossistema UI menos ágil que web.

---

## Plano de execução (6 fases)

## Fase 0 — Diagnóstico e baseline (1 semana)
- Mapear dependências e pontos críticos (`GameManager`, combate, criação, inventário).
- Congelar contratos mínimos para não quebrar fluxo atual.
- Métrica inicial: cobertura de testes, tempo de turno, bugs conhecidos.

## Fase 1 — Extração do núcleo (2–3 semanas)
- Criar pacote `rpg/core` com entidades e serviços puros.
- Substituir acessos diretos por interfaces/repositórios.
- Manter CLI atual funcionando como cliente do novo core.

## Fase 2 — API de estado/eventos (2 semanas)
- Introduzir “event sourcing leve” para ações do jogador e resultados do turno.
- Expor snapshots consistentes para qualquer UI.
- Garantir replay de combate para debug.

## Fase 3 — Nova interface (3–5 semanas)
- Implementar telas-chave: menu, criação, hub de cidade, combate tático, inventário/equipamentos, diário.
- UX mínima: atalhos, feedback visual de buffs/debuffs, histórico de ação.

## Fase 4 — Pipeline de conteúdo massivo (contínuo)
- Estruturar pastas de conteúdo por domínio: `racas/`, `classes/`, `habilidades/`, `itens/`, `quests/`, `areas/`.
- Criar lint de conteúdo e testes de consistência.
- Ferramentas para autores: templates e geradores de boilerplate.

## Fase 5 — Balanceamento e progressão longa (contínuo)
- Simulador automático de combates para detectar outliers.
- Tabelas de progressão por faixa de nível.
- Métricas de economia (entrada/saída de ouro, inflação de recursos).

---

## Sistemas para “acrescentar muito mais conteúdo”
- Árvore de classes em múltiplas trilhas (inicial → intermediária → avançada/oculta).
- Biomas e dungeons com afixos/modificadores de temporada.
- Quests com estados globais e reputação por facção.
- Crafting em cadeias (coleta → refinamento → manufatura).
- Eventos mundiais procedurais + chefes regionais.
- Enciclopédia interna com descoberta progressiva de lore.

---

## Qualidade e segurança de evolução
- Testes de unidade para cálculo de stats, efeitos e regras de alvo.
- Testes de integração para loop de combate e fluxo de quest.
- Testes de regressão de conteúdo (todo ID referenciado existe).
- CI com validação de schema + suíte de simulação curta.

---

## Riscos e mitigação
- **Risco:** rewrite total travar entrega.
  - **Mitigação:** estratégia Strangler (migrar módulo por módulo).
- **Risco:** explosão de conteúdo gerar inconsistência.
  - **Mitigação:** schemas rígidos + lint + testes de referência.
- **Risco:** UI acoplada ao core.
  - **Mitigação:** contratos de eventos/snapshots estáveis.

---

## Próximo passo prático (o que eu faria já)
1. Abrir uma branch de “core extraction”.
2. Migrar primeiro o combate para `rpg/core/combat` com API pura.
3. Criar snapshots/eventos para o turno.
4. Subir protótipo de UI (web ou Qt) só para combate e inventário.
5. Depois migrar criação de personagem e quests.

Se você quiser, no próximo passo eu já preparo um **esqueleto técnico inicial** (estrutura de pastas + interfaces + primeiro fluxo do combate) para começarmos a execução de verdade.
