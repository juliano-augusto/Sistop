from database import Usuario, Produtos, Fornecedores


class control_user:
    def __init__(self):
        self.user = Usuario()
        self.prod = Produtos()
        self.forn = Fornecedores()

    def inicializa(self):
        self.user.cria_tabela_usuarios()
        self.user.insere_usuario_padrao()
        self.prod.cria_tabela_produto()
        self.forn.cria_tabela_fornecedor()

    def obter_login(self, username, password):
        autenticado = self.user.autenticacao(username, password)
        return autenticado == "user"


class control_produto:
    def __init__(self):
        self.db = Produtos()

    def dados_cadastro(self, nome, marca, sabor, quantidade, preco, peso, volume):
        return self.db.insere_produto(nome, marca, sabor, quantidade, preco, peso, volume)

    def dados_busca(self, nome):
        termo = (nome or "").strip()
        if not termo:
            return self.db.listar_produtos()
        return self.db.busca_produto(termo)

    def vender_produto(self, nome, quantidade):
        nome = (nome or "").strip()
        quantidade = int(quantidade)

        if not nome or quantidade <= 0:
            return False

        produto = self.db.busca_produto_por_nome(nome)
        if not produto:
            return False

        _, _, _, quantidade_atual, _, _, _ = produto
        if quantidade_atual < quantidade:
            return False

        nova_quantidade = quantidade_atual - quantidade
        return self.db.atualiza_estoque(nome, nova_quantidade)


class control_fornecedor:
    def __init__(self):
        self.db = Fornecedores()

    def dados_fornecedor(self, nome, cnpj, end, numero, cidade, estado, tel, email):
        return self.db.insert_fornecedor(nome, cnpj, end, numero, cidade, estado, tel, email)

    def buscar_fornecedor(self, nome):
        termo = (nome or "").strip()
        if not termo:
            return self.db.listar_fornecedores()
        return self.db.busca_fornecedor(termo)