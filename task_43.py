'''Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках'''

import random

# Вводим число элементов первого и второго массива

a = int(input("A:"))

limit = int(input("Введите пределы: "))


def array_filling(count_num, num):
    '''Функция заполнения массива рандомными числами'''
    array = []
    for _ in range(count_num):
        array.append(random.randint(0, num))
    return array


number_array = array_filling(a, limit)
print(number_array)
set_help = set()

for i in range(a):
    for j in range(i + 1, a):
        if number_array[i] == number_array[j]:
            set_help.add(number_array[i])
print(len(set_help))


count = 0

for i in range(a):
    for j in range(i + 1, a):
        if number_array[i] == number_array[j]:
            count += 1
print(f'count = {count}')
