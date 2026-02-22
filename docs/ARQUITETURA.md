# Arquitetura Inicial

## Camadas

- `rpg.main`: entrypoint
- `rpg.game`: orquestração de fluxo
- `rpg.entidades`: modelos de domínio
- `rpg.sistemas`: regras de negócio
- `rpg.dados`: catálogos estáticos

## Princípios

- separar dados de lógica
- minimizar imports circulares
- APIs pequenas e explícitas
