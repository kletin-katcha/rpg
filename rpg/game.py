from dataclasses import dataclass, field

from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.core.types import CharacterState
from rpg.systems.character.service import criar_personagem, conceder_xp
from rpg.systems.inventory.service import adicionar_item_catalogado
from rpg.systems.combat.service import combater_ate_fim
from rpg.systems.city import CityState, construir_estrutura, melhorar_estrutura, ativar_plano_automacao, processar_automacao
from rpg.systems.crafting import forjar_receita
from rpg.systems.meta_world import iniciar_reputacoes, aplicar_evento_mundo, gerar_contrato_aleatorio, concluir_contrato, falhar_contrato, resgatar_beneficio_faccao, gerar_cadeia_contratos, progresso_cadeia, avaliar_tensao_faccoes, gerar_crise_urbana
from rpg.systems.skills import listar_arvore, habilidades_disponiveis, desbloquear_habilidade
from rpg.systems.economy import iniciar_mercado, atualizar_mercado, vender_item, produzir_liga_metal
from rpg.systems.immersion import periodo_do_dia, avancar_tempo, atualizar_clima, registrar_jornal, desbloquear_lore, codex_base
from rpg.systems.world_director import iniciar_memoria_faccoes, gerar_arco_mundo, escolher_mutador, aplicar_mutador_mercado, registrar_memoria
from rpg.systems.expansion import regioes_base, viajar_para_regiao, gerar_dungeon, explorar_dungeon, simular_agenda_faccoes, iniciar_arco_longo, avancar_arco_longo, gerar_pacote_expansao, simular_balance_headless, validar_estado_expansao


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
    hora: int = 8
    clima: str = "ensolarado"
    jornal_cidade: list[str] = field(default_factory=list)
    codex: set[str] = field(default_factory=codex_base)
    mutador_ativo: str | None = None
    memoria_faccoes: dict[str, list[str]] = field(default_factory=dict)
    cadeia_contratos: list[dict] = field(default_factory=list)
    cadeia_resolvidos: int = 0
    tensao_faccoes: dict = field(default_factory=dict)
    crise_urbana: dict = field(default_factory=dict)
    regiao_atual: str = "vila_aurora"
    energia_viagem: int = 6
    regioes_descobertas: set[str] = field(default_factory=lambda: {"vila_aurora"})
    dungeon_ativa: dict | None = None
    agenda_faccoes: list[str] = field(default_factory=list)
    arco_longo: dict | None = None
    checkpoint_criacao: dict[str, str] | None = None
    ultimo_log_combate: list[dict] = field(default_factory=list)
    metricas_onboarding: dict[str, int] = field(
        default_factory=lambda: {
            "erros_criacao": 0,
            "comandos_invalidos": 0,
            "erros_regra_negocio": 0,
        }
    )


