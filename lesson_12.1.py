# Задача №31 (Работа с числом)

"""
Написать функцию, которая принимает в качестве параметра целое, многозначное число.
Функция должна вернуть сумму произведений каждой цифры на её порядковый номер.
Например: есть число 874658734

 8 имеет порядковый номер 1,
 7 - 2
 4 - 3
 6 - 4
 5 - 5 и т. д.

необходимо посчитать: 8 * 1 + 7 * 2 + 4 * 3 + 6 * 4 + 5 * 5 .....
Задачу надо решить с использование list comprehension и функции sum() в ОДНУ строку.
"""

num = int(input('Введите любое число: '))
print('Ваше цисло:', num)

lis = sum(list(i * int(str(num)[i - 1]) for i in range(1, len(str(num)) + 1)))

print('Сумма всех чисел и произведения на их порядковый номер равна:', lis)
