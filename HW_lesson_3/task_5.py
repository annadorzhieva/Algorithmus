'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random

SIZE = 10
MIN_ITEM = -12
MAX_ITEM = 10
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(arr)

i = 0
index = -1
while i < SIZE:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i +=1

print('Максимальный отрицательный элемент:', arr[index], 'на позиции:', index+1)
