# ЧИСЛА ФИБОНАЧЧИ С ПОМОШЬЮ РЕКУРСИИ
# Последовательность: 1, 2, 3, 5, 8, 13, 21, 34, 34, 55, 89, ...
def fibonacci(number):
    if number < 0:
        return -1
    if 0 <= number <= 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


# Проверяем, что оно работает
num = int(input('Введите любое число: '))
print(fibonacci(num))
