# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search_Window(object):
    def setupUi(self, Search_Window):
        Search_Window.setObjectName("Search_Window")
        Search_Window.resize(436, 265)
        self.centralwidget = QtWidgets.QWidget(Search_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 201, 31))
        self.label.setObjectName("label")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(160, 180, 101, 31))
        self.button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.button.setObjectName("button")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 130, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('Екатеринбург')
        self.comboBox.addItem('Москва')
        self.comboBox.addItem('Свердловская область')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 201, 21))
        self.label_2.setObjectName("label_2")
        Search_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Search_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 21))
        self.menubar.setObjectName("menubar")
        Search_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Search_Window)
        self.statusbar.setObjectName("statusbar")
        Search_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Search_Window)
        QtCore.QMetaObject.connectSlotsByName(Search_Window)

    def retranslateUi(self, Search_Window):
        _translate = QtCore.QCoreApplication.translate
        Search_Window.setWindowTitle(_translate("Search_Window", "Поиск вакансий"))
        self.label.setText(_translate("Search_Window", "Введите название вакансии:"))
        self.button.setText(_translate("Search_Window", "Поиск"))
        self.button.setShortcut(_translate("Search_Window", "Return"))
        self.label_2.setText(_translate("Search_Window", "И выберите регион:"))

