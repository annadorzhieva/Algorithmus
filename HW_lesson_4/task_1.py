'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''
from random import randint
import timeit
import cProfile

# №1
SIZE = 6
MIN_ITEM = 0
MAX_ITEM = 50
arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

def MyVar():
    even = []
    for i in range(SIZE):
        elem = arr[i]
        index = i
        if elem % 2 == 0:
            even.append(i)
    return even

# №2
def MyVar2():
    N = 5
    arr = [0] * N
    even = []
    for i in range(N):
        arr[i] = randint(10, 19)
        if arr[i] % 2 == 0:
            even.append(i)
    return even

print(timeit.timeit(MyVar)) # 1.6750475     Первый вариант работает быстрее
print(timeit.timeit(MyVar2)) # 8.3769695

cProfile.run('MyVar()')
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:16(MyVar)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''

cProfile.run('MyVar2')
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# В первом случае вызывается 6 функций, во втором 3 - это значит,что первый вариант дольше второго (хотя не уверена)