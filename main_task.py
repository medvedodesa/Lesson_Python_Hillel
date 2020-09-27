empty_triangle = 'пустой треугольник'
filled_triangle = 'закрашеный треугольник'
empty_rhombus = 'пустой ромб'
filled_rhombus = 'закрашей ромб'
rhombus_50_50 = 'верхняя часть ромба закрашеная а нижняя пустая'
rhombus_50_25_25 = 'верхняя часть ромба закрашеная а нижняя пустая и вертикальной линией'
end = None

while True:
    if end == 0:
        print('ВЫ ЗАВЕРШИЛИ РАБОТУ ПРОГРАММЫ!')
        break
    elif end == 1:
        end = None
        continue
    else:
        print()

        figure = input("""Выберети желаемую фигуру:
        
  1. Пустой треугольник 
  2. Закрашеный треугольник
  3. Пустой ромб
  4. Закрашей ромб 
  5. Верхняя часть ромба закрашеная а нижняя пустая
  6. Верхняя часть ромба закрашеная а нижняя пустая и вертикальной линией
  0. Завершить работу программы
    
Введите номер указаной фигуры: """)

        print()

        if figure.isdigit():
            figure = int(figure)
            if figure == 1:
                print('Вы выбрали', empty_triangle)
            elif figure == 2:
                print('Вы выбрали', filled_triangle)
            elif figure == 3:
                print('Вы выбрали', empty_rhombus)
            elif figure == 4:
                print('Вы выбрали', filled_rhombus)
            elif figure == 5:
                print('Вы выбрали', rhombus_50_50)
            elif figure == 6:
                print('Вы выбрали', rhombus_50_25_25)
            elif figure == 0:
                end = 0
                break

            print()

            while True:
                if end == 1 or end == 0:
                    break
                n = input("""      Введите любое НЕ ЧЁТНОЕ НАТУРАЛЬНОЕ число!
        *** Это будет высота вашей фигуры ***
    
                !!!ПРЕДУПРЕЖДЕНИЕ!!!  
                            
Если вы введёте ЧЁТНОЕ число то оно увеличится на одну 
единицу. НАПРИМЕР: вы ввели число 2 оно станет 3!
Или введите "0" что бы выбрать другую фугуру.
    
Введите ваше число: """)
                if n.isdigit():
                    n = int(n)
                    if n == 0:
                        print()
                        print('Вы вернулись в меню выбора фигуры.')
                        print()
                        break
                    elif n > 0:
                        if not n % 2:
                            n += 1
                        print()
                        print('Высота вашей фигуры:', n)
                        print()
                        c = n // 2 + 1
                        if figure == 1:
                            for i in range(n):
                                for j in range(2 * n - 1):
                                    if j == n - 1 - i or j == n - 1 + i or i == n - 1:
                                        print('*', end='')
                                    else:
                                        print(' ', end='')
                                print()
                            print()
                            end = input("""*** Выберете следующее действие ***
    
 1. Ещё разок выбрать фигуру
 0. Завершить роботу программы
    
Ваше действие: """)
                            if end.isdigit():
                                end = int(end)
                                if end == 1 or end == 0:
                                    break
                            else:
                                continue
                        elif figure == 2:
                            for i in range(n):
                                print(' ' * n, end='')
                                n -= 1
                                for j in range(i):
                                    print('*', end='')
                                for j in range(i + 1):
                                    print('*', end='')
                                print()
                            print()
                            end = input("""Выберете следующее действие:
    
 1. Ещёразок выбрать фигуру
 0. Завершить роботу программы
    
Ваше действие: """)
                            if end.isdigit():
                                end = int(end)
                                if end == 1 or end == 0:
                                    break
                            else:
                                continue
                        elif figure == 3:
                            for i in range(n):
                                if i < c:
                                    for j in range(2 * n - 1):
                                        if j == n - 1 - i or j == n - 1 + i or i == n - 1:
                                            print('*', end='')
                                        else:
                                            print(' ', end='')
                                else:
                                    n -= 1
                                    for j in range(2 * n):
                                        if j == i or j == n + c - 2:
                                            print('*', end='')
                                        else:
                                            print(' ', end='')
                                print()
                            print()
                            end = input("""Выберете следующее действие:
    
 1. Ещё разок выбрать фигуру
 0. Завершить роботу программы
    
Ваше действие: """)
                            if end.isdigit():
                                end = int(end)
                                if end == 1 or end == 0:
                                    break
                            else:
                                continue
                        elif figure == 4:
                            for i in range(n):
                                if i < c:
                                    print(' ' * n, end='')
                                    n -= 1
                                    for j in range(i):
                                        print('*', end='')
                                    for j in range(i + 1):
                                        print('*', end='')
                                else:
                                    print(' ' * (i + 1), end='')
                                    n -= 1
                                    for j in range(n + 1):
                                        print('*', end='')
                                    for j in range(n):
                                        print('*', end='')
                                print()
                            print()
                            end = input("""Выберете следующее действие:
    
 1.     Ещё разок выбрать фигуру
 0.     Завершить роботу программы
    
Ваше действие: """)
                            if end.isdigit():
                                end = int(end)
                                if end == 1 or end == 0:
                                    break
                            else:
                                continue
                        elif figure == 5:
                            for i in range(n):
                                if i < c:
                                    print(' ' * n, end='')
                                    n -= 1
                                    for j in range(i):
                                        print('*', end='')
                                    for j in range(i + 1):
                                        print('*', end='')
                                else:
                                    n -= 1
                                    for j in range(2 * n + (j + 3)):
                                        if j == i + 1 or j == n + (2 * c - 1):
                                            print('*', end='')
                                        else:
                                            print(' ', end='')
                                print()
                            print()
                            end = input("""Выберете следующее действие:
    
 1. Ещё разок выбрать фигуру
 0. Завершить роботу программы
    
Ваше дествие: """)
                            if end.isdigit():
                                end = int(end)
                                if end == 1 or end == 0:
                                    break
                            else:
                                continue
                        elif figure == 6:
                            for i in range(n):
                                if i < c:
                                    print(' ' * n, end='')
                                    n -= 1
                                    for j in range(i):
                                        print('*', end='')
                                    for j in range(i + 1):
                                        print('*', end='')
                                else:
                                    n -= 1
                                    for j in range(2 * n + (j + 3)):
                                        if j == i + 1 or j == n + (2 * c - 1) or j == n + i + 1:
                                            print('*', end='')
                                        else:
                                            print(' ', end='')
                                print()
                            print(end)
                            while end != 1 or end != 0:
                                end = input("""Выберете следующее действие:
    
 1. Ещё разок выбрать фигуру
 0. Завершить роботу программы
    
Ваше действие: """)
                                if end.isdigit():
                                    end = int(end)
                                    if end != 1 or end != 0:
                                        break
                                elif end != 1 or end != 0:
                                    print()
                                    print('!!!ТАКОГО ДЕЙСТВИЯ НЕ СУЩЕСТВУЕТ!!!')
                                    print()
                                    continue
                else:
                    print()
                    print('!!!ВЫ ВВЕЛИ НЕ ЧИСЛО!!!')
                    print()
                    continue

        else:
            print()
            print('!!!ВЫ ВВЕЛИ НЕ СУЩЕСТВУЮЩУЮ ФИГУРУ!!!\n    --- Попробуйте ещё раз ---')
            print()
            continue
