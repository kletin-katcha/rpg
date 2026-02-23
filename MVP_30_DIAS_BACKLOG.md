# MVP 30 dias — Início de produção (decisões consolidadas)

Este documento converte as decisões mais recentes em um plano executável para começar a codar imediatamente.

## Decisões fechadas
- Plataforma: **Híbrida** (Web beta primeiro, Desktop depois).
- Prioridade atual: **Jogabilidade + Conteúdo**.
- Combate do MVP: **Turno tático** (tempo real fica para fase posterior).
- Metalurgia do MVP: **mínimo viável (placeholder funcional)**.
- Escopo do MVP: combate + progressão + exploração + 1 cidade.
- Visão de conteúdo (longo prazo): muitas raças/sub-raças, classes (incluindo secundárias, secretas e únicas por raça).

## Regra de escopo (solo dev)
Para viabilizar 30 dias sem travar o projeto:
- Implementar **sistema escalável** para suportar muitas raças/classes.
- Entregar no MVP apenas um **recorte inicial de conteúdo**.
- Expandir conteúdo em ondas sem refatorar o núcleo.

---

## Entregáveis obrigatórios do MVP

## 1) Núcleo de Combate (turno tático)
- Ações: ataque básico, defender, habilidade, item, fugir.
- Recursos: HP, MP, stamina.
- Efeitos: buff/debuff simples com duração por turno.
- IA inicial de inimigo com 2 perfis (agressivo e suporte).

## 2) Progressão inicial
- Raça/sub-raça aplicando bônus e habilidades passivas.
- Classe inicial aplicando habilidades ativas e equipamento inicial.
- XP + nível + ganho básico de atributos.

## 3) Exploração + 1 cidade hub
- Cidade com menu funcional (quests, inventário, equipamento, status, sair para exploração).
- 1 área de exploração com encontros aleatórios.
- 1 mini-boss de marco para validar progressão.

## 4) Inventário/equipamento
- Empilhamento de itens, equipar/desequipar, consumo.
- Persistência simples de save/load para ciclo de testes.

## 5) Magia e Metalurgia (versão mínima)
- Magia: 1 escola inicial ou 3 feitiços-base (dano, cura, buff).
- Metalurgia: loop mínimo (coletar recurso -> fundir -> gerar 1 item útil).

---

## Alvos de conteúdo no MVP (recorte mínimo)
> Observação: a visão final é “muitas raças e classes”. Aqui é apenas o recorte inicial.

- Raças: **3**
- Sub-raças: **1 por raça** (3 no total)
- Classes iniciais: **3**
- Classe secundária: **1 protótipo via quest**
- Classe secreta: **1 protótipo**
- Classe única de raça: **1 protótipo**

Total de foco: provar o sistema de diversidade sem tentar preencher todo o conteúdo final no primeiro mês.

---

## Backlog por semana (30 dias)

## Semana 1 — Fundação jogável
- Fechar contrato de dados para raça/sub-raça/classe/habilidade.
- Garantir loop de combate estável com logs claros.
- Criar testes para cálculo de dano, custo de recurso e duração de efeito.
- Entregar 1 inimigo comum + 1 elite.

**DoD semana 1**
- Combate completo roda sem travar por 20 turnos simulados.
- Testes de combate passando no CI local.

## Semana 2 — Progressão + conteúdo base
- Implementar fluxo completo: criar personagem -> raça/sub-raça -> classe -> atributos.
- Integrar habilidades iniciais por classe.
- Balanceamento inicial de XP e recompensa.
- Adicionar 3 raças, 3 sub-raças, 3 classes iniciais.

**DoD semana 2**
- Jogador cria personagem e vence 3 combates seguidos sem bug de estado.

## Semana 3 — Cidade + exploração + mini-boss
- Construir cidade hub com opções essenciais.
- Implementar área de exploração com eventos/encontros.
- Inserir 1 mini-boss com mecânica diferente (ex.: buff próprio).
- Quest de desbloqueio de classe secundária (protótipo).

**DoD semana 3**
- Loop completo: cidade -> exploração -> combate -> recompensa -> retorno.

## Semana 4 — Sistemas mínimos extras + polimento
- Magia mínima (3 feitiços base) e metalurgia placeholder.
- Protótipo de classe secreta e classe única racial.
- Balanceamento de stamina/MP/curva de dano.
- Revisão de UX textual (mensagens, clareza de decisão e feedback).

**DoD semana 4 (MVP pronto)**
- Jogo completo em ciclo curto de 30–45 min sem bloqueios.
- Save/load funcional.
- Testes essenciais passando.

---

## Métricas de sucesso do MVP
- Taxa de erro em combate: < 2% de ações inválidas por sessão.
- Tempo médio de turno: < 10 segundos no cliente textual.
- Progressão percebida: jogador sobe pelo menos 2 níveis por sessão curta.
- Clareza: usuário entende diferenças entre raça/sub-raça/classe sem documentação externa.

---

## Pós-MVP (ordem recomendada)
1. Expandir conteúdo (ondas): +raças, +sub-raças, +classes.
2. Metalurgia completa (ligas, tiers, cadeia de produção).
3. Árvore de habilidades maior (constelações por arquétipo).
4. Beta web com interface visual moderna.
5. Cliente desktop definitivo com foco em performance e UX final.

---

## Princípio de produção
**Escalar por sistema primeiro, por volume depois.**
Ou seja: construir uma base que suporte 100+ variações, mas lançar poucas variações inicialmente para garantir qualidade e velocidade de entrega.
