# SisTop

Protótipo de aplicação desktop de gerenciamento de estoque e fornecedores, desenvolvida em Python com PySide6 e SQLite. O projeto segue o padrão MVC, separando:

- Model: acesso ao banco em `database.py`
- Controller: regras e fluxo em `control.py`
- View: telas em `ui/` e a lógica de navegação em `main.py`

O banco SQLite é criado automaticamente ao iniciar a aplicação.

## Funcionalidades

- Login com usuário padrão: `admin` / `admin`
- Cadastro de produtos
- Consulta de produtos por nome
- Cadastro de fornecedores
- Consulta de fornecedores por nome
- Persistência em banco SQLite

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação e navegação entre telas
- `control.py`: camada de controle (lógica de aplicação)
- `database.py`: modelos e acesso ao banco SQLite
- `ui/`: arquivos gerados da interface do Qt Designer

## Como executar

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   ```

2. Ative o ambiente:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa:
   ```bash
   python main.py
   ```

