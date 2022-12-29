# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# d = 0.001
# k = 0
# while d < 1:
#     d *= 10
#     k += 1
# print(round(pi, k))


# Задача 2. Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

# def list_of_prime_factors(number):
#     res = []
#     d = 2
#     while d <= number // 2 + 1:
#         if number % d == 0:
#             res.append(d)
#             number //= d
#         else:
#             d += 1
#     if number > 1:
#         res.append(number)
#     return res
# print(list_of_prime_factors(87))


# Задача 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# list = [6, 1, 4, 4, 1, 2, 3]
# res = []

# for i in list:
#     if list.count(i) == 1:
#         res.append(i)
# print(res)

# Задача 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в 
# файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# def list_of_coefficients(factors):
#     k = len(factors) - 1
#     res = ""
#     for i in range(0, len(factors)):
#         if i == len(factors) - 1:
#             res += f"{factors[i]}"
#         elif k == 1:
#             res += f"{factors[i]}x + "
#         else:
#             res += f"{factors[i]}x^{k} + "
#         k -= 1
#     return res
# def polinome(k, file_name):
#     factors = [randint(1, 101) for _ in range (0, k + 1)]
#     res = list_of_coefficients(factors)
#     print(res)
#     with open(file_name, "w", encoding="utf-8") as f:
#         f.write(' '.join([str(i) for i in factors[::-1]]) +'\n')
#         f.write(res)

# polinome(3, 'file1.txt')
# polinome(3, 'file2.txt')   

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.78

def list_of_coefficients(factors):
    k = len(factors) - 1
    res = ""
    for i in range(0, len(factors)):
        if i == len(factors) - 1:
            res += f"{factors[i]}"
        elif k == 1:
            res += f"{factors[i]}x + "
        else:
            res += f"{factors[i]}x^{k} + "
        k -= 1
    return res
pol_1 = []
with open("file1.txt") as f1, open('file2.txt') as f2:
    factors1 = [int(i) for i in f1.readline().split()]
    factors2 = [int(i) for i in f2.readline().split()]
if len(factors2) == len(factors1):
    res = [a + b for a, b in zip(factors1, factors2)]
elif len(factors1) > len(factors2):
    res =factors1.copy()
    for i in range(len(factors2)):
        res[i] += factors2[i]
else:
    res = factors2.copy()
    for i in range(len(factors1)):
        res[i] += factors1[i]
with open('file3.txt', 'w') as f:
    f.write(list_of_coefficients(res[::-1]))
    



