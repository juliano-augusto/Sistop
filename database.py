import sqlite3


class DatabaseConnection:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()


class Usuario:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def cria_tabela_usuarios(self):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    UNIQUE(usuario, senha)
                );
                """
            )
            connection.commit()

    def insere_usuario_padrao(self):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT OR IGNORE INTO usuarios(usuario, senha) VALUES (?, ?)
                """,
                ("admin", "admin"),
            )
            connection.commit()

    def autenticacao(self, user, senha):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT usuario, senha
                FROM usuarios
                WHERE UPPER(usuario) = UPPER(?) AND UPPER(senha) = UPPER(?)
                """,
                (user, senha),
            )
            return "user" if cursor.fetchone() else "sem acesso"


class Produtos:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def cria_tabela_produto(self):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS produtos(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    sabor TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    preco REAL NOT NULL,
                    peso REAL,
                    volume REAL,
                    UNIQUE(nome, sabor)
                );
                """
            )
            connection.commit()

    def insere_produto(self, nome, marca, sabor, quantidade, preco, peso=None, volume=None):
        try:
            with DatabaseConnection(self.name) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """
                    INSERT INTO produtos(nome, marca, sabor, quantidade, preco, peso, volume)
                    VALUES(?,?,?,?,?,?,?)
                    ON CONFLICT(nome, sabor) DO UPDATE SET
                        marca = excluded.marca,
                        quantidade = excluded.quantidade,
                        preco = excluded.preco,
                        peso = excluded.peso,
                        volume = excluded.volume
                    """,
                    (nome, marca, sabor, quantidade, preco, peso, volume),
                )
                connection.commit()
                return True
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
            return False
        except sqlite3.Error as e:
            print(f"Erro ao inserir o produto: {e}")
            return False

    def busca_produto(self, nome):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT nome, marca, sabor, quantidade, preco, peso, volume
                FROM produtos
                WHERE nome LIKE ?
                ORDER BY nome
                """,
                ('%' + nome + '%',),
            )
            return cursor.fetchall()

    def busca_produto_por_nome(self, nome):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT nome, marca, sabor, quantidade, preco, peso, volume
                FROM produtos
                WHERE LOWER(nome) = LOWER(?)
                LIMIT 1
                """,
                (nome,),
            )
            return cursor.fetchone()

    def atualiza_estoque(self, nome, nova_quantidade):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE produtos
                SET quantidade = ?
                WHERE LOWER(nome) = LOWER(?)
                """,
                (nova_quantidade, nome),
            )
            connection.commit()
            return cursor.rowcount > 0

    def listar_produtos(self):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT nome, marca, sabor, quantidade, preco, peso, volume
                FROM produtos
                ORDER BY nome
                """
            )
            return cursor.fetchall()


class Fornecedores:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def cria_tabela_fornecedor(self):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS fornecedores(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cnpj INTEGER NOT NULL,
                    end TEXT NOT NULL,
                    numero INTEGER NOT NULL,
                    cidade TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    tel INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    UNIQUE(cnpj)
                );
                """
            )
            connection.commit()

    def insert_fornecedor(self, nome, cnpj, end, numero, cidade, estado, tel, email):
        try:
            with DatabaseConnection(self.name) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    """
                    INSERT INTO fornecedores(nome, cnpj, end, numero, cidade, estado, tel, email)
                    VALUES(?,?,?,?,?,?,?,?)
                    """,
                    (nome, cnpj, end, numero, cidade, estado, tel, email),
                )
                connection.commit()
                return True
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
            return False
        except sqlite3.Error as e:
            print(f"Erro ao inserir fornecedor: {e}")
            return False

    def busca_fornecedor(self, nome):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT nome, cnpj, end, numero, cidade, estado, tel, email
                FROM fornecedores
                WHERE nome LIKE ?
                ORDER BY nome
                """,
                ('%' + nome + '%',),
            )
            return cursor.fetchall()

    def listar_fornecedores(self):
        with DatabaseConnection(self.name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT nome, cnpj, end, numero, cidade, estado, tel, email
                FROM fornecedores
                ORDER BY nome
                """
            )
            return cursor.fetchall()
            
