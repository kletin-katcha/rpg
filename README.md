# Ecos da Aetheria

## Sobre o Projeto

Ecos da Aetheria é um projeto de RPG de texto colossal, desenvolvido inteiramente em Python. Sua arquitetura é projetada para ser altamente modular, com uma separação clara entre o motor do jogo (`motor_jogo/`) e as interfaces de usuário (`interface_grafica/`, `interface_terminal/`). O objetivo é criar uma experiência de RPG rica e expansível, com todos os dados do jogo (raças, classes, itens, etc.) gerenciados através de estruturas de dados Python.

## Características Atuais

O projeto atualmente possui um loop de gameplay funcional através da interface gráfica (GUI).

- **Interface Gráfica com Tkinter:** Uma GUI funcional que permite a navegação entre as diferentes telas do jogo.
- **Menu Principal:** Inclui opções para Iniciar um Novo Jogo, Carregar Jogo (não implementado), Configurações e Sair.
- **Tela de Configurações:** Permite ajustar o tamanho da fonte da aplicação, com as configurações sendo salvas e carregadas entre sessões.
- **Criação de Personagem Detalhada:**
  - Sistema de 7 atributos: Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma e Sorte.
  - Lógica de atributos baseada na fórmula: `5 (base) + Bônus Racial + 20 Pontos de Bônus`.
  - Seleção de Raça e Classe a partir do banco de dados do jogo.
- **Ciclo de Jogo Inicial:**
  - O jogador começa em uma tela de cidade após criar o personagem.
  - É possível navegar para uma área de exploração.
  - Na exploração, o jogador pode iniciar um combate com um monstro aleatório da região.
- **Sistema de Combate por Turnos:**
  - Interface de combate que exibe o status do jogador e do monstro.
  - Log de combate para narrar as ações.
  - Funcionalidade de ataque básico implementada.
  - Condições de vitória e derrota, com o jogador retornando à cidade após o combate.

## Estrutura do Projeto

O código é organizado nos seguintes diretórios principais:

- **`rpg_colossal/`**: O pacote principal do projeto.
  - **`motor_jogo/`**: Contém toda a lógica central do jogo, independente de interface.
    - `entidades/`: As classes para `Personagem`, `Monstro`, etc.
    - `sistemas/`: Os gerenciadores de sistemas como `Combate`, `Save/Load`, etc.
    - `banco_de_dados/`: Todos os dados do jogo, como raças, classes e monstros.
  - **`interface_grafica/`**: A implementação da GUI com Tkinter.
    - `views/`: Cada tela do jogo é uma "view" em seu próprio arquivo (ex: `view_cidade.py`).
  - **`interface_terminal/`**: (Legado/Em desenvolvimento) A implementação da interface via terminal.

## Como Executar

Para rodar a versão com interface gráfica do RPG, execute o seguinte comando a partir da raiz do projeto:

```bash
python3 rpg_colossal/interface_grafica/main_window.py
```

## Sistema de Atributos

A criação de atributos do personagem segue uma regra clara:

- Cada um dos 7 atributos começa com um valor base de **5**.
- Ao escolher uma **Raça**, bônus (positivos ou negativos) são aplicados a esses valores base.
- O jogador então recebe **20 pontos de bônus** para distribuir livremente entre os atributos, customizando seu personagem.
