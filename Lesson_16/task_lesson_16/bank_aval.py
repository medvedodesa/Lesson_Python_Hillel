# ПАРСИНГ

"""
Класс Student - содержит поля: name и grades. grades - это список оценок студента.
Класс Group - содержит поля name и students. students - список объектов класса Student.
Все поля - аттрибуты объекта.
Плюс, каждый класс должен содержать необходимые функции.
"""

from bs4 import BeautifulSoup
import requests

from Lesson_16.task_lesson_16.bank import Bank
from Lesson_16.task_lesson_16.currency import currency


class RaifffeisenBankAval(Bank):
    __URL = 'https://www.aval.ua/'

    def get_html(self):
        requests.get(self.__URL)
        return requests.text



if __name__ == '__main__':
    bank = RaifffeisenBankAval()
    print((bank.get_currency_rate()))

