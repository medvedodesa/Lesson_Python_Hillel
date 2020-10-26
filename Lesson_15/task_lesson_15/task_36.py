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


groupStudent = open('groupStudent.txt', encoding='utf-8')
information_student = groupStudent.readlines()
listGrout = Group()

# БЕРУ ДАННЫЕ ИЗ ФАЙЛА groutStudent.txt И ДОБАВЛЯЮ ВСЕ ДАННЫЕ О СТУДЕНТЕ В self.studentList
for i in information_student:
    file = i.strip('\n').split()
    listGrout.add_student(file[0], file[1], file[2:])

groupStudent.close()

print('| {name:^15}|{age:^5}|{grades:^37}|'.format(name='NAME', age='AGE', grades='GRADE'))
print(' ' + '-' * 60 + ' ')

# ДЕЛАЮ КРАСИВЫЙ ВЫВОД --class Group-- ЕГО МЕТОДА --out_on_display--
for line in listGrout.out_on_display():
    print(('| ' + line[0]) + ' ' * (15 - len(str(line[0]))), end='')
    print(('| ' + line[1]) + ' ' * (4 - len(str(line[1]))), end='')
    print('| ', end='')
    for grade in range(len(line[2])):
        print(line[2][grade] + ' ' * (3 - len(line[2][grade])), end='')
    print('|')



