# Contratos do Núcleo — RPG Surreal

Este documento define contratos mínimos entre domínios. A meta é permitir expansão massiva sem acoplamento implícito.

## Entidades de domínio (MVP)

### Personagem
Campos obrigatórios:
- `id: str`
- `nome: str`
- `nivel: int`
- `xp: int`
- `atributos: dict[str, int]`
- `hp_atual: int`
- `hp_max: int`

### Inimigo
Campos obrigatórios:
- `id: str`
- `nome: str`
- `nivel: int`
- `hp_atual: int`
- `hp_max: int`
- `ataque_base: int`

### Item
Campos obrigatórios:
- `id: str`
- `nome: str`
- `tipo: str`
- `valor: int`

## Contratos de serviços

### Combate
- `resolver_turno(contexto: CombatContext) -> CombatResult`

### Inventário
- `adicionar_item(inventario: dict[str, int], item_id: str, qtd: int = 1) -> dict[str, int]`
- `remover_item(inventario: dict[str, int], item_id: str, qtd: int = 1) -> dict[str, int]`

### Progressão
- `conceder_xp(personagem: CharacterState, xp: int) -> CharacterState`

## Regras técnicas
- Serviços de um domínio não devem chamar `rules.py` de outro domínio diretamente.
- Qualquer integração cross-domínio deve passar por APIs públicas (service layer).
- Quebras de contrato exigem atualização dos testes em `tests/contracts/`.
