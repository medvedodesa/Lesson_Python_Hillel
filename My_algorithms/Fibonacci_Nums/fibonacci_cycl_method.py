# ЧИСЛА ФИБОНАЧЧИ С ПОМОШЬЮ ЦИКЛА
# Последовательность: 1, 2, 3, 5, 8, 13, 21, 34, 34, 55, 89, ...
def fibonacci(number):
    n = None
    n1 = 0
    n2 = 1

    while number > 0:
        n = n1 + n2
        n1 = n2
        n2 = n
        number -= 1

    return n


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(fibonacci(num))
