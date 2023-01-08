# 1.	Задайте строку из набора чисел. Напишите программу, которая покажет 
# большее и меньшее число. В качестве символа-разделителя используйте пробел

# s = input('Введите набор чисел ').split()
# print(s)
# s = [int(i) for i in s]  # сразу превратим наш список в цифры
# print(s)
# print (f'Максимум: {max(s)}')
# print (f'Минимум: {min(s)}')

# 2.	Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1.	с помощью математических формул нахождения корней квадратного уравнения
# 2.	с помощью дополнительных библиотек Python

# f = '5x^2 + 3x + -7 = 0'
# f = f[:-3]
# print(f)
# f = f.split('+') 
# print(f)
# sp = []
# for i in f:
#     sp.append(int(i.split('x')[0]))
# print(sp)
# a,b,c = sp
# d = b**2 -4 * a * c
# print(d)
# if d > 0:
#     x1 = round((-b -d**0,5)/(2*a), 2)
#     x2 = round((-b +d**0,5)/(2*a), 2)
#     print(x1, x2)
# elif d == 0:
#     x1 = (-b)/(2*a)
#     print(x1)
# else:
#     print('Корней нет')


# import math 


# f = '5x^2 + 3x + -7 = 0'
# f = f[:-3]
# print(f)
# f = f.split('+') 
# print(f)
# sp = []
# for i in f:
#     sp.append(int(i.split('x')[0]))
# print(sp)
# a,b,c = sp
# d = b**2 -4 * a * c
# print(d)
# if d > 0:
#     x1 = round((-b - math.sqrt(d))/(2*a), 2)
#     x2 = round((-b + math.sqrt(d))/(2*a), 2)
#     print(x1, x2)
# elif d == 0:
#     x1 = (-b)/(2*a)
#     print(x1)
# else:
#     print('Корней нет')

# 3.	Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

# a = int(input('Задайте число: '))
# b = int(input('Задайте второе число: ')) 
# if a > b:
#     for i in range(1, b+1):
#         if a * i % b == 0:
#             print(a*i)
#             break
# elif a<b:
#     for i in range(1, a+1):
#         if b * i % a == 0:
#             print(b*i)
#             break
# else:
#     print(a)

# 4.	В единственной строке записан текст. Для каждого слова из данного текста
#  подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.
# #1
# slovar = {'login': 'Ivan', 'password': '123'}
# login = 'Ivan'
# password = '123'
# if login == slovar['login'] and password == slovar['password']:
#     print('Доступ разрешен')
# else:
#     print('Неверная пара логин/пароль')
# #2
# slovar['email'] = 'iv@mail.ru'
# print(slovar)
# print(slovar.items()) #items перебор кортежа
# for key, value in slovar.items():
#     print(key, value)  # key, value - ключ значения.

# #3 задача на число повторений с применением словаря.

# Объяснение словарей:
# stroka = 'aabbbcccc' # a-2 b-3 c-4
# slovar = {}
# for i in stroka:
#     if i in slovar:
#         slovar[i] += 1
#     else:
#         slovar[i] = 1
# print(slovar)
# print(slovar.get('a')) # запишем выше конструкцию покороче через функцию get. 
# Если ввести неизвестную переменную, которой нет, то выйдет 
# none print(slovar.get('i')).  а чтобы вернул не  none а 0, 
# то нужно записать так:  print(slovar.get('i', 0)) 

# #вариант 2 

# stroka = 'aabbbcccc' # a-2 b-3 c-4
# slovar = {}
# for i in stroka:
#     slovar[i] = slovar.get(i, 0) + 1 # 
# print(slovar)

# # Решение задачи 3.
# stroka = "one two one two three".split(" ")
# slovar = {}
# for i in stroka:
#     slovar[i] = slovar.get(i, -1) + 1 # -1 -вернет 0, а если (i, 0) то вернет 1
#     print(slovar[i], end =' ')
# print(slovar)

# 5.	Вам дан словарь, состоящий из пар слов. Каждое слово является 
# синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Входные данные	Выходные данные
# 3                  Bye
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye	

# slovar = {}
# for i in range(3):
#     key, value = input().split()
#     slovar[key] = value
# print(slovar)
# a = input('Введите слово: ')
# for key, value in slovar.items():
#     if a == key:
#         print(value)
#     elif a == value:
#         print(key)
        
# 6.	Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Входные данные	                   Выходные данные
# 1
# apple orange banana banana orange	        banana

stroka = "apple orange banana banana orange".split(" ")
slovar = {}
for i in stroka:
    slovar[i] = slovar.get(i, 0) + 1 # -1 -вернет 0, а если (i, 0) то вернет 1
print(slovar)
maxi = max(slovar.values())  # если записать только maxi - то у нас найдет 2 максимума бананы и апельсины так как они 2 раза встречаються. Но чтобы мы можем выделить только максимум по алфавиту который встретиться первым. добавим нахождение минимума.
mini = 'z'
for key, value in slovar.items():
    if value == maxi:
        if key < mini:
            mini = key
        print(key, end = " ")
print(mini)    

