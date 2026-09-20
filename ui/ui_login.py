# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1200, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QSize(0, 0))
        login.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(login)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.txt_usuario = QLineEdit(self.frame_2)
        self.txt_usuario.setObjectName(u"txt_usuario")
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setMinimumSize(QSize(250, 40))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"color: rgb(106, 0, 240);")

        self.gridLayout.addWidget(self.txt_usuario, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.entrar = QPushButton(self.frame_2)
        self.entrar.setObjectName(u"entrar")
        sizePolicy.setHeightForWidth(self.entrar.sizePolicy().hasHeightForWidth())
        self.entrar.setSizePolicy(sizePolicy)
        self.entrar.setMinimumSize(QSize(260, 50))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.entrar.setFont(font1)
        self.entrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(106, 0, 240);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(130, 0, 255);\n"
"}\n"
"")
        self.entrar.setIconSize(QSize(503, 30))
        self.entrar.setAutoDefault(True)

        self.gridLayout.addWidget(self.entrar, 5, 1, 1, 1)

        self.ajuda = QToolButton(self.frame_2)
        self.ajuda.setObjectName(u"ajuda")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ajuda.sizePolicy().hasHeightForWidth())
        self.ajuda.setSizePolicy(sizePolicy2)
        self.ajuda.setMinimumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        self.ajuda.setFont(font2)
        self.ajuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.ajuda.setStyleSheet(u"QToolButton{\n"
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

        self.gridLayout.addWidget(self.ajuda, 2, 3, 1, 1)

        self.txt_senha = QLineEdit(self.frame_2)
        self.txt_senha.setObjectName(u"txt_senha")
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setMinimumSize(QSize(250, 40))
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"color: rgb(106, 0, 240);")
        self.txt_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.txt_senha, 4, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(106, 0, 240);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setPixmap(QPixmap(u"visibility-off.jpg"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(25, 25))
        self.label.setPixmap(QPixmap(u"person.jpg"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 3, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 140))
        self.frame.setStyleSheet(u"background-color: rgb(106, 0, 240);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(106, 0, 240);\n"
"border-radius:10px")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.ajuda, self.txt_usuario)
        QWidget.setTabOrder(self.txt_usuario, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.entrar)

        self.retranslateUi(login)

        self.entrar.setDefault(True)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("login", u"Usu\u00e1rio", None))
        self.entrar.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.ajuda.setText(QCoreApplication.translate("login", u"?", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("login", u"Senha", None))
        self.label_3.setText(QCoreApplication.translate("login", u"Bem-Vindo!", None))
        self.label_2.setText("")
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("login", u"F1 : Ajuda                    ", None))
    # retranslateUi

