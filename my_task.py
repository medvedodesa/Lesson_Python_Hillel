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

print(55 % 36)