class Game:
    """Fase 25: expansão massiva concluída (fases 21-25)."""

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
        "jornal": "ver_jornal",
        "clima": "ver_clima",
        "codex": "ver_codex",
        "arco": "gerar_arco_mundo",
        "mutador": "aplicar_mutador",
        "memoria": "ver_memoria_faccoes",
        "condicoes": "ver_condicoes_combate",
        "cadeia": "iniciar_cadeia_contratos",
        "tensao": "ver_tensao_faccoes",
        "crise": "gerar_crise_urbana",
        "viagem": "ver_regiao",
        "dungeon": "gerar_dungeon",
        "agenda": "rodar_agenda_faccoes",
        "arco_longo": "ver_arco_longo",
        "expansao": "gerar_pacote_expansao",
        "diagnostico": "diagnostico_fases_1_25",
    }

    def __init__(self) -> None:
        self.running = True
        self.state = GameState()
        self.state.memoria_faccoes = iniciar_memoria_faccoes(self.state.reputacoes)

    def ajuda_contextual(self) -> str:
        grupos = {
            "core": ["descansar", "coletar_item_inicial", "ver_status", "ver_historico", "ajuda", "sair"],
            "combate": ["cacar_lobo", "cacar_goblin", "cacar_boss", "ver_condicoes_combate", "ver_arvore"],
            "economia": [
                "forjar_espada_longa",
                "construir_oficina",
                "melhorar_oficina",
                "construir_nucleo_automacao",
                "ativar_automacao",
                "ver_mercado",
                "vender_sucata",
                "produzir_liga_metal",
            ],
            "mundo": [
                "evento_mundo",
                "contrato_aleatorio",
                "concluir_contrato",
                "falhar_contrato",
                "faccao_status",
                "resgatar_beneficio_faccao",
                "iniciar_cadeia_contratos",
                "ver_cadeia_contratos",
                "gerar_tensao_faccoes",
                "ver_tensao_faccoes",
                "gerar_crise_urbana",
                "ver_crise_urbana",
            ],
            "expansao": [
                "ver_regiao",
                "viajar_fronteira_norte",
                "viajar_ruinas_antigas",
                "gerar_dungeon",
                "explorar_dungeon",
                "rodar_agenda_faccoes",
                "ver_agenda_faccoes",
                "iniciar_arco_longo",
                "avancar_arco_longo",
                "ver_arco_longo",
                "gerar_pacote_expansao",
                "simular_balance_headless",
                "diagnostico_fases_1_25",
            ],
            "sistema": ["salvar", "carregar", "rollback_criacao", "ver_metricas_onboarding"],
        }
        partes = [
            f"{grupo}: {', '.join([acao for acao in acoes if acao in self.opcoes_cidade()])}"
            for grupo, acoes in grupos.items()
        ]
        return "Ajuda contextual -> " + " | ".join(partes)

    def start_message(self) -> str:
        return "RPG Surreal iniciado: fase 25 pronta (expansão massiva de conteúdo e sistemas)."

    def opcoes_criacao(self) -> dict[str, list[str]]:
        racas = load_catalog("racas")
        classes = load_catalog("classes")
        return {
            "racas": sorted(racas.keys()),
            "classes": sorted(classes.keys()),
        }

    def criar_jogador(self, nome: str, raca_id: str, classe_id: str) -> CharacterState:
        try:
            jogador = criar_personagem(nome, raca_id, classe_id)
        except RegraNegocioError:
            self.state.metricas_onboarding["erros_criacao"] += 1
            raise
        self.state.jogador = jogador
        self.state.etapa = "cidade"
        self.state.log.append(
            f"Personagem criado: {jogador.nome} ({raca_id}/{classe_id}) em {self.state.cidade_atual}."
        )
        self.state.checkpoint_criacao = {
            "nome": nome,
            "raca_id": raca_id,
            "classe_id": classe_id,
        }
        return jogador

    def opcoes_cidade(self) -> list[str]:
        return [
            "descansar",
            "coletar_item_inicial",
            "cacar_lobo",
            "cacar_goblin",
            "cacar_esqueleto",
            "cacar_aranha",
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
            "ver_clima",
            "ver_jornal",
            "ver_codex",
            "gerar_arco_mundo",
            "aplicar_mutador",
            "ver_memoria_faccoes",
            "iniciar_cadeia_contratos",
            "ver_cadeia_contratos",
            "gerar_tensao_faccoes",
            "ver_tensao_faccoes",
            "gerar_crise_urbana",
            "ver_crise_urbana",
            "ver_regiao",
            "viajar_fronteira_norte",
            "viajar_ruinas_antigas",
            "gerar_dungeon",
            "explorar_dungeon",
            "rodar_agenda_faccoes",
            "ver_agenda_faccoes",
            "iniciar_arco_longo",
            "avancar_arco_longo",
            "ver_arco_longo",
            "gerar_pacote_expansao",
            "simular_balance_headless",
            "ver_status",
            "ver_historico",
            "ver_log_combate",
            "ajuda",
            "buscar_acoes:<termo>",
            "ver_metricas_onboarding",
            "rollback_criacao",
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

    def mutadores_combate_atuais(self) -> dict[str, int]:
        mutadores = {
            "bonus_dano_personagem": 0,
            "reducao_dano_personagem": 0,
            "bonus_dano_inimigo": 0,
        }

        periodo = periodo_do_dia(self.state.hora)
        if periodo == "noite":
            mutadores["bonus_dano_inimigo"] += 1

        if self.state.clima == "tempestade_arcana":
            mutadores["bonus_dano_inimigo"] += 1
        elif self.state.clima == "ensolarado":
            mutadores["bonus_dano_personagem"] += 1
        elif self.state.clima == "chuvoso":
            mutadores["reducao_dano_personagem"] += 1

        if self.state.mutador_ativo == "escassez":
            mutadores["bonus_dano_inimigo"] += 1
        elif self.state.mutador_ativo == "prosperidade":
            mutadores["bonus_dano_personagem"] += 1

        return mutadores

    def normalizar_acao(self, acao: str) -> str:
        base = acao.strip().lower()
        return self.ACTION_ALIASES.get(base, base)

    def executar_acao_cidade(self, acao: str) -> str:
        if self.state.jogador is None:
            raise RegraNegocioError("Jogador não criado")

        acao = self.normalizar_acao(acao)

        if acao.startswith("buscar_acoes:"):
            termo = acao.split(":", 1)[1].strip().lower()
            if not termo:
                raise RegraNegocioError("Informe um termo: buscar_acoes:<termo>")
            encontradas = [op for op in self.opcoes_cidade() if termo in op.lower()]
            msg = f"Busca '{termo}': {encontradas or ['nenhuma ação encontrada']}"
            self.state.log.append(msg)
            return msg

        if acao == "descansar":
            self.state.jogador.hp_atual = self.state.jogador.hp_max
            msg = "Você descansou na estalagem e recuperou todo HP."
        elif acao == "coletar_item_inicial":
            adicionar_item_catalogado(self.state.inventario, "pocao_cura", 1)
            msg = "Você recebeu 1 Poção de Cura."
        elif acao == "cacar_lobo":
            resultado = combater_ate_fim(
                self.state.jogador,
                "lobo_cinzento",
                self.state.inventario,
                self.mutadores_combate_atuais(),
            )
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
            self.state.ultimo_log_combate = resultado.get("log_turnos", [])
        elif acao == "cacar_goblin":
            resultado = combater_ate_fim(
                self.state.jogador,
                "goblin_batedor",
                self.state.inventario,
                self.mutadores_combate_atuais(),
            )
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
            self.state.ultimo_log_combate = resultado.get("log_turnos", [])
        elif acao == "cacar_esqueleto":
            resultado = combater_ate_fim(
                self.state.jogador,
                "esqueleto_vigia",
                self.state.inventario,
                self.mutadores_combate_atuais(),
            )
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
            self.state.ultimo_log_combate = resultado.get("log_turnos", [])
        elif acao == "cacar_aranha":
            resultado = combater_ate_fim(
                self.state.jogador,
                "aranha_cavernosa",
                self.state.inventario,
                self.mutadores_combate_atuais(),
            )
            msg = (
                f"Combate concluído. Vitória={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"Loot={resultado['loot']}"
            )
            self.state.ultimo_log_combate = resultado.get("log_turnos", [])
        elif acao == "cacar_boss":
            resultado = combater_ate_fim(
                self.state.jogador,
                "ogro_alfa",
                self.state.inventario,
                self.mutadores_combate_atuais(),
            )
            msg = (
                f"Boss derrotado={resultado['vitoria']} | XP +{resultado['xp_recebido']} | "
                f"fase_final={resultado['fase_final_inimigo']} | Loot={resultado['loot']}"
            )
            self.state.ultimo_log_combate = resultado.get("log_turnos", [])
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
            self.state.hora = avancar_tempo(self.state.hora, 6)
            self.state.clima = atualizar_clima(self.state.dia_economico)
            self.state.energia_viagem = min(10, self.state.energia_viagem + 2)
            atualizar_mercado(self.state.mercado, self.state.dia_economico)
            registrar_jornal(
                self.state.jornal_cidade,
                f"Dia {self.state.dia_economico}: clima={self.state.clima}, periodo={periodo_do_dia(self.state.hora)}",
            )
            msg = "Tempo avançado. Automação, mercado e clima atualizados."
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
        elif acao == "ver_clima":
            msg = f"Clima atual: {self.state.clima} | Período: {periodo_do_dia(self.state.hora)}"
        elif acao == "ver_jornal":
            ultimos = self.state.jornal_cidade[-5:] if self.state.jornal_cidade else ["Sem eventos no jornal."]
            msg = " | ".join(ultimos)
        elif acao == "ver_codex":
            msg = f"Codex desbloqueado: {sorted(self.state.codex)}"
        elif acao == "gerar_arco_mundo":
            arco = gerar_arco_mundo(self.state.reputacoes, self.state.clima, self.state.hora)
            registrar_jornal(self.state.jornal_cidade, f"Arco: {arco['titulo']}")
            msg = f"Arco gerado: {arco['titulo']} | {arco['descricao']}"
        elif acao == "aplicar_mutador":
            mutador = escolher_mutador(self.state.dia_economico)
            self.state.mutador_ativo = mutador
            aplicar_mutador_mercado(self.state.mercado, mutador)
            registrar_jornal(self.state.jornal_cidade, f"Mutador ativo: {mutador}")
            msg = f"Mutador aplicado: {mutador}"
        elif acao == "ver_memoria_faccoes":
            msg = f"Memória de facções: {self.state.memoria_faccoes}"
        elif acao == "ver_condicoes_combate":
            msg = f"Condições de combate atuais: {self.mutadores_combate_atuais()}"
        elif acao == "ver_regiao":
            msg = f"Região atual: {self.state.regiao_atual} | energia_viagem={self.state.energia_viagem}"
        elif acao == "viajar_fronteira_norte":
            resultado = viajar_para_regiao(self.state.regiao_atual, "fronteira_norte", self.state.energia_viagem)
            if not resultado["ok"]:
                raise RegraNegocioError(f"Viagem falhou: {resultado['motivo']}")
            self.state.regiao_atual = resultado["regiao"]
            self.state.energia_viagem = resultado["energia"]
            self.state.regioes_descobertas.add(resultado["regiao"])
            msg = f"Viagem concluída para {resultado['regiao']} (energia {self.state.energia_viagem})."
        elif acao == "viajar_ruinas_antigas":
            resultado = viajar_para_regiao(self.state.regiao_atual, "ruinas_antigas", self.state.energia_viagem)
            if not resultado["ok"]:
                raise RegraNegocioError(f"Viagem falhou: {resultado['motivo']}")
            self.state.regiao_atual = resultado["regiao"]
            self.state.energia_viagem = resultado["energia"]
            self.state.regioes_descobertas.add(resultado["regiao"])
            msg = f"Viagem concluída para {resultado['regiao']} (energia {self.state.energia_viagem})."
        elif acao == "gerar_dungeon":
            self.state.dungeon_ativa = gerar_dungeon(self.state.dia_economico, self.state.regiao_atual)
            msg = f"Dungeon gerada: {self.state.dungeon_ativa}"
        elif acao == "explorar_dungeon":
            if not self.state.dungeon_ativa:
                raise RegraNegocioError("Nenhuma dungeon ativa. Use gerar_dungeon primeiro.")
            resultado = explorar_dungeon(self.state.jogador.hp_atual, self.state.dungeon_ativa)
            self.state.jogador.hp_atual = resultado["hp_final"]
            conceder_xp(self.state.jogador, resultado["xp"])
            self.state.cidade.ouro += resultado["ouro"]
            self.state.dungeon_ativa["concluida"] = True
            registrar_jornal(self.state.jornal_cidade, f"Dungeon concluída: {self.state.dungeon_ativa['id']}")
            msg = f"Dungeon explorada: XP+{resultado['xp']} Ouro+{resultado['ouro']} HP={resultado['hp_final']}"
        elif acao == "rodar_agenda_faccoes":
            self.state.agenda_faccoes = simular_agenda_faccoes(self.state.reputacoes, self.state.dia_economico)
            self.state.tensao_faccoes = avaliar_tensao_faccoes(self.state.reputacoes)
            registrar_jornal(self.state.jornal_cidade, "Agenda faccional processada")
            msg = f"Agenda de facções executada: {self.state.agenda_faccoes} | tensão={self.state.tensao_faccoes['status']}"
        elif acao == "ver_agenda_faccoes":
            msg = f"Agenda recente: {self.state.agenda_faccoes or ['sem eventos']}"
        elif acao == "iniciar_arco_longo":
            self.state.arco_longo = iniciar_arco_longo("Ascensão das Cinzas")
            msg = f"Arco longo iniciado: {self.state.arco_longo}"
        elif acao == "avancar_arco_longo":
            if not self.state.arco_longo:
                raise RegraNegocioError("Nenhum arco longo ativo. Use iniciar_arco_longo.")
            self.state.arco_longo = avancar_arco_longo(self.state.arco_longo)
            if self.state.arco_longo.get("concluido"):
                bonus = self.state.arco_longo.get("recompensa_final_ouro", 0)
                self.state.cidade.ouro += bonus
                registrar_jornal(self.state.jornal_cidade, f"Arco concluído: {self.state.arco_longo['titulo']}")
            msg = f"Arco longo atualizado: {self.state.arco_longo}"
        elif acao == "ver_arco_longo":
            msg = f"Arco longo: {self.state.arco_longo or 'nenhum'}"
        elif acao == "gerar_pacote_expansao":
            pacote = gerar_pacote_expansao("fase25", 5)
            msg = f"Pacote de expansão gerado: {pacote}"
        elif acao == "simular_balance_headless":
            resultado = simular_balance_headless(20)
            msg = f"Simulação headless: {resultado}"
        elif acao == "diagnostico_fases_1_25":
            validacao = validar_estado_expansao(
                {
                    "energia_viagem": self.state.energia_viagem,
                    "regiao_atual": self.state.regiao_atual,
                    "regioes_descobertas": self.state.regioes_descobertas,
                    "dungeon_ativa": self.state.dungeon_ativa,
                    "arco_longo": self.state.arco_longo,
                }
            )
            resumo = {
                "fase1_criacao": self.state.jogador is not None,
                "fase6_save_ready": True,
                "fase10_faccoes": bool(self.state.reputacoes),
                "fase15_diretor": self.state.mutador_ativo is not None or bool(self.state.memoria_faccoes),
                "fase20_crise": isinstance(self.state.crise_urbana, dict),
                "fase25_expansao_ok": validacao["ok"],
            }
            msg = f"Diagnóstico 1-25: {resumo} | erros_expansao={validacao['erros']}"
        elif acao == "ver_status":
            msg = (
                f"Status: nível {self.state.jogador.nivel}, HP {self.state.jogador.hp_atual}/{self.state.jogador.hp_max}, "
                f"inventário={self.state.inventario}, ouro={self.state.cidade.ouro}, estruturas={self.state.cidade.estruturas}, "
                f"região={self.state.regiao_atual}, energia={self.state.energia_viagem}"
            )
        elif acao == "ver_historico":
            ultimos = self.state.log[-5:] if self.state.log else ["Sem histórico ainda."]
            msg = " | ".join(ultimos)
        elif acao == "ver_log_combate":
            if not self.state.ultimo_log_combate:
                msg = "Sem log de combate ainda."
            else:
                ultimos_turnos = self.state.ultimo_log_combate[-3:]
                msg = f"Log combate (últimos turnos): {ultimos_turnos}"
        elif acao == "ajuda":
            msg = self.ajuda_contextual()
        elif acao == "ver_metricas_onboarding":
            msg = f"Métricas onboarding: {self.state.metricas_onboarding}"
        elif acao == "rollback_criacao":
            if not self.state.checkpoint_criacao:
                raise RegraNegocioError("Sem checkpoint de criação para rollback.")
            checkpoint = self.state.checkpoint_criacao
            self.state = GameState()
            self.state.memoria_faccoes = iniciar_memoria_faccoes(self.state.reputacoes)
            self.criar_jogador(checkpoint["nome"], checkpoint["raca_id"], checkpoint["classe_id"])
            msg = "Rollback aplicado: estado do jogo restaurado para logo após a criação."
        elif acao == "evento_mundo":
            ev = aplicar_evento_mundo(self.state.cidade.ouro)
            self.state.cidade.ouro = ev["ouro"]
            desbloquear_lore(self.state.codex, f"evento:{ev['evento']}")
            registrar_jornal(self.state.jornal_cidade, f"Evento mundial registrado: {ev['evento']}")
            msg = f"Evento: {ev['evento']} | Ouro agora: {self.state.cidade.ouro}"
        elif acao == "contrato_aleatorio":
            contrato = gerar_contrato_aleatorio("ouro")
            self.state.contrato_ativo = contrato
            msg = (
                f"Contrato ativo: {contrato['nome']} [tier={contrato['tier']}] (XP {contrato['xp']}, Ouro {contrato['ouro']}, "
                f"Facção {contrato['faccao_id']})"
            )
        elif acao == "iniciar_cadeia_contratos":
            self.state.cadeia_contratos = gerar_cadeia_contratos("ouro", tamanho=3)
            self.state.cadeia_resolvidos = 0
            self.state.contrato_ativo = self.state.cadeia_contratos[0]
            msg = (
                f"Cadeia iniciada: {len(self.state.cadeia_contratos)} contratos | "
                f"Primeiro: {self.state.contrato_ativo['nome']}"
            )
        elif acao == "ver_cadeia_contratos":
            msg = progresso_cadeia(self.state.cadeia_resolvidos, len(self.state.cadeia_contratos))
        elif acao == "gerar_tensao_faccoes":
            self.state.tensao_faccoes = avaliar_tensao_faccoes(self.state.reputacoes)
            self.state.cidade.ouro += self.state.tensao_faccoes.get("efeito_ouro", 0)
            msg = f"Tensão de facções atualizada: {self.state.tensao_faccoes}"
        elif acao == "ver_tensao_faccoes":
            if not self.state.tensao_faccoes:
                self.state.tensao_faccoes = avaliar_tensao_faccoes(self.state.reputacoes)
            msg = f"Tensão de facções: {self.state.tensao_faccoes}"
        elif acao == "gerar_crise_urbana":
            if not self.state.tensao_faccoes:
                self.state.tensao_faccoes = avaliar_tensao_faccoes(self.state.reputacoes)
            self.state.crise_urbana = gerar_crise_urbana(self.state.tensao_faccoes, self.state.clima)
            self.state.cidade.ouro += self.state.crise_urbana.get("impacto_ouro", 0)
            registrar_jornal(self.state.jornal_cidade, f"Crise urbana: {self.state.crise_urbana['tipo']}")
            msg = f"Crise urbana gerada: {self.state.crise_urbana}"
        elif acao == "ver_crise_urbana":
            msg = f"Crise urbana atual: {self.state.crise_urbana or 'nenhuma'}"
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
            if self.state.cadeia_contratos and self.state.cadeia_resolvidos < len(self.state.cadeia_contratos):
                self.state.cadeia_resolvidos += 1
                if self.state.cadeia_resolvidos < len(self.state.cadeia_contratos):
                    self.state.contrato_ativo = self.state.cadeia_contratos[self.state.cadeia_resolvidos]
            registrar_memoria(self.state.memoria_faccoes, resultado["faccao_id"], f"sucesso:{contrato_nome}")
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
            if self.state.cadeia_contratos:
                self.state.cadeia_contratos = []
                self.state.cadeia_resolvidos = 0
            registrar_memoria(self.state.memoria_faccoes, resultado["faccao_id"], f"falha:{contrato_nome}")
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
            if not self.state.memoria_faccoes:
                self.state.memoria_faccoes = iniciar_memoria_faccoes(self.state.reputacoes)
            msg = "Jogo carregado de savegame.json"
        elif acao == "sair":
            self.running = False
            msg = "Saindo do jogo."
        else:
            self.state.metricas_onboarding["comandos_invalidos"] += 1
            raise RegraNegocioError(f"Ação de cidade inválida: {acao}")

        self.state.log.append(msg)
        return msg
