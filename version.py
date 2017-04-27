# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gmull_000\PycharmProjects\AppDevGUIProject\Qt Designer\version.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_versionDialog(object):
    def setupUi(self, versionDialog):
        versionDialog.setObjectName("versionDialog")
        versionDialog.resize(320, 135)
        versionDialog.setMinimumSize(QtCore.QSize(320, 135))
        versionDialog.setMaximumSize(QtCore.QSize(320, 135))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(versionDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(versionDialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QDialogButtonBox(versionDialog)
        self.okButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okButton.setCenterButtons(True)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(versionDialog)
        self.okButton.accepted.connect(versionDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(versionDialog)

    def retranslateUi(self, versionDialog):
        _translate = QtCore.QCoreApplication.translate
        versionDialog.setWindowTitle(_translate("versionDialog", "Dialog"))
        self.label.setText(_translate("versionDialog", " Version 0.0.01"))

