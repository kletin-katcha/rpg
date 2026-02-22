from dataclasses import dataclass, field

from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState
from rpg.systems.character.service import criar_personagem
from rpg.systems.inventory.service import adicionar_item_catalogado
from rpg.systems.combat.service import combater_ate_fim
from rpg.systems.city import CityState, construir_estrutura, melhorar_estrutura, ativar_plano_automacao, processar_automacao
from rpg.systems.crafting import forjar_receita
from rpg.systems.meta_world import iniciar_reputacoes, aplicar_evento_mundo, gerar_contrato_aleatorio, concluir_contrato, falhar_contrato, resgatar_beneficio_faccao
from rpg.systems.skills import listar_arvore, habilidades_disponiveis, desbloquear_habilidade
from rpg.systems.economy import iniciar_mercado, atualizar_mercado, vender_item, produzir_liga_metal


@dataclass
class GameState:
    etapa: str = "criacao"
    cidade_atual: str = "Vila Aurora"
    jogador: CharacterState | None = None
    inventario: dict[str, int] = field(default_factory=dict)
    log: list[str] = field(default_factory=list)
    cidade: CityState = field(default_factory=CityState)
    reputacoes: dict[str, int] = field(default_factory=iniciar_reputacoes)
    contrato_ativo: dict | None = None
    mercado: dict[str, float] = field(default_factory=iniciar_mercado)
    dia_economico: int = 0


