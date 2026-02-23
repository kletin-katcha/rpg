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


### Fase 10 — Benefícios de facção e recompensas de reputação
- Reputação agora desbloqueia benefícios resgatáveis por facção
- Benefícios impactam economia (ouro/itens) no loop principal
- Ação dedicada para resgate no menu de cidade
- Fase 10 concluída: reputação virou moeda de progressão contínua.


### Fase 11 — Contratos ramificados e reputação dinâmica
- Contratos classificados por tier (bronze/prata/ouro/lendário)
- Falha de contrato gera reputação negativa por facção
- Perks de facção passam a escalar por tier de reputação
- Fase 11 concluída: loop de contrato ganhou risco/recompensa real e progressão reputacional bidirecional.


### Fase 12 — Combate avançado e chefes multi-fase
- Iniciativa por velocidade/destreza no turno de combate
- Arquétipos de inimigo (agressivo/defensivo/venenoso/boss)
- Boss com transição de fase durante a luta
- Fase 12 concluída: combate ganhou profundidade tática sem quebrar o loop atual.


### Fase 13 — Economia dinâmica e cadeia de produção
- Mercado com multiplicadores dinâmicos por dia
- Venda de itens convertendo inventário em ouro com preço variável
- Cadeia produtiva avançada (`barra_metal` -> `liga_metal`)
- Fase 13 concluída: economia ganhou variação temporal e novo loop de produção.


### Fase 14 — Imersão sistêmica (tempo, clima e narrativa local)
- Ciclo temporal com períodos do dia no loop principal
- Clima dinâmico acoplado ao avanço de tempo
- Jornal da cidade para histórico diegético recente
- Codex desbloqueável por eventos do mundo
- Fase 14 concluída: base de imersão narrativa integrada ao gameplay.


### Fase 15 — Diretor de Mundo e procedural avançado
- Gerador de arcos de mundo com base em reputação, clima e período do dia
- Mutadores de mundo que alteram mercado dinamicamente
- Memória emergente por facção a partir das decisões do jogador
- Fase 15 concluída: núcleo procedural e memória sistêmica integrados ao loop.


### Fase 16 — Plataforma para conteúdo massivo e compatibilidade de branches
- Validação de referências cruzadas entre catálogos (itens, facções, receitas, planos, loot)
- Pipeline local estendida com etapa de referência semântica
- Shims de compatibilidade para caminhos legados (reduz conflitos de merge no GitHub)
- Fase 16 concluída: base preparada para expansão massiva de conteúdo com menor risco operacional.


### Fase 17 — Combate situacional e condições ambientais
- Mutadores de combate conectados ao período do dia, clima e mutador global do diretor de mundo
- Contexto de combate expandido com bônus/reduções aplicados a cada turno
- Nova ação de inspeção (`ver_condicoes_combate`) para leitura rápida dos modificadores ativos
- Fase 17 concluída: combate mais reativo ao estado sistêmico do mundo sem quebrar compatibilidade.


### Fase 18 — Cadeias de contratos narrativos
- Geração de cadeia de contratos (mini-campanha) com múltiplas etapas
- Progresso rastreável por etapa e inspeção via comando no loop
- Avanço automático para o próximo contrato após conclusão
- Falha em contrato da cadeia encerra o arco em andamento
- Fase 18 concluída: contratos ganharam continuidade narrativa e sensação de campanha.


### Fase 19 — Tensão dinâmica entre facções
- Avaliação sistêmica da rivalidade entre as facções mais influentes
- Estado de tensão com três níveis (`conflito`, `competicao`, `hegemonia`)
- Impacto urbano imediato via ajuste de ouro da cidade
- Novas ações de inspeção e atualização (`gerar_tensao_faccoes`, `ver_tensao_faccoes`)
- Fase 19 concluída: reputação agora afeta o estado político-econômico local.


### Fase 20 — Crises urbanas sistêmicas
- Geração de crise urbana baseada em tensão de facções e condição climática
- Crises com impacto econômico imediato na cidade
- Registro diegético no jornal para reforçar continuidade narrativa
- Novas ações de controle e inspeção (`gerar_crise_urbana`, `ver_crise_urbana`)
- Fase 20 concluída: o mundo urbano reage a política + clima de forma tangível.


### Fase 21 — Regiões e viagem
- Múltiplas regiões exploráveis com custo de energia
- Descoberta persistente de áreas visitadas
- Fase 21 concluída: exploração geográfica entrou no loop principal.

### Fase 22 — Dungeons procedurais leves
- Geração de dungeon por dia/região
- Exploração com risco/recompensa no loop de cidade
- Fase 22 concluída: conteúdo repetível com variação controlada.

### Fase 23 — Agenda autônoma de facções
- Tick de agenda por facção com variações de reputação
- Histórico de eventos faccionais para inspeção
- Fase 23 concluída: o mundo político evolui entre decisões do jogador.

### Fase 24 — Arcos narrativos multi-ato
- Arco longo inicializável e progressão por atos
- Estado de campanha observável durante a run
- Fase 24 concluída: narrativa de campanha ganhou continuidade formal.

### Fase 25 — Ferramentas de expansão massiva
- Gerador de pacotes mock para produção de conteúdo em lote
- Simulação headless para leitura rápida de balanceamento
- Gate de qualidade adicional: auditoria automática `scripts/auditar_fases.py` com trilha 1→25 e teste end-to-end.
- Instrumentação runtime: ação `diagnostico_fases_1_25` para inspeção rápida da cobertura funcional por marcos.
- Fase 25 concluída: base pronta para escalar conteúdo de forma industrial.
