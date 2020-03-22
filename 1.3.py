#виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
#Результати множення елементів занесіть до нової матриці та виведіть її на екран;
import numpy as np
while True:
    while True:
        try:
            row1matr = int(input('Enter amount rows in first matrix: '))  # заповнення першої матриці
            col1matr = int(input('Enter amount columns in first matrix: '))  
            row2matr = int(input('Enter amount rows in second matrix: '))   #заповнення другої матриці
            col2matr = int(input('Enter amount columns in second matrix: '))  
            if col1matr == row2matr:  #перевірка на сумісність
                break
            else:
                print('Wrong values!')
        except ValueError:
            print('Wrong value!')

    matr1 = np.zeros((row1matr, col1matr), dtype=int)   #створюєм нулевий масив
    for i in range(row1matr):
        for j in range(col1matr):
            while True:
                try:
                    matr1[i, j] = int(input(f'Enter element ({i + 1},{j + 1}) 1st Matrix: '))   #задання масиву першої матриці
                    break
                except ValueError:
                    print('Wrong value!')

    matr2 = np.zeros((row2matr, col2matr), dtype=int)   #створюєм нулевий масив
    for i in range(row2matr):
        for j in range(col2matr):
            while True:
                try:
                    matr2[i, j] = int(input(f'Enter element ({i + 1},{j + 1}) 2nd Matrix: '))   #задання масиву другої матриці
                    break
                except ValueError:
                    print('Wrong value!')

    new_el = 0          #елемент нової матриці
    bufmatr = []        #буферна матриця
    endmatr = []        #кінечна матриця
    for z in range(0, row1matr):  #проходим циклом по ряду першої матриці
        for j in range(0, col2matr):  #проходим циклом по стовпчику другої
            for i in range(0, col1matr):
                new_el = new_el + matr1[z][i] * matr2[i][j]  #новий елемент ма триці
            bufmatr.append(new_el)  #добавляєм новий елемент в буферну матрицю
            new_el = 0  #обнуляем новий елемент для подальшого пошуку інших
        endmatr.append(bufmatr)  #добавляєм елементи з буферної матриці в кінечну
        bufmatr = []  #обнулення буфера
    print(endmatr)
    question = input("Хочете продовжити?Так-1,ні-інше")
    if question != "1":
        break
