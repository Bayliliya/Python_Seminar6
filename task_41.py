"""Дан массив, состоящий из целых чисел. Напишите программу,
которая в данном массиве определит количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного.
Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел."""

import random

# Вводим число элементов первого и второго массива

a = int(input("A:"))

limit = int(input("Ввведите пределы: "))


def array_filling(a, n):
    '''Функция заполнения массива рандомными числами'''
    array = []
    for _ in range(a):
        array.append(random.randint(0, n))
    return array


number_array = array_filling(a, limit)
print(number_array)
count = 0

for i in range(-1, a - 1):
    if (number_array[i] > number_array[i - 1]
       and number_array[i] > number_array[i + 1]):
        count += 1
print(count)
