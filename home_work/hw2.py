# Задача 1.Напишите программу, которая принимает на вход вещественное число и
#  показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# str = float(input("Введите число: "))
# sum = 0
# while str != int(str):
#     str *= 10
# while str > 0:
#     sum += str % 10
#     str //= 10
# print(int(sum))

# # var1.1. 
# print('Введите число')
# a = input()
# s = 0
# for i in a:
#     if i.isdigit():
#         s += int(i)   # i.isdigit() - это обозначает цифра.
# print(s)


# Задача 2. Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# f = 1

# for i in range(n):
#     i += 1
#     f *= i 
#     print(f, end=', ')

#  вариант 2 зад 2.

# n = int(input("Введите число: "))
# p = 1
# for i in range(1, n + 1):
#     p = p * i 
#     print(p, end=' ')

# Задача 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
  
# n = int(input('Введите число: '))
# sum = 0

# for i in range(n):
#     i += 1
#     sum += ((1 + 1/n) ** n)
# print(round(sum, 2))

# вариант 2. зад 3

# print('Введите N: ')
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += ((1 + 1 / i) ** i)
# print(round(sum, 2))

# Задача 4. Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# print('Введите n ')
# n = int(input())
# list = []

# for i in range(-n, n + 1):
#     list.append(i)
# print(list)
# with open('file.txt', 'r') as f:
#     inds = f.readlines()
# multiple = 1
# for i in inds:
#     multiple += list[int(i)]
# print(multiple)

# Задача 5.	Реализуйте алгоритм перемешивания списка 
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

# import random
# list = [0, 1, 2, 3, 4]
# for i in range(0, len(list)):
#     a = random.randint(0, len(list) - 1)
#     list[i], list[a] = list[a], list[i]
# print(list)



    




