# ПИРАМИДАЛЬНАЯ СОРТИРОВКА (КУЧА)
def heapify(lis, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and lis[left_child] > lis[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and lis[right_child] > lis[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        lis[root_index], lis[largest] = lis[largest], lis[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(lis, heap_size, largest)


def heap_sort(lis):
    n = len(lis)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении, 
    # уменьшая счётчик i на 1 
    for i in range(n, -1, -1):
        heapify(lis, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        lis[i], lis[0] = lis[0], lis[i]
        heapify(lis, i, 0)

    return lis


# Проверяем, что оно работает
lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
print(heap_sort(lst))
