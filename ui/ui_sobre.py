# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sobre.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

class Ui_Sobre(object):
    def setupUi(self, Sobre):
        if not Sobre.objectName():
            Sobre.setObjectName(u"Sobre")
        Sobre.resize(1200, 736)
        Sobre.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Sobre)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_topo = QFrame(Sobre)
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

        self.frame = QFrame(Sobre)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(980, 500))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(12)
        self.frame.setFont(font2)
        self.frame.setStyleSheet(u"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(790, 60))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 9, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_4, 5, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 10, 1, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_5, 5, 3, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 4, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 8, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(790, 60))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(300, 60))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 5, 2, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(300, 60))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(800, 75))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 3)


        self.verticalLayout.addWidget(self.frame)

        self.frame_6 = QFrame(Sobre)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 4))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_roxo = QFrame(Sobre)
        self.frame_roxo.setObjectName(u"frame_roxo")
        sizePolicy.setHeightForWidth(self.frame_roxo.sizePolicy().hasHeightForWidth())
        self.frame_roxo.setSizePolicy(sizePolicy)
        self.frame_roxo.setMinimumSize(QSize(0, 95))
        self.frame_roxo.setMaximumSize(QSize(16777215, 135))
        self.frame_roxo.setSizeIncrement(QSize(0, 0))
        self.frame_roxo.setStyleSheet(u"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.frame_roxo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_roxo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_roxo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_roxo)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.frame_7 = QFrame(self.frame_roxo)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_roxo)

        QWidget.setTabOrder(self.btn_voltar, self.btn_sair)
        QWidget.setTabOrder(self.btn_sair, self.textEdit)

        self.retranslateUi(Sobre)

        QMetaObject.connectSlotsByName(Sobre)
    # setupUi

    def retranslateUi(self, Sobre):
        Sobre.setWindowTitle(QCoreApplication.translate("Sobre", u"Form", None))
        self.btn_voltar.setText(QCoreApplication.translate("Sobre", u"Voltar", None))
        self.textEdit.setHtml(QCoreApplication.translate("Sobre", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Verdana'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; color:#6a00f0;\">Bem-Vindo</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:700; color:#6a00f0;\">SisTop</span></p></body></html>", None))
        self.btn_sair.setText(QCoreApplication.translate("Sobre", u"Sair", None))
        self.label_3.setText(QCoreApplication.translate("Sobre", u"Email: juliano.silva7@unioeste.br", None))
        self.label_2.setText(QCoreApplication.translate("Sobre", u"Desenvolvedor: Juliano Augusto da Silva", None))
        self.label.setText(QCoreApplication.translate("Sobre", u"Contato:", None))
        self.label_5.setText(QCoreApplication.translate("Sobre", u"Sobre:", None))
        self.label_6.setText(QCoreApplication.translate("Sobre", u"O usu\u00e1rio pode realizar o cadastro e consulta de produtos na p\u00e1gina 'Estoque'.\n"
"O usu\u00e1rio pode cadastrar fornecedores na p\u00e1gina 'Fornecedores'.", None))
        self.label_4.setText(QCoreApplication.translate("Sobre", u"Backspace : Voltar", None))
    # retranslateUi

