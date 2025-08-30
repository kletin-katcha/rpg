# -*- coding: utf-8 -*-
"""
================================================================================================
MOTOR: UTILITÁRIOS - GERENCIADOR DE CONFIGURAÇÃO
================================================================================================
Este módulo é responsável por carregar e salvar as configurações do usuário.
"""

import importlib.util
import os
from rpg_colossal.config import default_settings

# O caminho para o arquivo de configuração do usuário.
# Colocamos na raiz do projeto para ser fácil de encontrar e editar se necessário.
USER_CONFIG_PATH = "user_config.py"

def load_settings():
    """
    Carrega as configurações do arquivo user_config.py.
    Se o arquivo não existir ou não contiver as configurações,
    retorna as configurações padrão.
    """
    try:
        # Para garantir que estamos lendo a versão mais recente do arquivo,
        # precisamos de um mecanismo para "burlar" o cache de importação do Python.
        spec = importlib.util.spec_from_file_location("user_config", USER_CONFIG_PATH)
        if spec is None:
            raise FileNotFoundError

        user_config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(user_config_module)

        user_settings = getattr(user_config_module, "settings")

        # Garante que todas as chaves padrão existam nas configurações do usuário
        settings = default_settings.copy()
        settings.update(user_settings)

        print("Configurações do usuário carregadas com sucesso.")
        return settings

    except (FileNotFoundError, AttributeError):
        # Se o arquivo não existe ou não tem o atributo 'settings'
        print("Arquivo de configuração do usuário não encontrado. Carregando configurações padrão.")
        return default_settings.copy()

def save_settings(settings_dict):
    """
    Salva o dicionário de configurações fornecido no arquivo user_config.py.
    """
    try:
        with open(USER_CONFIG_PATH, "w", encoding="utf-8") as f:
            f.write("# -*- coding: utf-8 -*-\n")
            f.write("# Este arquivo é gerado automaticamente. Não edite manualmente.\n\n")
            f.write(f"settings = {repr(settings_dict)}\n")
        print(f"Configurações salvas com sucesso em {USER_CONFIG_PATH}")
        return True
    except Exception as e:
        print(f"Erro ao salvar as configurações: {e}")
        return False
