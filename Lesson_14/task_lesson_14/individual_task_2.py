# # Задача №2 (lesson_13)

"""
Написать функцию сортировки двухмерного списка МхМ (матрицы)
Значение М - задаётся пользователем, с клавиатуры. Может быть любым
целым, положительным числом, больше 5.

Функция должна:

 1. найти сумму элементов столбцов и отсортировать столбцы по
    возрастанию этих сумм
 2. отсортировать каждый нечётный столбец по возрастанию значений снизу
    вверх, а каждый чётный столбец по возрастанию значений сверху вниз.

 Так же, ваша программа должна иметь функцию вывода данного списка
 на экран. При выводе, внизу каждого столбца должна выводиться сумма
 элементов этого столбца.

Что можно использовать:

 1. для создания списка использовать ТОЛЬКО 'list comprehension' и
    генератор случайных чисел. Диапазон случайных чисел для заполнения
    списка от 1 до 50. Список должен создаваться однострочным
    выражением.
 2. Можно использовать ТОЛЬКО ДВА списка. Первый это двухмерный список
    размером МхМ, второй, вспомогательный, одномерный список размером
    М. Использование других списков (или коллекций) НЕДОПУСТИМО.
 3. Можно использовать ТОЛЬКО ОДНУ переменную М для хранения размера
    списка, плюс переменные циклов for.
 4. Для сортировки можно использовать алгоритм пузырьковой сортировки.
    Использование встроенных функций сортировки - НЕДОПУСТИМО (да и не
    получится их использовать)!
 5. Решение должно включать ТОЛЬКО ДВЕ функции: функцию сортировки (по
    правилам описанным выше) и функцию вывода на экран.
    Задача считается решённой верно при условии соблюдения всех требований.

Аккуратный вывод на экран - приветствуется.
"""

from random import randint


def sort_list(lis):
    suma_lis = []
    len_lis = len(lis)

    # !!!
    # НАЧАЛО ПЕРВОГО (НЕ ОБРАБОТАНОГО) ВЫВОДА
    for i in range(len_lis):
        for j in range(len_lis):
            print(' ' * (3 - len(str(lis[i][j]))) + str(lis[i][j]) + ' ', end='')
        print()
    print('--- ' * len_lis)

    for j in range(len(lis)):
        suma_lis.append(sum(lis[j]))
        print(' ' * (3 - len(str(suma_lis[j]))) + str(suma_lis[j]) + ' ', end='')
        suma = 0
    # КОНЕЦ ПЕРВОГО (НЕ ОБРАБОТАНОГО) ВЫВОДА
    # !!!

    print()

    for i in range(len(suma_lis)):
        flag = True
        for j in range(len(suma_lis) - i - 1):
            if suma_lis[j] > suma_lis[j + 1]:
                suma_lis[j], suma_lis[j + 1] = suma_lis[j + 1], suma_lis[j]
                flag = False
                for s in range(len(lis)):
                    lis[s][j], lis[s][j + 1] = lis[s][j + 1], lis[s][j]
        if flag:
            break

    for j in range(len(lis)):
        if j % 2 == 0:
            for i in range(len(lis) - 1, -1, -1):
                flag = True
                for s in range(len(lis) - 1):
                    if lis[s][j] < lis[s + 1][j]:
                        lis[s][j], lis[s + 1][j] = lis[s + 1][j], lis[s][j]
                        flag = False
                if flag:
                    break

        else:
            for i in range(len(lis)):
                flag = True
                for s in range(len(lis) - i - 1):
                    if lis[s][j] > lis[s + 1][j]:
                        lis[s][j], lis[s + 1][j] = lis[s + 1][j], lis[s][j]
                        flag = False
                if flag:
                    break

    print()

    for i in range(len(lis)):
        for j in range(len(lis)):
            print(' ' * (3 - len(str(lis[i][j]))) + str(lis[i][j]) + ' ', end='')
        print()
    print('--- ' * len(lis))

    for i in range(len(suma_lis)):
        print(' ' * (3 - len(str(suma_lis[i]))) + str(suma_lis[i]) + ' ', end='')

    print()
    # !!!КОНЕЦ ФУНКЦИИ!!!


while True:
    lening = int(input('Введите кол - во строк и столбцов (больше 5): '))
    if lening <= 5:
        print('!!!КОЛ - ВО СТРОК И СТОЛБЦОВ В ВАШЕЙ МАТРИЦЕ НЕ БОЛЬШЕ 5!!!')
        continue
    else:
        break

matrix = [[randint(1, 51) for j in range(lening)] for i in range(lening)]

sort_list(matrix)

