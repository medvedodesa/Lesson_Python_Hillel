from random import randint

lst = [randint(1, 50) for _ in range(30)]
print(lst)
lst.sort()
print(lst)



def fast_sort(lis, low, high):
    if low >= high:
        return

    i, j = low, high
    mid = lis[(low + high) // 2]

    while i <= j:
        while lis[i] < mid:
            i += 1
        while lis[j] > mid:
            j -= 1

        if i <= j:
            lis[i], lis[j] = lis[j], lis[i]
            i, j = i + 1, j - 1

    fast_sort(lis, low, j)
    fast_sort(lis, i, high)


fast_sort(lst, 0, len(lst) - 1)
