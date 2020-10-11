# Задача №33 (Развернуть словарь)

"""
Дан словарь ключами которого являются английские слова, а значениями - списки латинских слов.
Необходимо развернуть словарь. Другими словами, необходимо, на основании заданного словаря,
создать новый словарь, у которого в качестве ключей будут взяты латинские слова,
из первого словаря, а значениями будут, соответствующие им, английские слова.

d = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}
"""

d = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}

print(d)
print()
dict_revers = {}

# РАЗВОРАЧИВАЕМ СЛОВАРЬ
for key, value in d.items():
    for i in range(0, len(value)):
        print(value[i], key)

        # ТАК КАК ЗНАЧЕНИЕ 'malum' ВЫСТУПАЕТ В РОЛИ КЛЮЧА И ПОВТОРЯЕТСЯ (Я ВЫВЕДУ ПЕРВЫЙ ЕГО КЛЮЧ)!
        if value[i] in dict_revers:
            continue
        else:
            dict_revers[value[i]] = key
    print()

# НОВЫЙ СЛОВАРЬ ГДЕ ВМЕСТО (КЛЮЧ : ЗНАЧЕНИЕ) УЖЕ (ЗНАЧЕНИЕ : КЛЮЧ).
print(dict_revers)
