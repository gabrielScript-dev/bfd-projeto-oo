# Sistema de Cadastro de Livros

Este é um sistema simples de cadastro e gerenciamento de livros e escritores, implementado em Python seguindo o padrão **MVC (Model-View-Controller)**.

---

## Funcionalidades

O sistema permite:

- Cadastrar escritores.
- Cadastrar livros vinculados a escritores cadastrados.
- Buscar livros pelo nome.
- Excluir livros.
- Listar todos os livros cadastrados.

---

## Estrutura do Projeto

O projeto segue o padrão MVC:

### 1. Model (`model.py`)
Define as entidades principais do sistema:

- **Escritor**: representa um autor, com atributos `nome`, `email` e `descricao`.
- **Livro**: representa um livro, com atributos `nome`, `ano` e um objeto `escritor`. Possui método `exibir_dados()` para exibir informações detalhadas do livro e do autor.

### 2. Controller (`controller.py`)
Responsável pela lógica de negócios:

- Gerencia listas de livros e escritores.
- Permite adicionar, buscar, excluir e listar livros.
- Permite adicionar escritores.
- Garante que um livro só seja cadastrado se o escritor correspondente já existir.

### 3. View (`view.py`)
Responsável pela interface com o usuário via terminal:

- Exibe menus e opções.
- Recebe dados de entrada para cadastro de livros e escritores.
- Mostra mensagens de status ou resultados das operações.

### 4. Main (`main.py`)
Ponto de entrada do sistema:

- Inicializa as classes `View` e `Controller`.
- Loop principal que exibe o menu e processa as opções escolhidas pelo usuário.

---

## Como Executar

1. Certifique-se de ter Python 3.x instalado.
2. Clone ou baixe este repositório.
3. Navegue até a pasta do projeto no terminal.
4. Execute o script principal:

```bash
python main.py
