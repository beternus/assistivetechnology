//All the credits to Pietro Dal Pizzol and Francisco Castro by the software development
//Contact and information about the code: bernardoternus@gmail.com
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(800, 600)
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 180, 221, 31))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(330, 220, 141, 31))
        self.lineEdit.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 270, 171, 21))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(330, 300, 141, 31))
        self.lineEdit_2.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 460, 191, 71))
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(420, 460, 191, 71))
        self.pushButton_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 70, 301, 71))
        font1 = QFont()
        font1.setPointSize(35)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(330, 380, 141, 31))
        self.lineEdit_3.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 350, 171, 21))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"N\u00famero de Repeti\u00e7\u00f5es:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u00c2ngulo Extens\u00e3o:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Come\u00e7ar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Sair", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"SMART CPM", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u00c2ngulo Flex\u00e3o:", None))
    # retranslateUi

