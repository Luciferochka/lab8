#виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотньому порядку
import numpy as np #імпорт бібліоетки
while True:
    while True:
        try:
            n = int(input('Enter amount of digits'))  #
            a = np.zeros((n), dtype=int)    #місце для масива
            b = np.zeros((n), dtype=int)    #місце для масива
            break
        except ValueError:   #перевірка на помилки(тільки цифри)
            print('Only nums')

    for i in range(n):
        a[i] = int(input('Enter your digits: '))    #ввод цифр
    print(a)

    for i in range(n):
        b[i] = a[n - 1 - i]#вивод значення в зворотному порядку
    print(f'New array:{b}')
    result = input('Хочете продовжити?Так-1,ні-інше')
    if result == '1':
        continue
    else:
        break
