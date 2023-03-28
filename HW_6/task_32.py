'''Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)'''


import random

# Вводим число элементов массива

a = int(input("A:"))
lim_min = int(input("Минимум:"))
lim_max = int(input("Максимум:"))


def array_filling(count_num):
    '''Функция заполнения массива рандомными числами'''
    array = []
    for _ in range(count_num):
        array.append(random.randint(-20, 20))
    return array


number_array = array_filling(a)
print(number_array)

limit_index = []

for i, num in enumerate(number_array):
    if num >= lim_min and num <= lim_max:
        limit_index.append(i)
print(limit_index)
