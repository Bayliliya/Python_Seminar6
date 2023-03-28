'''Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: a
n
 = a1
 + (n-1) * d.
Каждое число вводится с новой строки.'''


a_1 = int(input("Input first element: "))
n_count = int(input("Input count: "))
d_dif = int(input("Input difference: "))

arith_prog = []

for i in range(1, n_count + 1):
    arith_prog.append(a_1 + ((i - 1) * d_dif))
print(arith_prog)
