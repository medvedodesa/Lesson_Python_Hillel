dictionary = {}

num_str = int(input('Введите число строк: '))

for text in range(num_str):
    string = input('Введите строку: ', )
    for word in string:
        dictionary[word] = dictionary.get(word, 0) + 1

# Сперва мы находим максимальное значение нашего словаря
max_value = max(dictionary.values())

# Теперь через (list comprehension) мы перебераем все ключи и их значение и ищем максимальное(ые).
lis_max_value = [i for i, mx in dictionary.items() if mx == max_value]

# Тут мы выводим минимальное значение списка. Елементы сравниваются по своим порядковым номерам. Метод ord().
print(min(lis_max_value))
