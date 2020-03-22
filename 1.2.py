#виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем)
import numpy as np
while True:
    while True:
        try:
            n, m = 3,3      #розмірність матриці
            a = np.zeros((n, m), dtype=int)     #місце для масива
            b = np.zeros((m, n), dtype=int)     #місце для масива
            break
        except ValueError:          #перевірка на помилки(вводити тільки цифри)
            print('Only nums')

    for i in range(n):
        for j in range(m):
            a[i,j]=int(input(f'A[{i},{j}]='))       #значення матриці
    print(f'Your matrix: \n {a}')

    for i in range(n):
        for j in range(m):          #транспонування матриці
            new = a[j, i]
            b[i, j] = new
    print(f'Your new matrix: \n {b}')
    result = input('Хочете продовжити? Так-1, ні-інше')
    if result == '1':   #перезапуск програми
        continue
    else:
        break
