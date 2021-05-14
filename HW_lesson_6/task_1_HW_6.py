'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
'''

'''64-разррядная ОС, Windows 10
Python 3.8.5'''

import sys
import random

# вариант 1
SIZE = 6
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

even = []
for i in range(SIZE):
    elem = arr[i]
    index = i
    if elem % 2 == 0:
        even.append(i)
print(arr)
print(even)

size_1 = 0
size_1 += sys.getsizeof(even)
size_1 += sys.getsizeof(elem)
size_1 += sys.getsizeof(index)
size_1 += sys.getsizeof(arr)

# вариант 2
N = 6
arr = [0] * N
even = []
for i in range(N):
    arr[i] = random.randint(100, 200)
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print(even)

size_2 = 0
size_2 += sys.getsizeof(arr)
size_2 += sys.getsizeof(even)
size_2 += sys.getsizeof(i)

print(size_1)
print(size_2)

'''
в первом варианте памяти затрачивается больше, чем во втором. Я думаю, что это связано с затратой памяти на элемент массива
'''


