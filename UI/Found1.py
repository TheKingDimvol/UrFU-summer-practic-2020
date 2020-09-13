# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'found.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FoundWindow(object):
    def setupUi(self, FoundWindow):
        FoundWindow.setObjectName("FoundWindow")
        FoundWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FoundWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setEnabled(True)
        self.table.setGeometry(QtCore.QRect(10, 40, 781, 511))
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setObjectName("table")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 211, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 91, 31))
        self.label.setObjectName("label")
        self.region = QtWidgets.QLabel(self.centralwidget)
        self.region.setGeometry(QtCore.QRect(330, 5, 71, 21))
        self.region.setObjectName("region")
        FoundWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FoundWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FoundWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FoundWindow)
        self.statusbar.setObjectName("statusbar")
        FoundWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FoundWindow)
        QtCore.QMetaObject.connectSlotsByName(FoundWindow)

    def retranslateUi(self, FoundWindow):
        _translate = QtCore.QCoreApplication.translate
        FoundWindow.setWindowTitle(_translate("FoundWindow", "Список вакансий"))
        self.pushButton.setText(_translate("FoundWindow", "Сохранить в Excel"))
        self.label.setText(_translate("FoundWindow", "Область поиска:"))
        self.region.setText(_translate("FoundWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FoundWindow = QtWidgets.QMainWindow()
    ui = Ui_FoundWindow()
    ui.setupUi(FoundWindow)
    FoundWindow.show()
    sys.exit(app.exec_())
