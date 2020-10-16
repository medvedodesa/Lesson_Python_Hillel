# Вариант 1 (Пузырьковая сортировка)
def bubble_sort_1(lis):
    count = 0
    length = len(lis)
    for i in range(len(lis)):
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]

        count += 1

    return lis, count, length


# Вариант 2 (Пузырьковая сортировка)
def bubble_sort_2(lis):
    count = 0
    length = len(lis)

    for i in range(len(lis)):
        flag = True
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                flag = False

        if flag:
            break

        count += 1

    return lis, count, length


# ВЫВОД РАЗНЫХ РЕЗУЛЬТАТОВ С ПОМОШЬЮ ДВУХ ФУНКЦИЙ
lst_1 = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
lst_2 = [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
lst_3 = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
lst_4 = [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]

print(bubble_sort_1(lst_1))
print(bubble_sort_1(lst_2))
print(bubble_sort_2(lst_3))
print(bubble_sort_2(lst_4))


