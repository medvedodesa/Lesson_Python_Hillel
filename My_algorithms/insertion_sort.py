# Сортировка вставками
def insertion_sort(lis):
    for i in range(1, len(lis)):
        key = lis[i]
        j = i - 1
        while j >= 0 and key < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = key

    return lis


lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]

print(insertion_sort(lst))
