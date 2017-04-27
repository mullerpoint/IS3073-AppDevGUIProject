# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gmull_000\PycharmProjects\AppDevGUIProject\Qt Designer\help.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_helpDialog(object):
    def setupUi(self, helpDialog):
        helpDialog.setObjectName("helpDialog")
        helpDialog.resize(320, 135)
        helpDialog.setMinimumSize(QtCore.QSize(320, 135))
        helpDialog.setMaximumSize(QtCore.QSize(320, 135))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(helpDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(helpDialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QDialogButtonBox(helpDialog)
        self.okButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okButton.setCenterButtons(True)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(helpDialog)
        self.okButton.accepted.connect(helpDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(helpDialog)

    def retranslateUi(self, helpDialog):
        _translate = QtCore.QCoreApplication.translate
        helpDialog.setWindowTitle(_translate("helpDialog", "Dialog"))
        self.label.setText(_translate("helpDialog", " There is no help"))

