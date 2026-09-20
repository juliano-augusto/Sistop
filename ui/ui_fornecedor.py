# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fornecedor.ui'
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

class Ui_Fornecedor(object):
    def setupUi(self, Fornecedor):
        if not Fornecedor.objectName():
            Fornecedor.setObjectName(u"Fornecedor")
        Fornecedor.resize(1224, 730)
        Fornecedor.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Fornecedor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_topo = QFrame(Fornecedor)
        self.frame_topo.setObjectName(u"frame_topo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_topo.sizePolicy().hasHeightForWidth())
        self.frame_topo.setSizePolicy(sizePolicy)
        self.frame_topo.setMinimumSize(QSize(0, 84))
        self.frame_topo.setMaximumSize(QSize(16777215, 130))
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

        self.tabFornecedor = QTabWidget(Fornecedor)
        self.tabFornecedor.setObjectName(u"tabFornecedor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabFornecedor.sizePolicy().hasHeightForWidth())
        self.tabFornecedor.setSizePolicy(sizePolicy2)
        self.tabFornecedor.setMinimumSize(QSize(1080, 510))
        self.tabFornecedor.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.tabFornecedor.setFont(font2)
        self.tabFornecedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabFornecedor.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.tabFornecedor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabFornecedor.setAutoFillBackground(False)
        self.tabFornecedor.setStyleSheet(u"background-color: rgb(106, 0, 240);\n"
"color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.tabFornecedor.setTabPosition(QTabWidget.TabPosition.North)
        self.tabFornecedor.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabFornecedor.setIconSize(QSize(16, 16))
        self.tab_novo_fornecedor = QWidget()
        self.tab_novo_fornecedor.setObjectName(u"tab_novo_fornecedor")
        self.tab_novo_fornecedor.setStyleSheet(u"text-align:center")
        self.gridLayout = QGridLayout(self.tab_novo_fornecedor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 21, 5, 1, 1)

        self.label_2 = QLabel(self.tab_novo_fornecedor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 42))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.cadastra = QPushButton(self.tab_novo_fornecedor)
        self.cadastra.setObjectName(u"cadastra")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cadastra.sizePolicy().hasHeightForWidth())
        self.cadastra.setSizePolicy(sizePolicy3)
        self.cadastra.setMinimumSize(QSize(400, 50))
        self.cadastra.setMaximumSize(QSize(16777215, 52))
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

        self.gridLayout.addWidget(self.cadastra, 17, 5, 1, 1)

        self.frame_8 = QFrame(self.tab_novo_fornecedor)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(0, 4))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_8, 19, 5, 1, 1)

        self.frame = QFrame(self.tab_novo_fornecedor)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame, 17, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 10, 1, 1, 1)

        self.label_8 = QLabel(self.tab_novo_fornecedor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 42))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 15, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 17, 6, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_11, 18, 5, 1, 1)

        self.label_5 = QLabel(self.tab_novo_fornecedor)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 42))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_9, 14, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 3, 1, 1)

        self.btn_ajuda = QToolButton(self.tab_novo_fornecedor)
        self.btn_ajuda.setObjectName(u"btn_ajuda")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_ajuda.sizePolicy().hasHeightForWidth())
        self.btn_ajuda.setSizePolicy(sizePolicy5)
        self.btn_ajuda.setMinimumSize(QSize(55, 55))
        self.btn_ajuda.setMaximumSize(QSize(52, 52))
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

        self.gridLayout.addWidget(self.btn_ajuda, 17, 7, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.tab_novo_fornecedor)
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

        self.label_7 = QLabel(self.tab_novo_fornecedor)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(200, 42))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 13, 1, 1, 1)

        self.txt_num = QLineEdit(self.tab_novo_fornecedor)
        self.txt_num.setObjectName(u"txt_num")
        sizePolicy2.setHeightForWidth(self.txt_num.sizePolicy().hasHeightForWidth())
        self.txt_num.setSizePolicy(sizePolicy2)
        self.txt_num.setMinimumSize(QSize(700, 42))
        self.txt_num.setFont(font1)
        self.txt_num.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_num, 7, 3, 1, 7)

        self.label_3 = QLabel(self.tab_novo_fornecedor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 42))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 17, 8, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.txt_end = QLineEdit(self.tab_novo_fornecedor)
        self.txt_end.setObjectName(u"txt_end")
        sizePolicy2.setHeightForWidth(self.txt_end.sizePolicy().hasHeightForWidth())
        self.txt_end.setSizePolicy(sizePolicy2)
        self.txt_end.setMinimumSize(QSize(700, 42))
        self.txt_end.setFont(font1)
        self.txt_end.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_end.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_end, 5, 3, 1, 7)

        self.txt_nome = QLineEdit(self.tab_novo_fornecedor)
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

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 1, 1, 1)

        self.label_9 = QLabel(self.tab_novo_fornecedor)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(200, 42))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 11, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 17, 4, 1, 1)

        self.frame_7 = QFrame(self.tab_novo_fornecedor)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy4.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy4)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_7, 17, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 8, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 12, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_10, 16, 5, 1, 1)

        self.txt_cnpj = QLineEdit(self.tab_novo_fornecedor)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        sizePolicy2.setHeightForWidth(self.txt_cnpj.sizePolicy().hasHeightForWidth())
        self.txt_cnpj.setSizePolicy(sizePolicy2)
        self.txt_cnpj.setMinimumSize(QSize(700, 42))
        self.txt_cnpj.setFont(font1)
        self.txt_cnpj.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_cnpj.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 3, 3, 1, 7)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_12, 20, 5, 1, 1)

        self.txt_tel = QLineEdit(self.tab_novo_fornecedor)
        self.txt_tel.setObjectName(u"txt_tel")
        sizePolicy2.setHeightForWidth(self.txt_tel.sizePolicy().hasHeightForWidth())
        self.txt_tel.setSizePolicy(sizePolicy2)
        self.txt_tel.setMinimumSize(QSize(700, 42))
        self.txt_tel.setFont(font1)
        self.txt_tel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_tel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_tel, 13, 3, 1, 7)

        self.txt_email = QLineEdit(self.tab_novo_fornecedor)
        self.txt_email.setObjectName(u"txt_email")
        sizePolicy2.setHeightForWidth(self.txt_email.sizePolicy().hasHeightForWidth())
        self.txt_email.setSizePolicy(sizePolicy2)
        self.txt_email.setMinimumSize(QSize(700, 42))
        self.txt_email.setFont(font1)
        self.txt_email.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 15, 3, 1, 7)

        self.txt_cidade = QLineEdit(self.tab_novo_fornecedor)
        self.txt_cidade.setObjectName(u"txt_cidade")
        sizePolicy2.setHeightForWidth(self.txt_cidade.sizePolicy().hasHeightForWidth())
        self.txt_cidade.setSizePolicy(sizePolicy2)
        self.txt_cidade.setMinimumSize(QSize(700, 42))
        self.txt_cidade.setFont(font1)
        self.txt_cidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_cidade.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_cidade, 9, 3, 1, 7)

        self.txt_estado = QLineEdit(self.tab_novo_fornecedor)
        self.txt_estado.setObjectName(u"txt_estado")
        sizePolicy2.setHeightForWidth(self.txt_estado.sizePolicy().hasHeightForWidth())
        self.txt_estado.setSizePolicy(sizePolicy2)
        self.txt_estado.setMinimumSize(QSize(700, 42))
        self.txt_estado.setFont(font1)
        self.txt_estado.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.txt_estado.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_estado, 11, 3, 1, 7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 10, 1, 1)

        self.label_4 = QLabel(self.tab_novo_fornecedor)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 42))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:  rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)

        self.tabFornecedor.addTab(self.tab_novo_fornecedor, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.tab)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy6)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.btn_ajuda_2 = QToolButton(self.frame_5)
        self.btn_ajuda_2.setObjectName(u"btn_ajuda_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_ajuda_2.sizePolicy().hasHeightForWidth())
        self.btn_ajuda_2.setSizePolicy(sizePolicy7)
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

        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(230)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.tabFornecedor.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabFornecedor)

        self.frame_2 = QFrame(Fornecedor)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 4))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_roxo = QFrame(Fornecedor)
        self.frame_roxo.setObjectName(u"frame_roxo")
        sizePolicy.setHeightForWidth(self.frame_roxo.sizePolicy().hasHeightForWidth())
        self.frame_roxo.setSizePolicy(sizePolicy)
        self.frame_roxo.setMinimumSize(QSize(0, 90))
        self.frame_roxo.setMaximumSize(QSize(16777215, 95))
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

        self.frame_4 = QFrame(self.frame_roxo)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy6.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy6)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_roxo)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_11 = QFrame(self.frame_roxo)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy6.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy6)
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_roxo)

        QWidget.setTabOrder(self.btn_voltar, self.btn_sair)
        QWidget.setTabOrder(self.btn_sair, self.txt_nome)
        QWidget.setTabOrder(self.txt_nome, self.txt_cnpj)
        QWidget.setTabOrder(self.txt_cnpj, self.txt_end)
        QWidget.setTabOrder(self.txt_end, self.txt_num)
        QWidget.setTabOrder(self.txt_num, self.txt_cidade)
        QWidget.setTabOrder(self.txt_cidade, self.txt_estado)
        QWidget.setTabOrder(self.txt_estado, self.txt_tel)
        QWidget.setTabOrder(self.txt_tel, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.cadastra)
        QWidget.setTabOrder(self.cadastra, self.tabFornecedor)
        QWidget.setTabOrder(self.tabFornecedor, self.textEdit)

        self.retranslateUi(Fornecedor)

        self.tabFornecedor.setCurrentIndex(0)
        self.cadastra.setDefault(True)
        self.btn_pesquisar.setDefault(True)


        QMetaObject.connectSlotsByName(Fornecedor)
    # setupUi

    def retranslateUi(self, Fornecedor):
        Fornecedor.setWindowTitle(QCoreApplication.translate("Fornecedor", u"Form", None))
        self.btn_voltar.setText(QCoreApplication.translate("Fornecedor", u"Voltar", None))
        self.textEdit.setHtml(QCoreApplication.translate("Fornecedor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Verdana'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; color:#6a00f0;\">Bem-Vindo</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:700; color:#6a00f0;\">SisTop</span></p></body></html>", None))
        self.btn_sair.setText(QCoreApplication.translate("Fornecedor", u"Sair", None))
        self.label_2.setText(QCoreApplication.translate("Fornecedor", u"CNPJ*", None))
        self.cadastra.setText(QCoreApplication.translate("Fornecedor", u"Cadastrar ", None))
        self.label_8.setText(QCoreApplication.translate("Fornecedor", u"Email*", None))
        self.label_5.setText(QCoreApplication.translate("Fornecedor", u"Cidade*", None))
        self.btn_ajuda.setText(QCoreApplication.translate("Fornecedor", u"?", None))
        self.label.setText(QCoreApplication.translate("Fornecedor", u"Nome*", None))
        self.label_7.setText(QCoreApplication.translate("Fornecedor", u"Telefone*", None))
        self.txt_num.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Ex.: 999", None))
        self.label_3.setText(QCoreApplication.translate("Fornecedor", u"Endere\u00e7o*", None))
        self.txt_end.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Endere\u00e7o", None))
        self.txt_nome.setInputMask("")
        self.txt_nome.setText("")
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Nome do fornecedor", None))
        self.label_9.setText(QCoreApplication.translate("Fornecedor", u"Estado*", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Ex.: 12345678000195", None))
        self.txt_tel.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Ex.: 45987654321", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"pessoa@email.com", None))
        self.txt_cidade.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Cidade", None))
        self.txt_estado.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Estado", None))
        self.label_4.setText(QCoreApplication.translate("Fornecedor", u"N\u00famero*", None))
        self.tabFornecedor.setTabText(self.tabFornecedor.indexOf(self.tab_novo_fornecedor), QCoreApplication.translate("Fornecedor", u"                      Cadastrar Fornecedor                   ", None))
        self.txt_buscar.setInputMask("")
        self.txt_buscar.setText("")
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("Fornecedor", u"Digite o nome do fornecedor", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("Fornecedor", u"Pesquisar", None))
        self.btn_ajuda_2.setText(QCoreApplication.translate("Fornecedor", u"?", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Fornecedor", u"Nome do fornecedor", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Fornecedor", u"CNPJ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Fornecedor", u"Endere\u00e7o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Fornecedor", u"N\u00famero", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Fornecedor", u"Cidade", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Fornecedor", u"Estado", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Fornecedor", u"Telefone", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Fornecedor", u"Email", None));
        self.tabFornecedor.setTabText(self.tabFornecedor.indexOf(self.tab), QCoreApplication.translate("Fornecedor", u"                            Consulta                               ", None))
        self.label_6.setText(QCoreApplication.translate("Fornecedor", u"F1 : Ajuda                    Backspace : Voltar", None))
    # retranslateUi

