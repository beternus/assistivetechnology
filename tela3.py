//All the credits to Pietro Dal Pizzol and Francisco Castro

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 120, 351, 51))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 220, 351, 51))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 350, 221, 91))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(400, 350, 211, 91))
        self.pushButton_2.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Acabou!!!", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Parab\u00e9ns", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Reiniciar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Sair", None))
    # retranslateUi
