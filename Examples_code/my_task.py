# Последовательность: 1, 2, 3, 5, 8, 13, 21, 34, 34, 55, 89, ...
num = 600851475143
lst = []
suma = 1

for i in range(2, num + 1):
    if num % i == 0:
        lst.append(i)
        suma *= i
        if suma == num:
            break
        elif suma < num:
            continue
        else:
            print('Такого нет')
            break

print(lst)
print(max(lst))
print(suma)
