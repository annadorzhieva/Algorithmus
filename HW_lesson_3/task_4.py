'''
4. Определить, какое число в массиве встречается чаще всего.
'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 7
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

num = arr[0] # самый встречаемый элемент
t_max = 1 # число встречаемости
for i in range(SIZE - 1):
    t = 1
    for k in range(i + 1, SIZE):
        if arr[i] == arr[k]:
            t += 1
    if t > t_max:
        t_max = t
        num = arr[i]

if t_max > 1:
    print(f'число %d встречается %d раз(a)' % (num, t_max))
else:
    print('Одинаковых чисел в массиве нет')
