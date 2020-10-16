# Выборочная сортировка
def selection_sort(lis):
    for i in range(len(lis) - 1):
        m = i
        j = i + 1
        while j < len(lis):
            if lis[j] < lis[m]:
                m = j

            j += 1

        lis[i], lis[m] = lis[m], lis[i]

    return lis


lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]

print(selection_sort(lst))
