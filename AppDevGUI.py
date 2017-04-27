# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gmull_000\PycharmProjects\AppDevGUIProject\Qt Designer\appDevGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 489)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.medButton = QtWidgets.QPushButton(self.centralwidget)
        self.medButton.setMinimumSize(QtCore.QSize(180, 0))
        self.medButton.setMaximumSize(QtCore.QSize(180, 16777215))
        self.medButton.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.medButton.setObjectName("medButton")
        self.verticalLayout.addWidget(self.medButton)
        self.avgButton = QtWidgets.QPushButton(self.centralwidget)
        self.avgButton.setMinimumSize(QtCore.QSize(180, 0))
        self.avgButton.setMaximumSize(QtCore.QSize(180, 16777215))
        self.avgButton.setObjectName("avgButton")
        self.verticalLayout.addWidget(self.avgButton)
        self.stdDevButton = QtWidgets.QPushButton(self.centralwidget)
        self.stdDevButton.setMinimumSize(QtCore.QSize(180, 0))
        self.stdDevButton.setMaximumSize(QtCore.QSize(180, 16777215))
        self.stdDevButton.setObjectName("stdDevButton")
        self.verticalLayout.addWidget(self.stdDevButton)
        self.maxMinButton = QtWidgets.QPushButton(self.centralwidget)
        self.maxMinButton.setMinimumSize(QtCore.QSize(180, 0))
        self.maxMinButton.setMaximumSize(QtCore.QSize(180, 16777215))
        self.maxMinButton.setObjectName("maxMinButton")
        self.verticalLayout.addWidget(self.maxMinButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.calcAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.calcAllButton.setMinimumSize(QtCore.QSize(180, 0))
        self.calcAllButton.setMaximumSize(QtCore.QSize(180, 16777215))
        self.calcAllButton.setObjectName("calcAllButton")
        self.verticalLayout.addWidget(self.calcAllButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.clearTextButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearTextButton.setMinimumSize(QtCore.QSize(180, 0))
        self.clearTextButton.setObjectName("clearTextButton")
        self.verticalLayout_2.addWidget(self.clearTextButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setMinimumSize(QtCore.QSize(180, 0))
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout_2.addWidget(self.quitButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.clearTextButton.clicked.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.medButton.setText(_translate("MainWindow", "Calculate Median"))
        self.avgButton.setText(_translate("MainWindow", "Calculate Average"))
        self.stdDevButton.setText(_translate("MainWindow", "Calculate Standard Deviation"))
        self.maxMinButton.setText(_translate("MainWindow", "Calculate Maximum and Minimum"))
        self.calcAllButton.setText(_translate("MainWindow", "Calculate Everything"))
        self.clearTextButton.setText(_translate("MainWindow", "Clear Text Box"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open Data"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
