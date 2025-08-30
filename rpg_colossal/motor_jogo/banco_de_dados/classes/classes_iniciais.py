# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: CLASSES INICIAIS
================================================================================================
"""
from typing import List, Dict

CLASSES_INICIAIS: List[Dict] = [
    # --- CLASSES MARCIAIS ---
    {
        "id_classe": "guerreiro", "nome": "Guerreiro",
        "descricao_curta": "Mestre do combate marcial, perito em armas e armaduras.",
        "lore": "Um combatente disciplinado que confia na força do aço e na resistência de seu escudo.",
        "foco_atributos": ["forca", "constituicao"],
        "habilidades_iniciais": ["guerreiro_golpe_poderoso"],
        "arvore_de_evolucoes": {"10": ["guardiao", "berserker"]}
    },
    {
        "id_classe": "barbaro", "nome": "Bárbaro",
        "descricao_curta": "Um guerreiro selvagem movido por uma fúria primordial.",
        "lore": "Vindos de terras indomadas, Bárbaros canalizam sua raiva para desferir ataques devastadores, ignorando a própria dor.",
        "foco_atributos": ["forca", "constituicao"],
        "habilidades_iniciais": ["barbaro_furia"],
        "arvore_de_evolucoes": {"10": ["frenetico", "totemico"]}
    },
    {
        "id_classe": "monge", "nome": "Monge",
        "descricao_curta": "Um artista marcial que usa a energia do corpo para lutar.",
        "lore": "Monges treinam seus corpos para serem armas. Eles usam uma energia interna, ou 'Chi', para desferir golpes rápidos e se mover com agilidade sobrenatural.",
        "foco_atributos": ["destreza", "sabedoria"],
        "habilidades_iniciais": ["monge_rajada_de_golpes"],
        "arvore_de_evolucoes": {"10": ["mao_aberta", "sombra"]}
    },
    # --- CLASSES DE ESPECIALISTAS ---
    {
        "id_classe": "ladino", "nome": "Ladino",
        "descricao_curta": "Especialista em furtividade, truques e ataques precisos.",
        "lore": "Operando nas sombras, o Ladino é um mestre do subterfúgio, usando sua astúcia para superar os inimigos e explorar suas fraquezas.",
        "foco_atributos": ["destreza", "inteligencia"],
        "habilidades_iniciais": ["ladino_ataque_furtivo"],
        "arvore_de_evolucoes": {"10": ["assassino", "trapaceiro"]}
    },
    {
        "id_classe": "bardo", "nome": "Bardo",
        "descricao_curta": "Um mestre da música, da palavra e da magia de encanto.",
        "lore": "Bardos são contadores de histórias, músicos e andarilhos. Sua magia vem da alma do mundo, tecida em canções e palavras que podem inspirar aliados e confundir inimigos.",
        "foco_atributos": ["carisma", "destreza"],
        "habilidades_iniciais": ["bardo_inspiracao", "magia_menor_bardo"],
        "arvore_de_evolucoes": {"10": ["colegio_do_conhecimento", "colegio_da_valentia"]}
    },
    # --- CLASSES MÁGICAS (Arcano) ---
    {
        "id_classe": "mago", "nome": "Mago",
        "descricao_curta": "Um estudioso que molda a realidade através do intelecto.",
        "lore": "Para o Mago, a magia é uma ciência. Através de anos de estudo, ele aprende a manipular as energias arcanas para criar efeitos poderosos.",
        "foco_atributos": ["inteligencia", "sabedoria"],
        "habilidades_iniciais": ["mago_seta_de_fogo"],
        "arvore_de_evolucoes": {"10": ["piromante", "criomante", "ilusionista"]}
    },
    {
        "id_classe": "feiticeiro", "nome": "Feiticeiro",
        "descricao_curta": "Um conjurador nato, cuja magia flui de sua linhagem.",
        "lore": "Diferente do Mago, o Feiticeiro não estuda magia; ele *é* a magia. Seu poder é um dom inato, vindo de uma linhagem dracônica, celestial ou de outras fontes misteriosas.",
        "foco_atributos": ["carisma", "constituicao"],
        "habilidades_iniciais": ["feiticeiro_magia_selvagem"],
        "arvore_de_evolucoes": {"10": ["linhagem_draconica", "magia_selvagem"]}
    },
    {
        "id_classe": "bruxo", "nome": "Bruxo",
        "descricao_curta": "Alguém que fez um pacto com uma entidade poderosa por poder.",
        "lore": "O Bruxo busca poder através de atalhos, forjando pactos com seres de outros planos - demônios, fadas, ou entidades cósmicas - em troca de segredos e magias.",
        "foco_atributos": ["carisma", "inteligencia"],
        "habilidades_iniciais": ["bruxo_rajada_mistica"],
        "arvore_de_evolucoes": {"10": ["pacto_da_lamina", "pacto_do_tomo"]}
    },
    # --- CLASSES MÁGICAS (Divino/Natureza) ---
    {
        "id_classe": "clerigo", "nome": "Clérigo",
        "descricao_curta": "Um canal de poder divino para curar e proteger.",
        "lore": "A força do Clérigo vem de sua devoção a uma divindade, que lhe concede o poder de realizar milagres, curar os feridos e punir os profanos.",
        "foco_atributos": ["sabedoria", "constituicao"],
        "habilidades_iniciais": ["clerigo_cura_leve"],
        "arvore_de_evolucoes": {"10": ["sacerdote", "inquisidor"]}
    },
    {
        "id_classe": "druida", "nome": "Druida",
        "descricao_curta": "Um sacerdote da natureza, capaz de se transformar em animais.",
        "lore": "Druidas são os guardiões do mundo natural. Sua magia vem da própria terra, permitindo-lhes controlar plantas, invocar animais e até mesmo assumir suas formas.",
        "foco_atributos": ["sabedoria", "destreza"],
        "habilidades_iniciais": ["druida_forma_selvagem_lobo"],
        "arvore_de_evolucoes": {"10": ["circulo_da_lua", "circulo_da_terra"]}
    },
    {
        "id_classe": "paladino", "nome": "Paladino",
        "descricao_curta": "Um guerreiro sagrado que fez um juramento de proteger os inocentes.",
        "lore": "Movido por um juramento sagrado, o Paladino é um farol de esperança que combina proeza marcial com poder divino para combater o mal.",
        "foco_atributos": ["forca", "carisma"],
        "habilidades_iniciais": ["paladino_golpe_divino"],
        "arvore_de_evolucoes": {"10": ["juramento_da_devocao", "juramento_da_vinganca"]}
    }
]

INDICE_CLASSES_INICIAIS = {"by_id": {c["id_classe"]: c for c in CLASSES_INICIAIS}}
