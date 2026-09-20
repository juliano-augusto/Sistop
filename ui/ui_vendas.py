# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vendas.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout, QWidget)


class Ui_Vendas(object):
    def setupUi(self, Vendas):
        if not Vendas.objectName():
            Vendas.setObjectName(u"Vendas")
        Vendas.resize(1200, 720)
        Vendas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Vendas)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.frame_topo = QFrame(Vendas)
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
"\tfont: 11pt \"Verdana\";\n"
"\tfont: 700 13pt \"Verdana\";\n"
"\tcolor: rgb(106, 0, 240);\n"
"\tbackground-color: rgb(255, 255, 255);\n"
"\tborder-radius:10px\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"\tcolor: rgb(255, 255, 255);\n"
"\tbackground-color: rgb(130, 0, 255);\n"
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
"\tcolor: rgb(106, 0, 240);\n"
"\tbackground-color: rgb(255, 255, 255);\n"
"\tborder-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\tcolor: rgb(255, 255, 255);\n"
"\tbackground-color: rgb(130, 0, 255);\n"
"}")
        self.horizontalLayout.addWidget(self.btn_sair)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_2)
        self.verticalLayout.addWidget(self.frame_topo)

        self.tabVendas = QTabWidget(Vendas)
        self.tabVendas.setObjectName(u"tabVendas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabVendas.sizePolicy().hasHeightForWidth())
        self.tabVendas.setSizePolicy(sizePolicy2)
        self.tabVendas.setMinimumSize(QSize(1080, 510))
        self.tabVendas.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.tabVendas.setFont(font2)
        self.tabVendas.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabVendas.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.tabVendas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabVendas.setAutoFillBackground(False)
        self.tabVendas.setStyleSheet(u"background-color: rgb(106, 0, 240);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.tabVendas.setTabPosition(QTabWidget.TabPosition.North)
        self.tabVendas.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabVendas.setIconSize(QSize(16, 16))

        self.tab_nova_venda = QWidget()
        self.tab_nova_venda.setObjectName(u"tab_nova_venda")
        self.tab_nova_venda.setStyleSheet(u"text-align:center")
        self.gridLayout = QGridLayout(self.tab_nova_venda)
        self.gridLayout.setObjectName(u"gridLayout")

        self.label_produto = QLabel(self.tab_nova_venda)
        self.label_produto.setObjectName(u"label_produto")
        self.label_produto.setMinimumSize(QSize(200, 42))
        self.label_produto.setFont(font1)
        self.label_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_produto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_produto, 1, 1, 1, 1)

        self.txt_nome = QLineEdit(self.tab_nova_venda)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(700, 42))
        self.txt_nome.setFont(font1)
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.txt_nome, 1, 3, 1, 7)

        self.label_quantidade = QLabel(self.tab_nova_venda)
        self.label_quantidade.setObjectName(u"label_quantidade")
        self.label_quantidade.setMinimumSize(QSize(200, 42))
        self.label_quantidade.setFont(font1)
        self.label_quantidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_quantidade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_quantidade, 3, 1, 1, 1)

        self.txt_quantidade = QSpinBox(self.tab_nova_venda)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        self.txt_quantidade.setMinimumSize(QSize(200, 42))
        self.txt_quantidade.setMinimum(1)
        self.txt_quantidade.setMaximum(9999)
        self.txt_quantidade.setFont(font1)
        self.txt_quantidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.gridLayout.addWidget(self.txt_quantidade, 3, 3, 1, 1)

        self.label_total = QLabel(self.tab_nova_venda)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setMinimumSize(QSize(200, 42))
        self.label_total.setFont(font1)
        self.label_total.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.label_total, 5, 1, 1, 1)

        self.txt_total = QLineEdit(self.tab_nova_venda)
        self.txt_total.setObjectName(u"txt_total")
        self.txt_total.setMinimumSize(QSize(400, 42))
        self.txt_total.setFont(font1)
        self.txt_total.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_total.setReadOnly(True)
        self.txt_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.txt_total, 5, 3, 1, 4)

        self.btn_confirmar = QPushButton(self.tab_nova_venda)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_confirmar.sizePolicy().hasHeightForWidth())
        self.btn_confirmar.setSizePolicy(sizePolicy3)
        self.btn_confirmar.setMinimumSize(QSize(400, 50))
        self.btn_confirmar.setMaximumSize(QSize(16777215, 52))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.btn_confirmar.setFont(font3)
        self.btn_confirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirmar.setStyleSheet(u"QPushButton{\n"
"\tcolor: rgb(106, 0, 240);\n"
"\tbackground-color: rgb(255, 255, 255);\n"
"\tborder-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\tcolor: rgb(255, 255, 255);\n"
"\tbackground-color: rgb(130, 0, 255);\n"
"}")
        self.gridLayout.addWidget(self.btn_confirmar, 7, 3, 1, 1)

        self.tableWidget = QTableWidget(self.tab_nova_venda)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Produto", "Marca", "Quantidade", "Preço"])
        self.tableWidget.setStyleSheet(u"background-color: rgb(255,255,255); color: rgb(106, 0, 240); border-radius:10px")
        self.gridLayout.addWidget(self.tableWidget, 9, 1, 3, 9)

        self.tabVendas.addTab(self.tab_nova_venda, "")
        self.verticalLayout.addWidget(self.tabVendas)

        self.retranslateUi(Vendas)
        QMetaObject.connectSlotsByName(Vendas)

    def retranslateUi(self, Vendas):
        Vendas.setWindowTitle(QCoreApplication.translate("Vendas", u"Vendas", None))
        self.btn_voltar.setText(QCoreApplication.translate("Vendas", u"Voltar", None))
        self.textEdit.setHtml(QCoreApplication.translate("Vendas", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Verdana'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; color:#6a00f0;\">Controle de</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:700; color:#6a00f0;\">Vendas</span></p></body></html>", None))
        self.btn_sair.setText(QCoreApplication.translate("Vendas", u"Sair", None))
        self.label_produto.setText(QCoreApplication.translate("Vendas", u"Produto*", None))
        self.label_quantidade.setText(QCoreApplication.translate("Vendas", u"Quantidade*", None))
        self.label_total.setText(QCoreApplication.translate("Vendas", u"Total", None))
        self.btn_confirmar.setText(QCoreApplication.translate("Vendas", u"Confirmar", None))
        self.tabVendas.setTabText(self.tabVendas.indexOf(self.tab_nova_venda), QCoreApplication.translate("Vendas", u"Nova venda", None))
