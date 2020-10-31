"""
Сумма пар
Учитывая список целых чисел и единственное значение суммы, верните первые два значения (пожалуйста, проанализируйте слева) в порядке появления, которые в сумме образуют сумму.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Отрицательные числа и повторяющиеся числа могут появиться и появятся.

ПРИМЕЧАНИЕ. Также будут протестированы списки длиной более 10 000 000 элементов. Убедитесь, что время ожидания вашего кода не истекло.
"""


def sum_pairs(ints, s):
    a = None
    b = None

    for i in range(len(ints) - 1, -1, -1):

        for j in range(i - 1, -1, -1):
            if i > j and ints[i] + ints[j] == s:
                a = ints[j]
                b = ints[i]

    if (a and b) is not None:
        ints.clear()
        ints.append(a)
        ints.append(b)

    else:
        ints = None

    return ints


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
print(sum_pairs([1, -2, 3, 0, -6, 1], -6))
