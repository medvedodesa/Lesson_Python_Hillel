# Вариант 1
s = input('Введите строку:')
ch = "ch"
last_ch = s.rfind("ch")
i = 1

for ch in s:
    if ch in s:
        print(i, "раз когда мы встретили 'ch' в нашей строке с индексом")
        i += 1

