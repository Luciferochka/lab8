import numpy as np
while True:
    print("прямий пошук підрядка \n")

        text = input("enter str")
        pattern = input("enter pattern")
        i = -1
        j = 0
        count = 0
        print('text:', text)
        print('pattern:', pattern)
        while (j < len(pattern)) and i < (len(text) - len(pattern)):
            count += 2
            j = 0
            i += 1
            while j < len(pattern) and pattern[j] == text[i + j]:
                count += 2
                j += 1
        if j == len(pattern):
            print('position', i)
        else:
            print('not found')
        print('quantity ', count)
        else:
        text = "my name is Johan, your name"
        pattern = "your"
        i = -1
        j = 0
        count = 0
        print('text:', text)
        print('pattern:', pattern)
        while (j < len(pattern)) and i < (len(text) - len(pattern)):
            count += 2
            j = 0
            i += 1
            while j < len(pattern) and pattern[j] == text[i + j]:
                count += 2
                j += 1
        if j == len(pattern):
            print('position', i)
        else:
            print('not found')
        print('quantity ', count)
        print()
        text = "my name is Johan, your name"
        pattern = "Im Kendrick"
        i = -1
        j = 0
        count = 0
        print('text:', text)
        print('pattern:', pattern)
        while (j < len(pattern)) and i < (len(text) - len(pattern)):
            count += 2
            j = 0
            i += 1
            while j < len(pattern) and pattern[j] == text[i + j]:
                count += 2
                j += 1
        if j == len(pattern):
            print('position', i)
        else:
            print('not found')
        print('quantity', count)
    if input('enter: ') == '':
        continue
    break
