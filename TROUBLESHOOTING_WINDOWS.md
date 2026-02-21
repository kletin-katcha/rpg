# Troubleshooting Windows

## Erro ao rodar módulo
Use sempre na raiz do projeto:

```powershell
python -m rpg.main
```

## Limpar cache
```powershell
Get-ChildItem -Recurse -Directory __pycache__ | Remove-Item -Recurse -Force
```
