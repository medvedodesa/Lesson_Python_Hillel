# Задача №36 (Студенты и группы)

"""
Создать класс, описывающий группу студентов - `Group`.
Данный класс хранит студентов в виде списка объектов
`Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс
`Student` должен иметь атрибуты `name`, `age`, `grades`), а так
же необходимый набор методов экземпляра для работы с этими экземплярами.

Наследование здесь не понадобится.
"""


class Group:
    def __init__(self):
        self.studentList = []

    def add_student(self, name, age, grades):
        self.studentList.append(Group.Student(name, age, grades).studentInformation())

    def out_on_display(self):
        return self.studentList

    class Student:
        def __init__(self, name, age, grades):
            self.name = name
            self.age = age
            self.grades = grades

        def studentInformation(self):
            return self.name, self.age, self.grades


listGrout = Group()
print(listGrout.out_on_display())