class Game:
    """Fase 13: economia dinâmica e cadeia de produção avançada."""

    ACTION_ALIASES = {
        "lobo": "cacar_lobo",
        "goblin": "cacar_goblin",
        "forjar": "forjar_espada_longa",
        "oficina": "construir_oficina",
        "automacao": "ativar_automacao",
        "dia": "avancar_dia",
        "status": "ver_status",
        "help": "ajuda",
        "historico": "ver_historico",
        "arvore": "ver_arvore",
        "mercado": "ver_mercado",
    }

    def __init__(self) -> None:
        self.running = True
        self.state = GameState()

    def start_message(self) -> str:
        return "RPG Surreal iniciado: fase 13 pronta (economia dinâmica + produção)."

    def opcoes_criacao(self) -> dict[str, list[str]]:
        racas = load_catalog("racas")
        classes = load_catalog("classes")
        return {
            "racas": sorted(racas.keys()),
            "classes": sorted(classes.keys()),
        }

    def criar_jogador(self, nome: str, raca_id: str, classe_id: str) -> CharacterState:
        jogador = criar_personagem(nome, raca_id, classe_id)
        self.state.jogador = jogador
        self.state.etapa = "cidade"
        self.state.log.append(
            f"Personagem criado: {jogador.nome} ({raca_id}/{classe_id}) em {self.state.cidade_atual}."
        )
        return jogador

    def opcoes_cidade(self) -> list[str]:
        return [
            "descansar",
            "coletar_item_inicial",
            "cacar_lobo",
            "cacar_goblin",
            "cacar_boss",
            "forjar_espada_longa",
            "construir_oficina",
            "melhorar_oficina",
            "construir_nucleo_automacao",
            "ativar_automacao",
            "avancar_dia",
            "ver_mercado",
            "vender_sucata",
            "produzir_liga_metal",
            "ver_status",
            "ver_historico",
            "ajuda",
            "evento_mundo",
            "contrato_aleatorio",
            "faccao_status",
            "concluir_contrato",
            "falhar_contrato",
            "resgatar_beneficio_faccao",
            "ver_arvore",
            "desbloquear_postura_ofensiva",
            "desbloquear_golpe_reforcado",
            "salvar",
            "carregar",
            "sair",
        ]

    def normalizar_acao(self, acao: str) -> str:
        base = acao.strip().lower()
        return self.ACTION_ALIASES.get(base, base)

    def executar_acao_cidade(self, acao: str) -> str:
        if self.state.jogador is None:
            raise RegraNegocioError("Jogador não criado")

        acao = self.normalizar_acao(acao)

        if acao == "descansar":
            self.state.jogador.hp_atual = self.state.jogador.hp_max
            msg = "Você descansou na estalagem e recuperou todo HP."
        elif acao == "coletar_item_inicial":
            adicionar_item_catalogado(self.state.inventario, "pocao_cura", 1)
            msg = "Você recebeu 1 Poção de Cura."
        elif acao == "cacar_lobo":
            resultado = combater_ate_fim(self.state.jogador, "lobo_cinzento", self.state.inventario)
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
        elif acao == "cacar_goblin":
            resultado = combater_ate_fim(self.state.jogador, "goblin_batedor", self.state.inventario)
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
        elif acao == "cacar_boss":
            resultado = combater_ate_fim(self.state.jogador, "ogro_alfa", self.state.inventario)
            msg = (
                f"Boss derrotado={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"fase_final={resultado['fase_final_inimigo']} | Loot={resultado['loot']}"
            )
        elif acao == "forjar_espada_longa":
            forjar_receita(self.state.inventario, "forja_espada_longa")
            msg = "Forja concluída: 1 Espada Longa criada."
        elif acao == "construir_oficina":
            nivel = construir_estrutura(self.state.cidade, "oficina")
            msg = f"Oficina construída no nível {nivel}."
        elif acao == "melhorar_oficina":
            nivel = melhorar_estrutura(self.state.cidade, "oficina")
            msg = f"Oficina melhorada para nível {nivel}."
        elif acao == "construir_nucleo_automacao":
            nivel = construir_estrutura(self.state.cidade, "nucleo_automacao")
            msg = f"Núcleo de automação construído no nível {nivel}."
        elif acao == "ativar_automacao":
            ativar_plano_automacao(self.state.cidade, "coleta_sucata")
            msg = "Plano de automação 'coleta_sucata' ativado."
        elif acao == "avancar_dia":
            processar_automacao(self.state.cidade, self.state.inventario)
            self.state.dia_economico += 1
            atualizar_mercado(self.state.mercado, self.state.dia_economico)
            msg = "Um dia se passou. Automação e mercado processados."
        elif acao == "ver_mercado":
            top = sorted(self.state.mercado.items(), key=lambda kv: kv[1], reverse=True)[:3]
            msg = f"Mercado (dia {self.state.dia_economico}): {top}"
        elif acao == "vender_sucata":
            self.state.cidade.ouro = vender_item(
                self.state.inventario,
                self.state.cidade.ouro,
                "sucata_metal",
                1,
                self.state.mercado,
            )
            msg = f"Venda concluída: 1 sucata_metal. Ouro={self.state.cidade.ouro}"
        elif acao == "produzir_liga_metal":
            produzir_liga_metal(self.state.inventario)
            msg = "Produção concluída: 1 liga_metal (2 barra_metal consumidas)."
        elif acao == "ver_status":
            msg = (
                f"Status: nível {self.state.jogador.nivel}, HP {self.state.jogador.hp_atual}/{self.state.jogador.hp_max}, "
                f"inventário={self.state.inventario}, ouro={self.state.cidade.ouro}, estruturas={self.state.cidade.estruturas}"
            )
        elif acao == "ver_historico":
            ultimos = self.state.log[-5:] if self.state.log else ["Sem histórico ainda."]
            msg = " | ".join(ultimos)
        elif acao == "ajuda":
            msg = f"Ações disponíveis: {', '.join(self.opcoes_cidade())}"
        elif acao == "evento_mundo":
            ev = aplicar_evento_mundo(self.state.cidade.ouro)
            self.state.cidade.ouro = ev["ouro"]
            msg = f"Evento: {ev['evento']} | Ouro agora: {self.state.cidade.ouro}"
        elif acao == "contrato_aleatorio":
            contrato = gerar_contrato_aleatorio("ouro")
            self.state.contrato_ativo = contrato
            msg = (
                f"Contrato ativo: {contrato['nome']} [tier={contrato['tier']}] (XP {contrato['xp']}, Ouro {contrato['ouro']}, "
                f"Facção {contrato['faccao_id']})"
            )
        elif acao == "faccao_status":
            msg = f"Reputações: {self.state.reputacoes}"
        elif acao == "concluir_contrato":
            if self.state.contrato_ativo is None:
                raise RegraNegocioError("Nenhum contrato ativo. Use contrato_aleatorio primeiro.")
            resultado = concluir_contrato(
                self.state.jogador,
                self.state.reputacoes,
                self.state.cidade.ouro,
                self.state.contrato_ativo,
            )
            self.state.cidade.ouro = resultado["ouro"]
            contrato_nome = self.state.contrato_ativo["nome"]
            self.state.contrato_ativo = None
            msg = (
                f"Contrato concluído: {contrato_nome} | XP +{resultado['xp']} | "
                f"Reputação {resultado['faccao_id']}={resultado['reputacao']}"
            )
        elif acao == "falhar_contrato":
            if self.state.contrato_ativo is None:
                raise RegraNegocioError("Nenhum contrato ativo para falhar.")
            resultado = falhar_contrato(self.state.reputacoes, self.state.contrato_ativo)
            contrato_nome = self.state.contrato_ativo["nome"]
            self.state.contrato_ativo = None
            msg = (
                f"Contrato falhou: {contrato_nome} | Reputação {resultado['faccao_id']} {resultado['reputacao']} "
                f"(perda {resultado['perda']})"
            )
        elif acao == "resgatar_beneficio_faccao":
            faccao_mais_relevante = max(self.state.reputacoes, key=self.state.reputacoes.get)
            resultado = resgatar_beneficio_faccao(
                self.state.reputacoes,
                self.state.inventario,
                self.state.cidade.ouro,
                faccao_mais_relevante,
            )
            self.state.cidade.ouro = resultado["ouro"]
            msg = (
                f"Benefício de facção ({faccao_mais_relevante}): {resultado['detalhe']}"
            )
        elif acao == "ver_arvore":
            arvore = listar_arvore("combate_base")
            disponiveis = habilidades_disponiveis(self.state.jogador, "combate_base")
            msg = (
                f"Árvore {arvore['nome']} | desbloqueadas={self.state.jogador.habilidades_desbloqueadas} "
                f"| disponíveis={disponiveis}"
            )
        elif acao == "desbloquear_postura_ofensiva":
            desbloquear_habilidade(self.state.jogador, "postura_ofensiva", "combate_base")
            msg = "Habilidade desbloqueada: postura_ofensiva."
        elif acao == "desbloquear_golpe_reforcado":
            desbloquear_habilidade(self.state.jogador, "golpe_reforcado", "combate_base")
            msg = "Habilidade desbloqueada: golpe_reforcado."
        elif acao == "salvar":
            from rpg.systems.persistence import save_game

            save_game(self)
            msg = "Jogo salvo em savegame.json"
        elif acao == "carregar":
            from rpg.systems.persistence import load_game

            carregado = load_game()
            self.state = carregado.state
            msg = "Jogo carregado de savegame.json"
        elif acao == "sair":
            self.running = False
            msg = "Saindo do jogo."
        else:
            raise RegraNegocioError(f"Ação de cidade inválida: {acao}")

        self.state.log.append(msg)
        return msg
