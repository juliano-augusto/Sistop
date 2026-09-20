# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Estoque(object):
    def setupUi(self, Estoque):
        if not Estoque.objectName():
            Estoque.setObjectName(u"Estoque")
        Estoque.resize(1200, 730)
        Estoque.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Estoque)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_topo = QFrame(Estoque)
        self.frame_topo.setObjectName(u"frame_topo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_topo.sizePolicy().hasHeightForWidth())
        self.frame_topo.setSizePolicy(sizePolicy)
        self.frame_topo.setMinimumSize(QSize(0, 95))
        self.frame_topo.setMaximumSize(QSize(16777215, 135))
        self.frame_topo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.frame_topo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_topo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_topo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_voltar = QToolButton(self.frame_topo)
        self.btn_voltar.setObjectName(u"btn_voltar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_voltar.sizePolicy().hasHeightForWidth())
        self.btn_voltar.setSizePolicy(sizePolicy1)
        self.btn_voltar.setMinimumSize(QSize(100, 60))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar.setStyleSheet(u"QToolButton{\n"
"	font: 11pt \"Verdana\";\n"
"	font: 700 13pt \"Verdana\";\n"
"	color: rgb(106, 0, 240);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_voltar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.textEdit = QTextEdit(self.frame_topo)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(700, 40))
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit.setStyleSheet(u"font: 12pt \"Verdana\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.btn_sair = QPushButton(self.frame_topo)
        self.btn_sair.setObjectName(u"btn_sair")
        sizePolicy1.setHeightForWidth(self.btn_sair.sizePolicy().hasHeightForWidth())
        self.btn_sair.setSizePolicy(sizePolicy1)
        self.btn_sair.setMinimumSize(QSize(100, 60))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.btn_sair.setFont(font1)
        self.btn_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"	color: rgb(106, 0, 240);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sair)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_topo)

        self.tabProduto = QTabWidget(Estoque)
        self.tabProduto.setObjectName(u"tabProduto")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabProduto.sizePolicy().hasHeightForWidth())
        self.tabProduto.setSizePolicy(sizePolicy2)
        self.tabProduto.setMinimumSize(QSize(1080, 510))
        self.tabProduto.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.tabProduto.setFont(font2)
        self.tabProduto.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabProduto.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.tabProduto.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabProduto.setAutoFillBackground(False)
        self.tabProduto.setStyleSheet(u"background-color: rgb(106, 0, 240);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.tabProduto.setTabPosition(QTabWidget.TabPosition.North)
        self.tabProduto.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabProduto.setIconSize(QSize(16, 16))
        self.tab_novo_produto = QWidget()
        self.tab_novo_produto.setObjectName(u"tab_novo_produto")
        self.tab_novo_produto.setStyleSheet(u"text-align:center")
        self.gridLayout = QGridLayout(self.tab_novo_produto)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 15, 8, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_6, 6, 3, 1, 1)

        self.label_7 = QLabel(self.tab_novo_produto)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(200, 42))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 11, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_8, 8, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 3, 1, 1)

        self.txt_peso = QLineEdit(self.tab_novo_produto)
        self.txt_peso.setObjectName(u"txt_peso")
        sizePolicy2.setHeightForWidth(self.txt_peso.sizePolicy().hasHeightForWidth())
        self.txt_peso.setSizePolicy(sizePolicy2)
        self.txt_peso.setMinimumSize(QSize(700, 42))
        self.txt_peso.setFont(font1)
        self.txt_peso.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_peso.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_peso, 11, 3, 1, 7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 10, 1, 1)

        self.label_4 = QLabel(self.tab_novo_produto)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 42))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)

        self.txt_marca = QLineEdit(self.tab_novo_produto)
        self.txt_marca.setObjectName(u"txt_marca")
        sizePolicy2.setHeightForWidth(self.txt_marca.sizePolicy().hasHeightForWidth())
        self.txt_marca.setSizePolicy(sizePolicy2)
        self.txt_marca.setMinimumSize(QSize(700, 42))
        self.txt_marca.setFont(font1)
        self.txt_marca.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_marca.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_marca, 3, 3, 1, 7)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 15, 4, 1, 1)

        self.cadastra = QPushButton(self.tab_novo_produto)
        self.cadastra.setObjectName(u"cadastra")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cadastra.sizePolicy().hasHeightForWidth())
        self.cadastra.setSizePolicy(sizePolicy3)
        self.cadastra.setMinimumSize(QSize(400, 52))
        self.cadastra.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.cadastra.setFont(font3)
        self.cadastra.setCursor(QCursor(Qt.PointingHandCursor))
        self.cadastra.setStyleSheet(u"QPushButton{\n"
"	color: rgb(106, 0, 240);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")
        self.cadastra.setAutoDefault(True)

        self.gridLayout.addWidget(self.cadastra, 15, 5, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_7, 2, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_5, 10, 3, 1, 1)

        self.label_2 = QLabel(self.tab_novo_produto)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 42))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_9, 12, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 16, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.btn_ajuda = QToolButton(self.tab_novo_produto)
        self.btn_ajuda.setObjectName(u"btn_ajuda")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_ajuda.sizePolicy().hasHeightForWidth())
        self.btn_ajuda.setSizePolicy(sizePolicy4)
        self.btn_ajuda.setMinimumSize(QSize(52, 52))
        self.btn_ajuda.setMaximumSize(QSize(55, 55))
        self.btn_ajuda.setFont(font)
        self.btn_ajuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajuda.setStyleSheet(u"QToolButton{\n"
"	font: 11pt \"Verdana\";\n"
"	font: 700 13pt \"Verdana\";\n"
"	color: rgb(106, 0, 240);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_ajuda, 15, 7, 1, 1)

        self.label_8 = QLabel(self.tab_novo_produto)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 42))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 13, 1, 1, 1)

        self.txt_volume = QLineEdit(self.tab_novo_produto)
        self.txt_volume.setObjectName(u"txt_volume")
        sizePolicy2.setHeightForWidth(self.txt_volume.sizePolicy().hasHeightForWidth())
        self.txt_volume.setSizePolicy(sizePolicy2)
        self.txt_volume.setMinimumSize(QSize(700, 42))
        self.txt_volume.setFont(font1)
        self.txt_volume.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_volume.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_volume, 13, 3, 1, 7)

        self.txt_quant = QLineEdit(self.tab_novo_produto)
        self.txt_quant.setObjectName(u"txt_quant")
        sizePolicy2.setHeightForWidth(self.txt_quant.sizePolicy().hasHeightForWidth())
        self.txt_quant.setSizePolicy(sizePolicy2)
        self.txt_quant.setMinimumSize(QSize(700, 42))
        self.txt_quant.setFont(font1)
        self.txt_quant.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_quant.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_quant, 7, 3, 1, 7)

        self.label_3 = QLabel(self.tab_novo_produto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 42))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)

        self.label = QLabel(self.tab_novo_produto)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(200, 42))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.txt_nome = QLineEdit(self.tab_novo_produto)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy2.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy2)
        self.txt_nome.setMinimumSize(QSize(700, 42))
        self.txt_nome.setFont(font1)
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 3, 1, 7)

        self.txt_sabor = QLineEdit(self.tab_novo_produto)
        self.txt_sabor.setObjectName(u"txt_sabor")
        sizePolicy2.setHeightForWidth(self.txt_sabor.sizePolicy().hasHeightForWidth())
        self.txt_sabor.setSizePolicy(sizePolicy2)
        self.txt_sabor.setMinimumSize(QSize(700, 42))
        self.txt_sabor.setFont(font1)
        self.txt_sabor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_sabor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_sabor, 5, 3, 1, 7)

        self.txt_preco = QLineEdit(self.tab_novo_produto)
        self.txt_preco.setObjectName(u"txt_preco")
        sizePolicy2.setHeightForWidth(self.txt_preco.sizePolicy().hasHeightForWidth())
        self.txt_preco.setSizePolicy(sizePolicy2)
        self.txt_preco.setMinimumSize(QSize(700, 42))
        self.txt_preco.setFont(font1)
        self.txt_preco.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_preco.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_preco, 9, 3, 1, 7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 14, 5, 1, 1)

        self.label_5 = QLabel(self.tab_novo_produto)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 42))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 15, 6, 1, 1)

        self.tabProduto.addTab(self.tab_novo_produto, "")
        self.tab_consulta = QWidget()
        self.tab_consulta.setObjectName(u"tab_consulta")
        self.tab_consulta.setStyleSheet(u"background-color: rgb(106, 0, 240);")
        self.verticalLayout_2 = QVBoxLayout(self.tab_consulta)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.tab_consulta)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(1060, 45))
        self.frame_5.setStyleSheet(u"background-color: rgb(106, 0, 240);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.txt_buscar = QLineEdit(self.frame_5)
        self.txt_buscar.setObjectName(u"txt_buscar")
        sizePolicy2.setHeightForWidth(self.txt_buscar.sizePolicy().hasHeightForWidth())
        self.txt_buscar.setSizePolicy(sizePolicy2)
        self.txt_buscar.setMinimumSize(QSize(650, 40))
        self.txt_buscar.setFont(font1)
        self.txt_buscar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_buscar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_buscar)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.btn_pesquisar = QPushButton(self.frame_5)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        sizePolicy2.setHeightForWidth(self.btn_pesquisar.sizePolicy().hasHeightForWidth())
        self.btn_pesquisar.setSizePolicy(sizePolicy2)
        self.btn_pesquisar.setMinimumSize(QSize(250, 40))
        self.btn_pesquisar.setFont(font3)
        self.btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(106, 0, 240);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")
        self.btn_pesquisar.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.btn_pesquisar)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy5)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.btn_ajuda_2 = QToolButton(self.frame_5)
        self.btn_ajuda_2.setObjectName(u"btn_ajuda_2")
        sizePolicy4.setHeightForWidth(self.btn_ajuda_2.sizePolicy().hasHeightForWidth())
        self.btn_ajuda_2.setSizePolicy(sizePolicy4)
        self.btn_ajuda_2.setMinimumSize(QSize(60, 60))
        self.btn_ajuda_2.setFont(font)
        self.btn_ajuda_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajuda_2.setStyleSheet(u"QToolButton{\n"
"	font: 11pt \"Verdana\";\n"
"	font: 700 13pt \"Verdana\";\n"
"	color: rgb(106, 0, 240);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_ajuda_2)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.tableWidget = QTableWidget(self.tab_consulta)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(10)
        font4.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(11)
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color:rgb(106, 0, 240);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"QTableWidget{\n"
"	background-color:rgb(255, 255, 255);\n"
"}")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.tabProduto.addTab(self.tab_consulta, "")

        self.verticalLayout.addWidget(self.tabProduto)

        self.frame_roxo = QFrame(Estoque)
        self.frame_roxo.setObjectName(u"frame_roxo")
        sizePolicy.setHeightForWidth(self.frame_roxo.sizePolicy().hasHeightForWidth())
        self.frame_roxo.setSizePolicy(sizePolicy)
        self.frame_roxo.setMinimumSize(QSize(0, 95))
        self.frame_roxo.setMaximumSize(QSize(16777215, 100))
        self.frame_roxo.setSizeIncrement(QSize(0, 0))
        self.frame_roxo.setStyleSheet(u"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.frame_roxo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_roxo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_roxo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_roxo)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 50))
        self.label_6.setMaximumSize(QSize(16777215, 60))
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.frame_roxo)

        self.frame_topo.raise_()
        self.frame_roxo.raise_()
        self.tabProduto.raise_()
        QWidget.setTabOrder(self.btn_voltar, self.btn_sair)
        QWidget.setTabOrder(self.btn_sair, self.tabProduto)
        QWidget.setTabOrder(self.tabProduto, self.txt_nome)
        QWidget.setTabOrder(self.txt_nome, self.txt_marca)
        QWidget.setTabOrder(self.txt_marca, self.txt_sabor)
        QWidget.setTabOrder(self.txt_sabor, self.txt_quant)
        QWidget.setTabOrder(self.txt_quant, self.txt_preco)
        QWidget.setTabOrder(self.txt_preco, self.txt_peso)
        QWidget.setTabOrder(self.txt_peso, self.txt_volume)
        QWidget.setTabOrder(self.txt_volume, self.cadastra)
        QWidget.setTabOrder(self.cadastra, self.txt_buscar)
        QWidget.setTabOrder(self.txt_buscar, self.btn_pesquisar)
        QWidget.setTabOrder(self.btn_pesquisar, self.btn_ajuda_2)
        QWidget.setTabOrder(self.btn_ajuda_2, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.textEdit)

        self.retranslateUi(Estoque)

        self.tabProduto.setCurrentIndex(0)
        self.cadastra.setDefault(True)
        self.btn_pesquisar.setDefault(True)


        QMetaObject.connectSlotsByName(Estoque)
    # setupUi

    def retranslateUi(self, Estoque):
        Estoque.setWindowTitle(QCoreApplication.translate("Estoque", u"Form", None))
        self.btn_voltar.setText(QCoreApplication.translate("Estoque", u"Voltar", None))
        self.textEdit.setHtml(QCoreApplication.translate("Estoque", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Verdana'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; color:#6a00f0;\">Bem-Vindo</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:700; color:#6a00f0;\">SisTop</span></p></body></html>", None))
        self.btn_sair.setText(QCoreApplication.translate("Estoque", u"Sair", None))
        self.label_7.setText(QCoreApplication.translate("Estoque", u"Peso (Kg)", None))
        self.txt_peso.setPlaceholderText(QCoreApplication.translate("Estoque", u"Ex.: 0.2", None))
        self.label_4.setText(QCoreApplication.translate("Estoque", u"Quantidade*", None))
        self.txt_marca.setPlaceholderText(QCoreApplication.translate("Estoque", u"Marca do produto", None))
        self.cadastra.setText(QCoreApplication.translate("Estoque", u"Cadastrar", None))
        self.label_2.setText(QCoreApplication.translate("Estoque", u"Marca*", None))
        self.btn_ajuda.setText(QCoreApplication.translate("Estoque", u"?", None))
        self.label_8.setText(QCoreApplication.translate("Estoque", u"Volume (L)", None))
        self.txt_volume.setPlaceholderText(QCoreApplication.translate("Estoque", u"Ex.: 1.5", None))
        self.txt_quant.setPlaceholderText(QCoreApplication.translate("Estoque", u"Ex.: 100", None))
        self.label_3.setText(QCoreApplication.translate("Estoque", u"Sabor*", None))
        self.label.setText(QCoreApplication.translate("Estoque", u"Nome*", None))
        self.txt_nome.setInputMask("")
        self.txt_nome.setText("")
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("Estoque", u"Nome do produto", None))
        self.txt_sabor.setPlaceholderText(QCoreApplication.translate("Estoque", u"Sabor do produto", None))
        self.txt_preco.setPlaceholderText(QCoreApplication.translate("Estoque", u"Ex.: 9.99", None))
        self.label_5.setText(QCoreApplication.translate("Estoque", u"Pre\u00e7o*", None))
        self.tabProduto.setTabText(self.tabProduto.indexOf(self.tab_novo_produto), QCoreApplication.translate("Estoque", u"                           Novo Produto                          ", None))
        self.txt_buscar.setInputMask("")
        self.txt_buscar.setText("")
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("Estoque", u"Digite o nome do produto", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("Estoque", u"Pesquisar", None))
        self.btn_ajuda_2.setText(QCoreApplication.translate("Estoque", u"?", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Estoque", u"Nome do produto", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Estoque", u"Marca", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Estoque", u"Sabor", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Estoque", u"Quantidade", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Estoque", u"Pre\u00e7o", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Estoque", u"Peso (Kg)", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Estoque", u"Volume (L)", None));
        self.tabProduto.setTabText(self.tabProduto.indexOf(self.tab_consulta), QCoreApplication.translate("Estoque", u"                              Consulta                              ", None))
        self.label_6.setText(QCoreApplication.translate("Estoque", u"F1 : Ajuda                     Backspace : Voltar", None))
    # retranslateUi

