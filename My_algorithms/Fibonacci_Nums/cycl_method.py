# ЧИСЛА ФИБОНАЧЧИ С ПОМОШЬЮ ЦИКЛА
def fibonacci_1(number):
    n1 = n2 = 1
    for i in range(number - 2):
        n = n1 + n2
        n1 = n2
        n2 = n

    return n


def fibonacci_2(number):
    n1 = n2 = 1
    while (number - 2) > 0:
        n = n1 + n2
        n1 = n2
        n2 = n
        number -= 1

    return n


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(fibonacci_1(num))
print(fibonacci_2(num))
