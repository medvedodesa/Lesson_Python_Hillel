# ЧИСЛА ФИБОНАЧЧИ С ПОМОШЬЮ РЕКУРСИИ
def fibonacci(number):
    if number < 0:
        return -1
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(fibonacci(num))
