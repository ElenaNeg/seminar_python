# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# Входные данные	Выходные данные
# 1 2 2 3 3 3	1

# sp = [int(i) for i in input().split()]
# for el in sp:
#     if sp.count(el) == 1:
#         print(el)

# 2. Дан список чисел. Выведите все элементы списка, которые больше 
# предыдущего элемента.

# sp = [int(i) for i in input().split()]
# for i in range(len(sp) - 1):
#     if sp[i] < sp[i + 1]:
#         print(sp[i + 1], end = ' ') # , end = ' ' - данная запись позволяет все записать в строку через запятую.

# 3.	Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

# import time
# t = str(time.time())[-3:]

# print(t)

# # var 2:
# import time


# def myrandom(x):
#     t = str(time.time())[-x:]
#     print(t)


# myrandom(4)

# 4.	Задайте список. Напишите программу, которая определит, присутствует
#  ли в заданном списке строк некое число.
# 12
# # Строка1
# # Строка2
# # Строка3
# # Строка45
# # Стр12ка
# list = []
# count = 0
# a = input()
# for i in range(5):
#     s = input()
#     list.append(s)

# for el in list:
#     if a in el:      # или if str12 in el:
#         count += 1
# if count >= 1:
#     print('Да')
# else:
#     print('нет')  


# 5.	Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.
# •	список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# •	список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# •	список: [], ищем: "123", ответ: -1

# sp = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find = 'ert'
# count = 0
# for i in  range(len(sp)):
#     if sp[i] == find:
#         count +=1
#     if count == 2:
#         print(i)
#         break
# if count <= 1:
#     print(-1)

# 1.	Дан список чисел. Определите, сколько в нем встречается различных чисел.
# 1 5 2 2 2 4	4

# sp = [1, 5, 2, 2, 2, 4]
# print(len(set(sp)))   #(set(sp)) - чтобы избавить список от повторов, можно обернуть его в set(sp) set- множество.

# 2.	Даны два списка чисел. Найдите все числа, которые входят как в первый, 
# так и во второй список и выведите их в порядке возрастания
# 1 3 2
# 4 3 2	      2 3

# sp1 = [1, 3, 2]
# sp2 = [4, 3, 2]
# print(set(sp1) & set(sp2))   # числа входящие как в первый так и во второй список.
# print(*set(sp1) & set(sp2))  # числа входящие как в первый так и во второй список. только без {} 
# print(*set(sp1) | set(sp2))  # перечисление всех переменных без повтора

# 3.	Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:
# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#          'D': '-..', 'E': '.', 'F': '..-.',
#          'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..',
#          'M': '--', 'N': '-.', 'O': '---',
#          'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-',
#          'V': '...-', 'W': '.--', 'X': '-..-',
#          'Y': '-.--', 'Z': '--..'}

# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#          'D': '-..', 'E': '.', 'F': '..-.',
#          'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..',
#          'M': '--', 'N': '-.', 'O': '---',
#          'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-',
#          'V': '...-', 'W': '.--', 'X': '-..-',
#          'Y': '-.--', 'Z': '--..'}
# print(MORSE['A'])
# s = 'Help me SOS'.upper().split()  # .upper() - делает все буквы заглавными
# for j in s:
#     for i in j:
#         if i in MORSE:
#             print(MORSE[i], end = ' ')
#         else:
#             print(i, end = ' ')
#     print()