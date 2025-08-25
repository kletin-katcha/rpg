import json
import os
from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

SAVE_DIR = "saves"

def garantir_diretorio_saves():
    """Garante que o diretório de saves exista."""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def salvar_jogo(personagem: 'Personagem', nome_arquivo: str):
    """
    Salva o estado do jogo em um arquivo JSON.
    Isso requer um método to_dict() na classe Personagem.
    """
    garantir_diretorio_saves()
    caminho_arquivo = os.path.join(SAVE_DIR, f"{nome_arquivo}.json")

    try:
        # TODO: Implementar um método to_dict() na classe Personagem
        # que converte o objeto e seus sub-objetos em um dicionário.

        # Placeholder simples por enquanto:
        dados_save = {
            "nome": personagem.nome,
            "nivel": personagem.nivel,
            "xp_atual": personagem.xp_atual,
            "ouro": personagem.ouro,
            "hp_atual": personagem.hp_atual,
            "mp_atual": personagem.mp_atual,
            "forca": personagem.forca,
            "destreza": personagem.destreza,
            "constituicao": personagem.constituicao,
            "inteligencia": personagem.inteligencia,
            "sabedoria": personagem.sabedoria,
            "carisma": personagem.carisma,
            # Inventário, quests, etc, precisarão de serialização mais complexa
        }

        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_save, f, indent=4, ensure_ascii=False)
        print(f"\nJogo salvo com sucesso em '{caminho_arquivo}'!")

    except Exception as e:
        print(f"\nOcorreu um erro ao salvar o jogo: {e}")

def carregar_jogo(nome_arquivo: str) -> 'Personagem':
    """
    Carrega o estado do jogo de um arquivo JSON.
    Isso requer um método from_dict() ou lógica de reconstrução.
    """
    caminho_arquivo = os.path.join(SAVE_DIR, f"{nome_arquivo}.json")

    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo de save '{nome_arquivo}' não encontrado.")
        return None

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_carregados = json.load(f)

        # TODO: Implementar lógica para reconstruir o objeto Personagem
        # a partir do dicionário carregado.

        # Placeholder simples por enquanto:
        from ..entidades.personagem import Personagem
        personagem = Personagem(nome=dados_carregados["nome"], nivel=dados_carregados["nivel"])
        personagem.xp_atual = dados_carregados["xp_atual"]
        personagem.ouro = dados_carregados["ouro"]
        personagem.hp_atual = dados_carregados["hp_atual"]
        personagem.mp_atual = dados_carregados["mp_atual"]
        personagem.forca = dados_carregados["forca"]
        personagem.destreza = dados_carregados["destreza"]
        personagem.constituicao = dados_carregados["constituicao"]
        personagem.inteligencia = dados_carregados["inteligencia"]
        personagem.sabedoria = dados_carregados["sabedoria"]
        personagem.carisma = dados_carregados["carisma"]

        personagem.recalcular_stats_completos() # Recalcula HP/MP max e outros stats

        print(f"\nJogo '{nome_arquivo}' carregado com sucesso!")
        return personagem

    except Exception as e:
        print(f"\nOcorreu um erro ao carregar o jogo: {e}")
        return None

def listar_saves() -> list:
    """Retorna uma lista dos arquivos de save existentes."""
    garantir_diretorio_saves()
    saves = [f.replace(".json", "") for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    return saves
