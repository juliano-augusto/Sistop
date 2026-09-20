# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_menu_principal(object):
    def setupUi(self, menu_principal):
        if not menu_principal.objectName():
            menu_principal.setObjectName(u"menu_principal")
        menu_principal.resize(1200, 720)
        menu_principal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(menu_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_topo = QFrame(self.centralwidget)
        self.frame_topo.setObjectName(u"frame_topo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_topo.sizePolicy().hasHeightForWidth())
        self.frame_topo.setSizePolicy(sizePolicy)
        self.frame_topo.setMinimumSize(QSize(0, 120))
        self.frame_topo.setMaximumSize(QSize(16777215, 135))
        self.frame_topo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.frame_topo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_topo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_topo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_ajuda = QToolButton(self.frame_topo)
        self.btn_ajuda.setObjectName(u"btn_ajuda")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_ajuda.sizePolicy().hasHeightForWidth())
        self.btn_ajuda.setSizePolicy(sizePolicy1)
        self.btn_ajuda.setMinimumSize(QSize(60, 60))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
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

        self.horizontalLayout.addWidget(self.btn_ajuda)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.textEdit = QTextEdit(self.frame_topo)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(700, 50))
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

        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 450))
        self.frame_menu.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.btn_vendas = QPushButton(self.frame_menu)
        self.btn_vendas.setObjectName(u"btn_vendas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_vendas.sizePolicy().hasHeightForWidth())
        self.btn_vendas.setSizePolicy(sizePolicy2)
        self.btn_vendas.setMinimumSize(QSize(200, 100))
        self.btn_vendas.setFont(font1)
        self.btn_vendas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_vendas.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(106, 0, 240);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_vendas, 1, 3, 1, 1)

        self.btn_sobre = QPushButton(self.frame_menu)
        self.btn_sobre.setObjectName(u"btn_sobre")
        sizePolicy2.setHeightForWidth(self.btn_sobre.sizePolicy().hasHeightForWidth())
        self.btn_sobre.setSizePolicy(sizePolicy2)
        self.btn_sobre.setMinimumSize(QSize(200, 100))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(106, 0, 240);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_sobre, 3, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 6, 1, 1)

        self.btn_relatorios = QPushButton(self.frame_menu)
        self.btn_relatorios.setObjectName(u"btn_relatorios")
        sizePolicy2.setHeightForWidth(self.btn_relatorios.sizePolicy().hasHeightForWidth())
        self.btn_relatorios.setSizePolicy(sizePolicy2)
        self.btn_relatorios.setMinimumSize(QSize(200, 100))
        self.btn_relatorios.setFont(font1)
        self.btn_relatorios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorios.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(106, 0, 240);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_relatorios, 1, 5, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.btn_estoque = QPushButton(self.frame_menu)
        self.btn_estoque.setObjectName(u"btn_estoque")
        sizePolicy2.setHeightForWidth(self.btn_estoque.sizePolicy().hasHeightForWidth())
        self.btn_estoque.setSizePolicy(sizePolicy2)
        self.btn_estoque.setMinimumSize(QSize(200, 100))
        self.btn_estoque.setFont(font1)
        self.btn_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(106, 0, 240);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_estoque, 1, 1, 1, 1)

        self.btn_compras = QPushButton(self.frame_menu)
        self.btn_compras.setObjectName(u"btn_compras")
        sizePolicy2.setHeightForWidth(self.btn_compras.sizePolicy().hasHeightForWidth())
        self.btn_compras.setSizePolicy(sizePolicy2)
        self.btn_compras.setMinimumSize(QSize(200, 100))
        self.btn_compras.setFont(font1)
        self.btn_compras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_compras.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(106, 0, 240);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_compras, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.btn_fornecedores = QPushButton(self.frame_menu)
        self.btn_fornecedores.setObjectName(u"btn_fornecedores")
        sizePolicy2.setHeightForWidth(self.btn_fornecedores.sizePolicy().hasHeightForWidth())
        self.btn_fornecedores.setSizePolicy(sizePolicy2)
        self.btn_fornecedores.setMinimumSize(QSize(200, 100))
        self.btn_fornecedores.setFont(font1)
        self.btn_fornecedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fornecedores.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(106, 0, 240);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_fornecedores, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 4, 1, 1)


        self.verticalLayout.addWidget(self.frame_menu)

        self.frame_roxo = QFrame(self.centralwidget)
        self.frame_roxo.setObjectName(u"frame_roxo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_roxo.sizePolicy().hasHeightForWidth())
        self.frame_roxo.setSizePolicy(sizePolicy3)
        self.frame_roxo.setMinimumSize(QSize(0, 120))
        self.frame_roxo.setMaximumSize(QSize(16777215, 135))
        self.frame_roxo.setStyleSheet(u"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.frame_roxo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_roxo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_roxo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_roxo)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_roxo)

        menu_principal.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_ajuda, self.btn_sair)
        QWidget.setTabOrder(self.btn_sair, self.btn_estoque)
        QWidget.setTabOrder(self.btn_estoque, self.btn_vendas)
        QWidget.setTabOrder(self.btn_vendas, self.btn_relatorios)
        QWidget.setTabOrder(self.btn_relatorios, self.btn_fornecedores)
        QWidget.setTabOrder(self.btn_fornecedores, self.btn_compras)
        QWidget.setTabOrder(self.btn_compras, self.btn_sobre)
        QWidget.setTabOrder(self.btn_sobre, self.textEdit)

        self.retranslateUi(menu_principal)

        QMetaObject.connectSlotsByName(menu_principal)
    # setupUi

    def retranslateUi(self, menu_principal):
        menu_principal.setWindowTitle(QCoreApplication.translate("menu_principal", u"MainWindow", None))
        self.btn_ajuda.setText(QCoreApplication.translate("menu_principal", u"?", None))
        self.textEdit.setHtml(QCoreApplication.translate("menu_principal", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Verdana'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; color:#6a00f0;\">Bem-Vindo</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:700; color:#6a00f0;\">SisTop</span></p></body></html>", None))
        self.btn_sair.setText(QCoreApplication.translate("menu_principal", u"Sair", None))
        self.btn_vendas.setText(QCoreApplication.translate("menu_principal", u"Vendas", None))
        self.btn_sobre.setText(QCoreApplication.translate("menu_principal", u"Sobre", None))
        self.btn_relatorios.setText(QCoreApplication.translate("menu_principal", u"Relat\u00f3rios", None))
        self.btn_estoque.setText(QCoreApplication.translate("menu_principal", u"Estoque", None))
        self.btn_compras.setText(QCoreApplication.translate("menu_principal", u"Compras", None))
        self.btn_fornecedores.setText(QCoreApplication.translate("menu_principal", u"Fornecedores", None))
        self.label.setText(QCoreApplication.translate("menu_principal", u"F1 : Ajuda                    F2 : Estoque                    F3 : Fornecedores                  F10 : Sobre                         ", None))
    # retranslateUi

