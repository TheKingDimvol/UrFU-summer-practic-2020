import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from Windows.FoundWindow import Found
from UI.Search import Ui_Search_Window


class Search(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_Search_Window()
        self.ui.setupUi(self)
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.button.clicked.connect(self.open_found_window)

    def open_found_window(self):
        self.found_window = Found()
        self.found_window.ui.region.setText(self.ui.comboBox.currentText())
        self.found_window.setWindowModality(Qt.ApplicationModal)
        self.found_window.show()
        self.found_window.findVacancies(self.ui.lineEdit.text(), self.ui.comboBox.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Search()
    window.connect_buttons()
    window.show()
    sys.exit(app.exec_())