'''Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
'''
import random

# Вводим число элементов первого и второго массива

a = int(input("A:"))
b = int(input("B:"))
limit = int(input("Ввведите пределы: "))


def array_filling(a, n):
    '''Функция заполнения массива рандомными числами'''
    array = []
    for _ in range(a):
        array.append(random.randint(-n, n))
    return array


first_array = array_filling(a, limit)
second_array = array_filling(b, limit)

print(first_array, "\n", second_array)


for i in first_array:
    for k in second_array:
        if i == k:
            first_array.remove(i)
print(first_array)
