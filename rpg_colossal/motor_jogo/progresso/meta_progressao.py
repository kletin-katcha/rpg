# -*- coding: utf-8 -*-
"""
================================================================================================
MOTOR DE PROGRESSÃO: META PROGRESSÃO E LEGADO
================================================================================================
Este arquivo define o `GerenciadorDeMetaProgressao`, um sistema que gerencia
conquistas e bônus que persistem entre diferentes personagens e sessões de jogo.
Ele cria um senso de legado, onde as ações de um herói ecoam para os próximos.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Persistência Externa:** Ao contrário de outros sistemas que operam apenas na
  memória durante o jogo, este gerenciador lê e escreve seu estado em um arquivo
  externo (ex: `meta_save.json`). Isso garante que as conquistas sejam permanentes.

- **Conquistas como Gatilhos:** O sistema funciona com base em um banco de dados de
  conquistas (`CONQUISTAS_MUNDO`). Cada conquista tem um `gatilho` específico (ex:
  derrotar um chefe, atingir um marco de reputação). O jogo notifica o gerenciador
  sobre eventos importantes, e o gerenciador verifica se algum gatilho foi ativado.

- **Bônus de Legado:** Ao desbloquear uma conquista, o jogador pode ganhar um
  "Bônus de Legado". Esses bônus são aplicados a *todos os novos personagens*
  criados subsequentemente. Exemplos incluem:
    - Um item inicial extra.
    - Um pequeno bônus permanente de atributos.
    - Um aumento na taxa de ganho de XP ou ouro.

- **Ciclo de Vida:**
  1. No início do jogo, o `GerenciadorDeMetaProgressao` é instanciado e carrega o
     arquivo `meta_save.json`.
  2. Durante o jogo, outros sistemas (combate, missões) notificam o gerenciador
     sobre eventos (`registrar_evento`).
  3. Se um evento desbloqueia uma conquista, o estado do gerenciador é atualizado e
     salvo de volta no arquivo.
  4. Ao criar um novo personagem, o método `aplicar_bonus_de_legado` é chamado
     para conceder a ele os benefícios de todas as conquistas já desbloqueadas.
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
except ImportError:
    Personagem = object

# ==============================================================================================
# == SEÇÃO 2: BANCO DE DADOS DE CONQUISTAS =====================================================
# ==============================================================================================
CONQUISTAS_MUNDO: Dict[str, Dict] = {
    "matador_do_rei_demonio": {
        "id": "matador_do_rei_demonio",
        "nome": "Matador do Rei Demônio",
        "descricao": "Você derrotou o Rei Demônio e salvou Aetheria da escuridão.",
        "gatilho": {"tipo": "chefe_derrotado", "id_chefe": "boss_rei_dos_demonios"},
        "bonus_legado": {
            "tipo": "item_inicial",
            "id_item": "fragmento_de_coragem",
            "dados_item": {"nome": "Fragmento de Coragem", "tipo": "amuleto", "bonus": {"forca": 1}}
        }
    },
    "mestre_da_arena": {
        "id": "mestre_da_arena",
        "nome": "Mestre da Arena",
        "descricao": "Você alcançou o rank máximo na Grande Arena.",
        "gatilho": {"tipo": "rank_arena", "rank": "mestre"},
        "bonus_legado": {
            "tipo": "boost_permanente",
            "boost": {"ganho_xp_percentual": 5} # 5% a mais de XP para sempre
        }
    }
}

# ==============================================================================================
# == SEÇÃO 3: CLASSE GERENCIADOR DE META PROGRESSÃO ============================================
# ==============================================================================================
class GerenciadorDeMetaProgressao:
    """
    Gerencia conquistas e bônus de legado persistentes.
    """
    def __init__(self, caminho_save: str = "meta_save.json"):
        """
        Inicializa o gerenciador, carregando o progresso meta de um arquivo.

        Args:
            caminho_save (str): O caminho para o arquivo de save da meta progressão.
        """
        self.caminho_save = caminho_save
        self.progresso = self._carregar_meta_save()

    def _carregar_meta_save(self) -> Dict:
        """Carrega o arquivo de save. Se não existir, cria um estado padrão."""
        if os.path.exists(self.caminho_save):
            try:
                with open(self.caminho_save, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print(f"Aviso: Não foi possível ler '{self.caminho_save}'. Um novo será criado.")
        return {"conquistas_desbloqueadas": {}}

    def _salvar_meta_save(self):
        """Salva o estado atual do progresso no arquivo."""
        try:
            with open(self.caminho_save, 'w') as f:
                json.dump(self.progresso, f, indent=4)
        except IOError:
            print(f"Erro: Não foi possível salvar o progresso em '{self.caminho_save}'.")

    def registrar_evento(self, tipo_evento: str, dados_evento: Dict):
        """
        Recebe notificações de eventos do jogo e verifica se alguma conquista foi desbloqueada.
        """
        print(f"Evento registrado: {tipo_evento}, Dados: {dados_evento}")
        for id_conquista, conquista in CONQUISTAS_MUNDO.items():
            # Evita tentar desbloquear uma conquista que já foi ganha
            if id_conquista in self.progresso["conquistas_desbloqueadas"]:
                continue

            gatilho = conquista["gatilho"]
            if gatilho["tipo"] == tipo_evento and all(dados_evento.get(k) == v for k, v in gatilho.items() if k != "tipo"):
                self._desbloquear_conquista(conquista)

    def _desbloquear_conquista(self, conquista: Dict):
        """Marca uma conquista como desbloqueada e salva o progresso."""
        id_conquista = conquista["id"]
        print("-" * 50)
        print(f"** CONQUISTA DE LEGADO DESBLOQUEADA: {conquista['nome']} **")
        print(f"Descrição: {conquista['descricao']}")
        print("-" * 50)

        self.progresso["conquistas_desbloqueadas"][id_conquista] = {
            "timestamp": datetime.utcnow().isoformat()
        }
        self._salvar_meta_save()

    def aplicar_bonus_de_legado(self, novo_personagem: Personagem):
        """
        Aplica todos os bônus de legado desbloqueados a um novo personagem.
        Este método deve ser chamado durante a criação do personagem.
        """
        print(f"\n--- Aplicando Bônus de Legado para {novo_personagem.nome} ---")
        if not self.progresso["conquistas_desbloqueadas"]:
            print("Nenhum bônus de legado para aplicar.")
            return

        for id_conquista in self.progresso["conquistas_desbloqueadas"]:
            conquista = CONQUISTAS_MUNDO.get(id_conquista)
            if not conquista or "bonus_legado" not in conquista:
                continue

            bonus = conquista["bonus_legado"]
            print(f"Aplicando bônus da conquista '{conquista['nome']}':")

            if bonus["tipo"] == "item_inicial":
                # Assumindo que o personagem tem um método `adicionar_item`
                if hasattr(novo_personagem, 'adicionar_item'):
                    novo_personagem.adicionar_item(bonus["dados_item"])
                    print(f"  - Item '{bonus['dados_item']['nome']}' adicionado ao inventário.")

            elif bonus["tipo"] == "boost_permanente":
                 # Assumindo que o personagem tem um dicionário para guardar boosts
                if hasattr(novo_personagem, 'boosts_legado'):
                    novo_personagem.boosts_legado.update(bonus['boost'])
                    print(f"  - Boosts permanentes aplicados: {bonus['boost']}")

# ==============================================================================================
# == SEÇÃO 4: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print("== DEMONSTRAÇÃO DO GERENCIADOR DE META PROGRESSÃO ==")
    print("="*80)

    # --- Setup do Teste ---
    CAMINHO_TESTE_SAVE = "test_meta_save.json"

    # Garante que não há um arquivo de save antigo antes de começar
    if os.path.exists(CAMINHO_TESTE_SAVE):
        os.remove(CAMINHO_TESTE_SAVE)

    class MockPersonagemMeta:
        def __init__(self, nome):
            self.nome = nome
            self.inventario = []
            self.boosts_legado = {}
        def adicionar_item(self, item):
            self.inventario.append(item)

    # --- 1. Primeiro Personagem: O Herói ---
    print("\n--- Etapa 1: A Jornada do Primeiro Herói ---")
    gerenciador = GerenciadorDeMetaProgressao(caminho_save=CAMINHO_TESTE_SAVE)

    # Simula o herói derrotando o chefe final
    print("\nO herói derrota o Rei Demônio...")
    gerenciador.registrar_evento("chefe_derrotado", {"id_chefe": "boss_rei_dos_demonios"})

    # Verifica se o save foi criado e contém a conquista
    assert os.path.exists(CAMINHO_TESTE_SAVE)
    with open(CAMINHO_TESTE_SAVE, 'r') as f:
        dados_salvos = json.load(f)
    assert "matador_do_rei_demonio" in dados_salvos["conquistas_desbloqueadas"]
    print("Progresso da conquista salvo com sucesso!")

    # --- 2. Segundo Personagem: O Herdeiro ---
    print("\n\n--- Etapa 2: A Jornada do Herdeiro do Legado ---")
    herdeiro = MockPersonagemMeta("Lia, a Herdeira")

    # O gerenciador é instanciado novamente, carregando o save existente
    gerenciador_para_herdeiro = GerenciadorDeMetaProgressao(caminho_save=CAMINHO_TESTE_SAVE)

    # Aplica os bônus ao novo personagem
    gerenciador_para_herdeiro.aplicar_bonus_de_legado(herdeiro)

    # Verifica se o herdeiro recebeu o item de legado
    assert len(herdeiro.inventario) == 1
    assert herdeiro.inventario[0]["nome"] == "Fragmento de Coragem"
    print(f"\nInventário do Herdeiro: {[item['nome'] for item in herdeiro.inventario]}")

    print("\n\n--- Etapa 3: Tentativa de Desbloqueio Duplicado ---")
    print("O herdeiro também derrota o Rei Demônio...")
    gerenciador_para_herdeiro.registrar_evento("chefe_derrotado", {"id_chefe": "boss_rei_dos_demonios"})
    # A verificação aqui é que o print de "CONQUISTA DESBLOQUEADA" não deve aparecer de novo.
    # O teste passará se não houver erros e a lógica de prevenção funcionar.

    # --- Limpeza ---
    print("\n--- Limpando ambiente de teste ---")
    if os.path.exists(CAMINHO_TESTE_SAVE):
        os.remove(CAMINHO_TESTE_SAVE)
    print("Arquivo de save de teste removido.")

    print("\n\nTeste concluído com sucesso! O sistema de meta progressão está funcionando.")
