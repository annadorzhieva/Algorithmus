'''
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только
из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
'''

import hashlib

string = input('Введите строку из маленьких латинских букв')

sum_string = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_string.add(hash_str)

print(f'{len(sum_string) -1} различных подстрок в строке {string}')