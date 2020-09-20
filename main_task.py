# Вариант 1
s = input('Введите строку:')
last_ch = s.find("ch")

i = 1

if last_ch > -1:
    while last_ch > -1:
        print(i, "раз когда мы встретили 'ch' в нашей строке с индексом", last_ch)
        last_ch = s.find("ch", last_ch + 1)
        i += 1
    else:
        print("Больше совпадений с символом 'ch' не найдено!")
else:
    print("Cовпадений с символом 'ch' не найдено!")