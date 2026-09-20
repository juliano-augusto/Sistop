
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem)
from PySide6.QtGui import QKeySequence
from ui.ui_login import Ui_login
from ui.ui_menu import Ui_menu_principal
from ui.ui_cadastro1 import Ui_Estoque
from ui.ui_sobre import Ui_Sobre
from ui.ui_fornecedor import Ui_Fornecedor
from ui.ui_vendas import Ui_Vendas
from control import control_user, control_produto, control_fornecedor
import sys

class tela_Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(tela_Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.ajuda.setShortcut(QKeySequence("F1"))
        self.controle_usuario = control_user()
        self.entrar.clicked.connect(self.open_system)
        self.ajuda.clicked.connect(self.show_help)

    def open_system(self):
    
        verifica = self.controle_usuario.obter_login(self.txt_usuario.text(), self.txt_senha.text())
        if (verifica):
            self.w = tela_Menu()
            self.w.show()
            self.close()
            
        else:
            QMessageBox.information(self, "Senha Inválida", "Senha Inválida")
        
    def show_help(self):
        QMessageBox.information(self, "Ajuda", "Caso tenha perdido a senha, entre em contato com o administrador do sistema.")

        
class tela_Menu(QMainWindow, Ui_menu_principal):
    def __init__(self):
        super(tela_Menu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SisTop")
        
        self.btn_ajuda.setShortcut(QKeySequence("F1"))
        self.btn_estoque.setShortcut(QKeySequence("F2"))
        self.btn_fornecedores.setShortcut(QKeySequence("F3"))
        self.btn_sobre.setShortcut(QKeySequence("F10"))
        
        self.btn_sair.clicked.connect(self.exit_system)
        self.btn_ajuda.clicked.connect(self.ajuda_menu)
        self.btn_estoque.clicked.connect(self.open_estoque)
        self.btn_vendas.clicked.connect(self.open_venda)
        self.btn_sobre.clicked.connect(self.open_sobre)
        self.btn_fornecedores.clicked.connect(self.open_fornecedor)
        
    def ajuda_menu(self):
        QMessageBox.information(self, "Ajuda", "Para mais informações acesse a página 'Sobre'.")

    def open_venda(self):
        self.w = tela_Vendas()
        self.w.show()
        self.close()
        
    def open_sobre(self):
        self.w = tela_Sobre()
        self.w.show()
        self.close()
        
    def open_estoque(self):
        self.w = tela_Estoque()
        self.w.show()
        self.close()
        
    def open_fornecedor(self):
        self.w = tela_Fornecedor()
        self.w.show()
        self.close()
        
    def exit_system(self):
        reply = QMessageBox.question(self, 'Sair do Sistema', 'Tem certeza que deseja sair do sistema?', 
                                     QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.w = tela_Login()
            self.w.show()
            self.close()
            
class tela_Sobre(QWidget, Ui_Sobre):
    def __init__(self):
        super(tela_Sobre, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sobre")
        self.btn_voltar.setShortcut(QKeySequence("Backspace"))
        self.btn_voltar.clicked.connect(self.voltar)
        self.btn_sair.clicked.connect(self.exit_system)
        
    def exit_system(self):
        reply = QMessageBox.question(self, 'Sair do Sistema', 'Tem certeza que deseja sair do sistema?', 
                                     QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.w = tela_Login()
            self.w.show()
            self.close()
        
    def voltar(self):
        self.w = tela_Menu()
        self.w.show()
        self.close()
            
class tela_Estoque(QWidget, Ui_Estoque):
    def __init__(self):
        super(tela_Estoque, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Estoque")
        self.btn_voltar.setShortcut(QKeySequence("Backspace"))
        self.controle_produto = control_produto()
        
        self.cadastra.clicked.connect(self.cadastro_produto)
        self.btn_voltar.clicked.connect(self.volta_menu)
        self.btn_pesquisar.clicked.connect(self.consulta_produto)
        self.btn_sair.clicked.connect(self.exit_system)
        self.btn_ajuda.clicked.connect(self.ajuda_estoque)
        self.btn_ajuda_2.clicked.connect(self.ajuda_estoque_1)
        self.btn_ajuda.setShortcut(QKeySequence("F1"))
        self.btn_ajuda_2.setShortcut(QKeySequence("F1"))

    def ajuda_estoque(self):
        QMessageBox.information(self, "Ajuda", "Campos com '*' é obrigatório o preenchimento.")

    def ajuda_estoque_1(self):
        QMessageBox.information(self, "Ajuda", "Digite o nome do produto para filtrar a pesquisa.")

    def exit_system(self):
        reply = QMessageBox.question(self, 'Sair do Sistema', 'Tem certeza que deseja sair do sistema?',
                                     QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.w = tela_Login()
            self.w.show()
            self.close()

    def volta_menu(self):
        self.w = tela_Menu()
        self.w.show()
        self.close()

    def cadastro_produto(self):
        try:
            nome = self.txt_nome.text()
            marca = self.txt_marca.text()
            sabor = self.txt_sabor.text()
            quantidade = int(self.txt_quant.text())
            preco = float(self.txt_preco.text())
            peso = float(self.txt_peso.text() or "0")
            volume = float(self.txt_volume.text() or "0")
            retorno = self.controle_produto.dados_cadastro(nome, marca, sabor, quantidade, preco, peso, volume)
            if not retorno:
                raise ValueError
            QMessageBox.information(self, "Cadastro", "Cadastro realizado com sucesso")

            self.txt_nome.clear()
            self.txt_marca.clear()
            self.txt_sabor.clear()
            self.txt_quant.clear()
            self.txt_preco.clear()
            self.txt_peso.clear()
            self.txt_volume.clear()
        except ValueError:
            QMessageBox.critical(self, "Erro", "Preencha corretamente os campos com '*'.")

    def consulta_produto(self):
        name = self.txt_buscar.text()
        resultado_busca = self.controle_produto.dados_busca(name)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(resultado_busca))
        for row_num, row_data in enumerate(resultado_busca):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
        if not resultado_busca:
            QMessageBox.warning(self, "Consulta", "Produto não cadastrado.")
        self.txt_buscar.clear()


class tela_Vendas(QWidget, Ui_Vendas):
    def __init__(self):
        super(tela_Vendas, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Vendas")
        self.btn_voltar.setShortcut(QKeySequence("Backspace"))
        self.controle_produto = control_produto()

        self.btn_voltar.clicked.connect(self.volta_menu)
        self.btn_sair.clicked.connect(self.exit_system)
        self.btn_confirmar.clicked.connect(self.registrar_venda)
        self.txt_quantidade.valueChanged.connect(self.atualiza_total)

    def atualiza_total(self):
        nome = self.txt_nome.text().strip()
        quantidade = self.txt_quantidade.value()
        if not nome:
            self.txt_total.setText("R$ 0,00")
            return

        produto = self.controle_produto.db.busca_produto_por_nome(nome)
        if not produto:
            self.txt_total.setText("R$ 0,00")
            return

        preco = produto[4]
        total = preco * quantidade
        self.txt_total.setText(f"R$ {total:.2f}")

    def registrar_venda(self):
        nome = self.txt_nome.text().strip()
        quantidade = self.txt_quantidade.value()

        if not nome:
            QMessageBox.warning(self, "Erro", "Informe o nome do produto.")
            return

        try:
            sucesso = self.controle_produto.vender_produto(nome, quantidade)
            if sucesso:
                QMessageBox.information(self, "Venda", "Venda registrada com sucesso!")
                self.txt_nome.clear()
                self.txt_quantidade.setValue(1)
                self.txt_total.setText("R$ 0,00")
            else:
                QMessageBox.warning(self, "Estoque insuficiente", "Produto não encontrado ou quantidade indisponível.")
        except Exception as exc:
            QMessageBox.critical(self, "Erro", f"Não foi possível registrar a venda:\n{exc}")

    def exit_system(self):
        reply = QMessageBox.question(self, 'Sair do Sistema', 'Tem certeza que deseja sair do sistema?',
                                     QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.w = tela_Login()
            self.w.show()
            self.close()

    def volta_menu(self):
        self.w = tela_Menu()
        self.w.show()
        self.close()
                
class tela_Fornecedor(QWidget, Ui_Fornecedor):
    def __init__(self):
        super(tela_Fornecedor, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Fornecedores")
        self.btn_voltar.setShortcut(QKeySequence("Backspace"))
        self.btn_ajuda.setShortcut(QKeySequence("F1"))
        self.controle_fornecedor = control_fornecedor()
        
        self.btn_pesquisar.clicked.connect(self.consulta_fornecedor)
        self.btn_voltar.clicked.connect(self.voltar)
        self.btn_sair.clicked.connect(self.exit_system)
        self.cadastra.clicked.connect(self.cad_fornecedor)
        self.btn_ajuda.clicked.connect(self.ajuda)
        
    def ajuda(self):
        QMessageBox.information(self, "Ajuda", "Campos com '*' é obrigatório o preenchimento.")
        
    def exit_system(self):
        reply = QMessageBox.question(self, 'Sair do Sistema', 'Tem certeza que deseja sair do sistema?', 
                                     QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.w = tela_Login()
            self.w.show()
            self.close()
            
    def voltar(self):
        self.w = tela_Menu()
        self.w.show()
        self.close()
        
    def cad_fornecedor(self):
        try:
            nome = self.txt_nome.text()
            cn = self.txt_cnpj.text()
            if len(cn) != 14:
                raise ValueError
            cnpj = int(cn)
            end = self.txt_end.text()
            num = self.txt_num.text()
            numero = int(num)
            cidade = self.txt_cidade.text()
            estado = self.txt_estado.text()
            tel = self.txt_tel.text()
            if len(tel) != 11:
                raise ValueError
            telefone = int(tel)
            email = self.txt_email.text()
            result = self.controle_fornecedor.dados_fornecedor(nome, cnpj, end, numero, cidade, estado, telefone, email)
            if not result:
                raise Exception
            QMessageBox.information(self, "Cadastro", "Cadastro realizado com sucesso")
        
            self.txt_nome.setText("")
            self.txt_cnpj.setText("")
            self.txt_end.setText("")
            self.txt_num.setText("")
            self.txt_cidade.setText("")
            self.txt_estado.setText("")
            self.txt_tel.setText("")
            self.txt_email.setText("")
        except ValueError as e:
            QMessageBox.critical(self, "Erro", "Preencha corretamente os campos com '*'")
        except Exception:
            QMessageBox.critical(self, "Erro", "CNPJ já cadastrado")
            
    def consulta_fornecedor(self):
        name = self.txt_buscar.text()
        resultado_busca = self.controle_fornecedor.buscar_fornecedor(name)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(resultado_busca))
        for row_num, row_data in enumerate(resultado_busca):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
        if not resultado_busca:
            QMessageBox.warning(self, "Consulta", "Fornecedor não cadastrado.")
        self.txt_buscar.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ini = control_user()
    ini.inicializa()
    window = tela_Login()
    window.show()
    app.exec()
