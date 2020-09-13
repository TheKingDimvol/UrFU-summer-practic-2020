import requests
import xlwt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from UI.Found import Ui_FoundWindow


regions = {'Екатеринбург': '3', 'Свердловская область': '1261', 'Москва': '1'}


class Found(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_FoundWindow()
        self.ui.setupUi(self)
        self.row = 0
        self.page = 0
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.pushButton.clicked.connect(lambda: self.book.save(self.vacancyName + '.xls'))

    def closeEvent(self, event):
        self.ui.table.clear()
        self.row = 1
        self.page = 0

    def fillItem(self, column, item):
        self.ui.table.setItem(self.row, column, QTableWidgetItem(item))
        font = xlwt.easyxf('font: height 240, name Arial Narrow; align: wrap on, vert centre, horiz center;')
        self.sheet.write(self.row + 1, column, item, font)

    def findVacancies(self, vacancyName, region):
        self.vacancyName = vacancyName
        self.startBook()
        while True:
            vacancies = []
            url = 'https://api.hh.ru/vacancies'
            par = {'text': self.vacancyName, 'area': regions[region], 'per_page': '10', 'page': self.page}
            r = requests.get(url, params=par)
            if not r or self.page == 1:
                break
            e = r.json()
            vacancies.append(e)
            self.page += 1
            for j in vacancies:
                y = j['items']
                for i in y:
                    vacancy = requests.get(i['url']).json()
                    key_skills = ''
                    for skill in vacancy['key_skills']:
                        key_skills += '[' + skill['name'] + ']; '
                    self.fillItem(0, vacancy['alternate_url'])
                    self.fillItem(1, vacancy['employer']['name'])
                    self.fillItem(2, vacancy['name'])
                    self.fillItem(3, key_skills)
                    if self.row % 10 == 0:
                        self.ui.addRows()
                    self.row += 1
                    self.ui.table.resizeRowsToContents()

    def startBook(self):
        self.book = xlwt.Workbook()
        font_big = xlwt.easyxf('font: height 220, name Bahnschrift; align: wrap on, vert centre, horiz center;')

        self.sheet = self.book.add_sheet('Вакансии')

        self.sheet.col(0).width = 10000
        self.sheet.col(1).width = 20000
        self.sheet.col(2).width = 20000
        self.sheet.col(3).width = 20000
        self.sheet.write(0, 0, 'Ссылка', font_big)
        self.sheet.write(0, 1, 'Компания', font_big)
        self.sheet.write(0, 2, 'Должность', font_big)
        self.sheet.write(0, 3, 'Ключевые навыки', font_big)
