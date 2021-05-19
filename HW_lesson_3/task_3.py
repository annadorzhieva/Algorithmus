'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

a = arr[1]
min_ = 0
max_ = 0
for i in range(SIZE):
    if arr[i] < arr[min_]:
        min_ = i
    elif arr[i] > arr[max_]:
        max_ = i

print(arr)
print('arr[%d]=%d arr[%d]=%d' % (min_+1, arr[min_], max_+1, arr[max_]))

b = arr[min_]
arr[min_] = arr[max_]
arr[max_] = b

for i in range(SIZE):
    print(arr[i], end=' ')
print()
