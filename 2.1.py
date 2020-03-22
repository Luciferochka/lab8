import numpy as np

while True:
    print("linear: \n")
    get = input("1-to input your, else: random\n")
    if get == 'yes':
        while True:
            try:
                g = int(input("length: "))
                x = int(input())

                break
            except ValueError:
                print('only digit')
        a = np.zeros(g, dtype=int)
        print("enter array:")
        for i in range(g):
            while True:
                try:
                    a[i] = int(input("enter int digit: "))
                    break
                except ValueError:
                    print("only digits")
        print(a)

        i = 0
        g = len(a)
        count = 0
        while i < g and a[i] != x:
            count += 2
            i += 1
        if i == g:
            print(x, 'not found')
            print('quantity ', count)
        else:
            print(x, 'founded ', i)
            print('quantity ', count)
    else:

        a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
        a = np.array(a)
        x = 15

        print(a)
        i = 0
        g = len(a)
        count = 0
        while i < g and a[i] != x:
            count += 2
            i += 1
        if i == g:
            print(x, 'not found')
            print('quantity ', count)
        else:
            print(x, 'founded ', i)
            print('quantity ', count)


        a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
        a = np.array(a)
        x = 6

        print(a)
        i = 0
        g = len(a)
        count = 0
        while i < g and a[i] != x:
            count += 2
            i += 1
        if i == g:
            print(x, 'not found')
            print('quantity ', count)
        else:
            print(x, 'founded ', i)
            print('quantity ', count)

    if input('enter') == '':
        continue
    break
