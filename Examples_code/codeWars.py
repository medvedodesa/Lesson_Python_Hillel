def flip(d, a):
    if d == 'R':
        for lis in a:
            for i in range(len(lis)):
                flag = True
                for j in range(len(lis) - i - 1):
                    if lis[j] > lis[j + 1]:
                        lis[j], lis[j + 1] = lis[j + 1], lis[j]
                        flag = False
                if flag:
                    break
        return a
    if d == 'L':
        for lis in a:
            for i in range(len(lis)):
                flag = True
                for j in range(len(lis) - i - 1):
                    if lis[j] < lis[j + 1]:
                        lis[j], lis[j + 1] = lis[j + 1], lis[j]
                        flag = False
                if flag:
                    break
        return a
    if d == 'U':
        for lis in a:
            for i in range(len(lis)):
                flag = True
                for j in range(len(lis) - i - 1):
                    if lis[j] > lis[j + 1]:
                        lis[j], lis[j + 1] = lis[j + 1], lis[j]
                        flag = False
                if flag:
                    break

        for lis in a:
            for i in range(len(lis)):
                flag = True
                for j in range(len(lis) - i - 1):
                    if lis[j] < lis[j + 1]:
                        lis[j], lis[j + 1] = lis[j + 1], lis[j]
                        flag = False
                if flag:
                    break

    for lis in a:
        for i in range(len(lis)):
            for j in range(len(lis)):
                if a[j][i] < a[j + 1][i]:
                    a[j][i], a[j + 1][i] = a[j + 1][i], a[j][i]

        return a

    if d == 'D':
        for lis in a:
            for i in range(len(lis)):
                for j in range(len(lis)):
                    if a[j][i] > a[j + 1][i]:
                        a[j][i], a[j + 1][i] = a[j + 1][i], a[j][i]

        return a


# print(flip('U', [[1, 3, 2],
#                  [4, 5, 1],
#                  [6, 5, 3],
#                  [7, 2, 9]]))

print(flip('U', [[9, 7, 3],
                 [6, 5, 2],
                 [5, 4, 1],
                 [3, 2, 1]]))