# -*- coding: utf-8 -*-
"""
================================================================================================
SISTEMA: GERENCIADOR DE SAVE/LOAD
================================================================================================
Este arquivo define o `GerenciadorSave`, a espinha dorsal da persistência de dados em
Aetheria. Ele é responsável por serializar o estado completo do jogo em um arquivo
JSON e por desserializá-lo para restaurar uma sessão de jogo.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Serialização em JSON:** O estado do jogo é salvo em formato JSON, que é legível
  por humanos e facilmente portável.

- **Encoder/Decoder Customizado:** O desafio de salvar um jogo é que objetos de classes
  customizadas (como `Personagem`) não são serializáveis em JSON por padrão. Para
  resolver isso de forma elegante e escalável, este módulo implementa um `JSONEncoder`
  customizado e um `object_hook` para o decoder.
    - `EstadoJogoEncoder`: Converte objetos (`Personagem`, `datetime`, etc.) em
      dicionários. Ele adiciona uma chave `__class__` para que o decoder saiba qual
      classe reconstruir.
    - `estado_jogo_decoder`: O `object_hook` que é chamado pelo `json.load`. Ele
      verifica a presença da chave `__class__` e usa um mapa para chamar o
      construtor da classe correta, recriando o objeto a partir do dicionário.

- **Estrutura do Save:** O save é encapsulado em um objeto `EstadoJogo`, que atua
  como um contêiner para todas as informações relevantes: o personagem do jogador,
  o estado do mundo (eventos concluídos, etc.) e metadados como a data do save.

- **Gerenciamento de Slots:** O `GerenciadorSave` pode lidar com múltiplos "slots"
  de save, permitindo que o jogador mantenha várias jornadas diferentes.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
from typing import Dict, Any, List
import json
import os
import sys
from datetime import datetime

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    from motor_jogo.entidades.personagem import Personagem
    from motor_jogo.entidades.monstro import Monstro
except ImportError:
    # Mocks para permitir a execução independente
    class Personagem:
        def __init__(self, **kwargs):
            for key, value in kwargs.items(): setattr(self, key, value)
    class Monstro:
        def __init__(self, **kwargs):
            for key, value in kwargs.items(): setattr(self, key, value)

# ==============================================================================================
# == SEÇÃO 2: ESTRUTURAS DE DADOS E CLASSES DE ESTADO ==========================================
# ==============================================================================================
class EstadoJogo:
    """
    Um contêiner para todo o estado do jogo que precisa ser salvo.
    """
    def __init__(self, personagem: Personagem, estado_mundo: Dict, metadata: Dict, monstros_na_area: List = []):
        self.personagem = personagem
        self.estado_mundo = estado_mundo
        self.metadata = metadata
        self.monstros_na_area = monstros_na_area

    def to_dict(self):
        """Converte o objeto para um dicionário para serialização."""
        return {
            "__class__": "EstadoJogo",
            "personagem": self.personagem,
            "estado_mundo": self.estado_mundo,
            "metadata": self.metadata,
            "monstros_na_area": self.monstros_na_area,
        }

# ==============================================================================================
# == SEÇÃO 3: LÓGICA DE SERIALIZAÇÃO/DESERIALIZAÇÃO (ENCODER/DECODER) ===========================
# ==============================================================================================
class EstadoJogoEncoder(json.JSONEncoder):
    """
    Encoder JSON customizado para lidar com objetos do jogo.
    """
    def default(self, obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        if isinstance(obj, (Personagem, Monstro)):
            # Adiciona a chave de classe e converte o objeto em um dicionário
            data = obj.__dict__
            data["__class__"] = obj.__class__.__name__
            return data
        if isinstance(obj, datetime):
            return {"__class__": "datetime", "isoformat": obj.isoformat()}
        return super().default(obj)

def estado_jogo_decoder(obj_dict: Dict) -> Any:
    """
    Object hook para o decoder JSON. Reconstrói objetos customizados.
    """
    if "__class__" in obj_dict:
        class_name = obj_dict.pop("__class__")

        # Mapa de classes para reconstrução
        class_map = {
            "EstadoJogo": EstadoJogo,
            "Personagem": Personagem,
            "Monstro": Monstro,
        }

        if class_name == "datetime":
            return datetime.fromisoformat(obj_dict["isoformat"])

        cls = class_map.get(class_name)
        if cls:
            # Classes de Entidade (Personagem, Monstro) têm construtores que não aceitam
            # todos os atributos de estado, então precisam de uma lógica de reconstrução especial.
            if class_name == "Personagem":
                init_args = {"id_entidade": obj_dict.pop("id_entidade"), "nome": obj_dict.pop("nome"), "dados_raca": obj_dict.pop("raca"), "dados_classe": obj_dict.pop("classe")}
                obj = Personagem(**init_args)
                for key, value in obj_dict.items(): setattr(obj, key, value)
                return obj

            elif class_name == "Monstro":
                # O construtor do Monstro espera um único dict `dados_monstro`.
                # Para restaurar o estado (como hp_atual), criamos com o dict salvo
                # e depois sobrescrevemos os valores de estado.
                obj = Monstro(dados_monstro=obj_dict)
                for key, value in obj_dict.items(): setattr(obj, key, value)
                return obj

            else:
                # Outras classes (como EstadoJogo) podem ser reconstruídas diretamente
                return cls(**obj_dict)
    return obj_dict

# ==============================================================================================
# == SEÇÃO 4: CLASSE GERENCIADOR DE SAVE =======================================================
# ==============================================================================================
class GerenciadorSave:
    """
    Gerencia as operações de salvar e carregar o estado do jogo.
    """
    def __init__(self, diretorio_saves: str = "./saves/"):
        self.diretorio_saves = diretorio_saves
        if not os.path.exists(self.diretorio_saves):
            os.makedirs(self.diretorio_saves)

    def _caminho_do_slot(self, slot: int) -> str:
        """Retorna o caminho completo do arquivo para um determinado slot."""
        return os.path.join(self.diretorio_saves, f"save_slot_{slot}.json")

    def salvar_jogo(self, estado_jogo: EstadoJogo, slot: int) -> bool:
        """
        Salva o estado do jogo em um arquivo JSON em um slot específico.

        Args:
            estado_jogo (EstadoJogo): O objeto contendo o estado atual do jogo.
            slot (int): O número do slot de save (ex: 1, 2, 3).

        Returns:
            bool: True se o jogo foi salvo com sucesso, False caso contrário.
        """
        caminho_arquivo = self._caminho_do_slot(slot)
        print(f"Salvando jogo no slot {slot} em '{caminho_arquivo}'...")
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump(estado_jogo, f, cls=EstadoJogoEncoder, indent=4, ensure_ascii=False)
            print("Jogo salvo com sucesso!")
            return True
        except (IOError, TypeError) as e:
            print(f"Erro ao salvar o jogo: {e}", file=sys.stderr)
            return False

    def carregar_jogo(self, slot: int) -> EstadoJogo | None:
        """
        Carrega o estado do jogo de um arquivo JSON de um slot específico.

        Args:
            slot (int): O número do slot de save a ser carregado.

        Returns:
            EstadoJogo | None: O objeto de estado do jogo reconstruído, ou None se
                                o arquivo não existir ou ocorrer um erro.
        """
        caminho_arquivo = self._caminho_do_slot(slot)
        if not os.path.exists(caminho_arquivo):
            print(f"Nenhum save encontrado no slot {slot}.")
            return None

        print(f"Carregando jogo do slot {slot} de '{caminho_arquivo}'...")
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                estado_carregado = json.load(f, object_hook=estado_jogo_decoder)
            print("Jogo carregado com sucesso!")
            return estado_carregado
        except (IOError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar o jogo: {e}", file=sys.stderr)
            return None

    def listar_saves(self) -> List[Dict]:
        """
        Lista os saves existentes e retorna seus metadados.
        """
        saves_encontrados = []
        for i in range(1, 11): # Procura por slots de 1 a 10
            caminho_arquivo = self._caminho_do_slot(i)
            if os.path.exists(caminho_arquivo):
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                       # Carrega apenas o suficiente para obter os metadados
                       dados = json.load(f)
                       metadata = dados.get("metadata", {})
                       metadata["slot"] = i
                       saves_encontrados.append(metadata)
                except (IOError, json.JSONDecodeError):
                    continue
        return saves_encontrados

    def apagar_save(self, slot: int) -> bool:
        """
        Apaga um arquivo de save de um slot específico.

        Args:
            slot (int): O número do slot de save a ser apagado.

        Returns:
            bool: True se o arquivo foi apagado com sucesso, False caso contrário.
        """
        caminho_arquivo = self._caminho_do_slot(slot)
        if not os.path.exists(caminho_arquivo):
            print(f"Nenhum save encontrado no slot {slot} para apagar.")
            return False

        try:
            os.remove(caminho_arquivo)
            print(f"Arquivo de save do slot {slot} apagado com sucesso.")
            return True
        except OSError as e:
            print(f"Erro ao apagar o arquivo de save: {e}", file=sys.stderr)
            return False

# ==============================================================================================
# == SEÇÃO 5: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO GERENCIADOR DE SAVE/LOAD ==")
    print("="*80)

    # --- Setup do Teste ---
    TEST_SAVE_DIR = "./test_saves/"
    TEST_SLOT = 1

    # Mock de dados para instanciar a classe Personagem real
    DADOS_RACA_MOCK = {"id": "humano_teste", "nome": "Humano de Teste", "atributos_base": {"constituicao": 10}}
    DADOS_CLASSE_MOCK = {"id_classe": "viajante_teste", "nome": "Viajante de Teste", "habilidades_iniciais": []}

    # Instancia o personagem da forma correta
    personagem_original = Personagem(
        id_entidade="valerius_01",
        nome="Valerius, o Viajante",
        dados_raca=DADOS_RACA_MOCK,
        dados_classe=DADOS_CLASSE_MOCK
    )
    # Define manualmente os atributos para o estado que queremos testar
    personagem_original.nivel = 25
    personagem_original.xp_atual = 1234
    personagem_original.atributos = {"forca": 50, "destreza": 35}
    personagem_original.inventario = [{"nome": "Espada Lendária"}, {"nome": "Poção de Cura", "quantidade": 5}]
    personagem_original.habilidades_conhecidas = ["Ataque Poderoso", "Defesa Impenetrável"]

    # Mock do Estado do Jogo
    estado_original = EstadoJogo(
        personagem=personagem_original,
        estado_mundo={"chefes_derrotados": ["goblin_king"], "fases_lua": "cheia"},
        metadata={"timestamp": datetime.now(), "tempo_de_jogo_segundos": 3600}
    )

    # --- 1. Salvar o Jogo ---
    print("\n--- Etapa 1: Salvando o estado do jogo ---")
    gerenciador = GerenciadorSave(diretorio_saves=TEST_SAVE_DIR)
    sucesso_save = gerenciador.salvar_jogo(estado_original, TEST_SLOT)
    assert sucesso_save, "Falha ao salvar o jogo."
    assert os.path.exists(gerenciador._caminho_do_slot(TEST_SLOT)), "Arquivo de save não foi criado."

    # --- 2. Carregar o Jogo ---
    print("\n--- Etapa 2: Carregando o estado do jogo ---")
    estado_carregado = gerenciador.carregar_jogo(TEST_SLOT)
    assert estado_carregado is not None, "Falha ao carregar o jogo."

    # --- 3. Verificação de Integridade ---
    print("\n--- Etapa 3: Verificando a integridade dos dados carregados ---")

    # Verifica se os objetos foram reconstruídos corretamente
    assert isinstance(estado_carregado, EstadoJogo), "O objeto raiz não é EstadoJogo."
    assert isinstance(estado_carregado.personagem, Personagem), "O personagem não é da classe Personagem."
    assert isinstance(estado_carregado.metadata["timestamp"], datetime), "O timestamp não foi reconstruído como datetime."

    # Verifica os dados do personagem
    p_original = estado_original.personagem
    p_carregado = estado_carregado.personagem
    assert p_carregado.nome == p_original.nome, "O nome do personagem não corresponde."
    assert p_carregado.nivel == p_original.nivel, "O nível do personagem não corresponde."
    assert len(p_carregado.inventario) == len(p_original.inventario), "O inventário não corresponde."
    assert p_carregado.inventario[1]["quantidade"] == 5, "Dados do inventário estão incorretos."

    # Verifica o estado do mundo
    assert estado_carregado.estado_mundo["chefes_derrotados"][0] == "goblin_king", "O estado do mundo não corresponde."

    print("Verificação de integridade concluída com sucesso. Os dados foram salvos e carregados perfeitamente.")

    # --- Limpeza ---
    print("\n--- Limpando ambiente de teste ---")
    if os.path.exists(gerenciador._caminho_do_slot(TEST_SLOT)):
        os.remove(gerenciador._caminho_do_slot(TEST_SLOT))
    if os.path.exists(TEST_SAVE_DIR):
        os.rmdir(TEST_SAVE_DIR)
    print("Diretório e arquivo de save de teste removidos.")

    print("\n\nTeste concluído com sucesso! O sistema de save/load está funcionando.")
