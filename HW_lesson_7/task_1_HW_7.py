'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''
import random

def bubble(desc):
    n = 1
    while n < len(desc):
        count = 0

        for i in range(len(desc) - 1 - (n - 1)):
            if desc[i] < desc[i + 1]:
                desc[i], desc[i + 1] = desc[i + 1], desc[i]
                count += 1
        if count == 0:
            break
        n += 1

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Исходный массив:', array)
bubble(array)
print('После сортировки:', array)
