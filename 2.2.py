import numpy as np

while True:
    print("Бінарний пошук: \n")
            try:
                g = int(input())
                x = int(input())
                break
            except ValueError:
                print('Только числа !')
    a = np.zeros(g, dtype=int)
    print("enter array ")
    for i in range(g):
        while True:
            try:
                a[i] = int(input("enter digit "))
                break
            except ValueError:
                print('only digits')
    print(a)
    a.sort()
    g = len(a)
    print(a)
    i = 0
    L = 0
    R = g - 1
    flag = True
    counter_def = 0
    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if g[K] == g:
            counter_def += 2
            print(g, 'position ', K)
            print('coincidences ', counter_def)
            flag = False
        elif a[K] < x:
            counter_def += 3
            L = K + 1
        elif a[K] > x:
            counter_def += 4
            R = K - 1
    if flag:
        print(x, 'not found')
        print('quantity:', counter_def)
    else:
    a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
    a = np.array(a)
    x = 15
    a.sort()
    g = len(a)
    print(a)
    i = 0
    L = 0
    R = g - 1
    flag = True
    counter_def = 0
    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if g[K] == g:
            counter_def += 2
            print(g, 'position ', K)
            print('coincidences ', counter_def)
            flag = False
        elif a[K] < x:
            counter_def += 3
            L = K + 1
        elif a[K] > x:
            counter_def += 4
            R = K - 1
    if flag:
        print(x, 'not found')
        print('Количество:', counter_def)

    # шуканий елемент знаходиться в масиві
    a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
    a = np.array(a)
    x = 6
    a.sort()
    g = len(a)
    print(a)
    i = 0
    L = 0
    R = g - 1
    flag = True
    counter_def = 0
    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if g[K] == g:
            counter_def += 2
            print(g, 'position ', K)
            print('coincidences ', counter_def)
            flag = False
        elif a[K] < x:
            counter_def += 3
            L = K + 1
        elif a[K] > x:
            counter_def += 4
 
