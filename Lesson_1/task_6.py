'''
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''
n = int(input('Введите номер буквы алфавита: '))
n = ord('n') + n - 1
print('Это буква:', chr(n))
