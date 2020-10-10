# !!!СОРТИРОВКА ПУЗЫРЬКОМ!!!

# from random import randint
#
# lst = [randint(0, 50) for _ in range(10)]
#
# print(lst)
#
# for i in range(len(lst)):
#     for j in range(len(lst) - i - 1):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
#             print(lst)
#
# swaps = True
#
# while swaps:
#     swaps = False
#     for j in range(len(lst) - 1):
#         if lst[j] > lst[j + 1]:
#             swaps = True
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
#
# print(lst)


# !!! ФАКТОРИАЛ ЧИСЛА!!!

# num = int(input('Please enter else number: '))
# k = 1
#
# for i in range(1, num + 1):
#     k *= i
#
# print(k)

# num = int(input('Please enter else number: '))
#
# def factorial(n):
#     if n == 0:
#         return 1
#     f = 1
#     i = 1
#
#     while i <= n:
#         f *= i
#         i += 1
#
#     return f
#
# print(factorial(num))

from random import randint

# def binary_search_2(array, key_value, left=0, right=None):
#     if right is None:
#         right = len(array)
#
#     j = 0
#     middle = (left + right) // 2
#     while array[middle] != key_value and left <= right:
#         if array[middle] < key_value:
#             left = middle + 1
#             j += 1
#         else:
#             right = middle - 1
#             j += 1
#
#         middle = (left + right) // 2
#     return (True, j, middle, array[middle]) if not (left > right) else (False, j)


# def binary_alg(args, key_value, low=0, high=None):
#     if high is None:
#         high = len(args)
#
#     mid = (low + high) // 2
#     j = 0
#     while args[mid] != key_value and low <= high:
#         if args[mid] < key_value:
#             low = mid + 1
#             j += 1
#         else:
#             high = mid - 1
#             j += 1
#
#         mid = (low + high) // 2
#
#     return (True, j, mid, args[mid]) if not (low > high) else (False, j)
#
#
# lst = [randint(1, 2000) for _ in range(1000)]
# print(lst)
# print()
# lst.sort()
# print(lst)
# print(len(lst))
#
# key = int(input('Введите любое число: '))
# print()
# print(binary_alg(lst, key))


# from random import randrange
#
# lis = [randrange(0, 1000) for _ in range(1000)]
# print(lis)
#
# counter = 0
# for i in range(len(lis)):
#     flag = True
#     for j in range(len(lis) - i - 1):
#         if lis[j] > lis[j + 1]:
#             lis[j], lis[j + 1] = lis[j + 1], lis[j]
#             flag = False
#     if flag:
#         break
#     counter += 1
#
# print(lis)
# print(counter)
#
# num = int(input('Бинарный поиск: '))
#
#
# def binary_sorce(lst, key_value):
#     low = 0
#     higth = len(lst)
#     j = 0
#     mid = (low + higth) // 2
#     while lst[mid] != key_value and low <= higth:
#         if lst[mid] < key_value:
#             low = mid + 1
#             j += 1
#         else:
#             higth = mid - 1
#             j += 1
#
#         mid = (low + higth) // 2
#
#     return (j, True) if not (low > higth) else (j, False)
#
#
# print(binary_sorce(lis, num))

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = 11

# Пустой треугольник
for i in range(n):
    for j in range(1, 2 * n):
        if j == n - i or j == n + i or i == n - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

# Закрашеный треугольник
for i in range(n):
    for j in range(1, 2 * n):
        if n - i <= j <= n + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

# Пустой ромб
for i in range(n):
    mid = n // 2 + n % 2
    if i < mid:
        for j in range(n):
            if j == mid - i - 1 or j == mid + i - 1:
                print('* ', end='')
            else:
                print('  ', end='')
    else:
        for j in range(n - 1):
            if j == i + 1 - mid or j == n - 2 - (i - mid):
                print('* ', end='')
            else:
                print('  ', end='')
    print()


