# Задание 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
 
# stroka = input().split()
# res = list(filter(lambda s: 'абв' not in s, stroka))
# print( ' '.join(res))

# Задание 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# import random
# from random import randint, choice
 
# messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
#             'Сколько конфет берем?', 'берите еще', 'Ваш ход']
# max_number_move = 0
 
# def introduce_players():
#     player1 = input('Представьтесь\n')
#     player2 = 'SmartBOT'
#     print(f'Очень приятно, сегодня Вы играете с {player2}')
#     return [player1, player2]
 
# def sweets_game(players):
#     global max_number_move
#     total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
#     max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
#     first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [total_sweets, max_number_move, int(first)]
 
# max_move = max_number_move
 
# def game_player_vs_smart_bot(sweets, players, messages):
#     global max_number_move
#     count = sweets[2]
 
 
#     while sweets[0] > 0:
#         if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
#             move = sweets[0] -1
#             print(f'Я забираю {move}')
 
#         elif not count % 2:
#             move = random.randint(1, sweets[1])
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > sweets[0] or move > sweets[1]:
#                 print(
#                     f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
#                 chance = 2
#                 while chance > 0:
#                     if sweets[0] >= move <= sweets[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {chance} попытки')
#                     move = int(input())
#                     chance -= 1
#                 else:
#                     return print(f'Попыток не осталось. Game over!')
#         sweets[0] = sweets[0] - move
#         if sweets[0] > 0:
#             print(f'Осталось {sweets[0]} конфет')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]
 
# players = introduce_players()
# sweets = sweets_game(players)
 
# winer = game_player_vs_smart_bot(sweets, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


# Задание 3. Создайте программу для игры в ""Крестики-нолики"".

# print('*'*100)
# print('\n')
# print('А теперь давайте сыграем в крестики нолики!')

# board = list(range(1,10))

# def design_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*12)

# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
#         try:
#             player_index = int(player_index)
#         except:
#             print('Выберите другую позицию')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Попробуйте еще')

# def vector_check(board):
#     vector = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in vector:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False

# def game(board):
#     counter = 0
#     vec = False
#     while not vec:
#         design_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             tt_win = vector_check(board)
#             if tt_win:
#                 print(tt_win,'Победил')
#                 vec = True
#                 break
#             if counter == 9:
#                 print('Победила, ДРУЖБА)')
#         design_board(board)
# game(board)

# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
# данных.

def compression(text):
    res = ''
    count = 1 
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            res += str(count) + text[i - 1]
            count = 1 
    res += str(count) + text[i]
    return res

def recovery(text):
    res = ''
    digit = ''
    for i in range(0, len(text)):
        if text[i].isdigit():
            digit += text[i]
        else:
            res += int(digit) * text[i]
            digit = ''
    return res

if __name__ == '__main__':
    with open('input_data.txt') as file:
        text = file.readline().strip()
    print(text)
    compression_text = compression(text)
    print(compression_text)
    with open('compression.txt', 'w') as file:
        file.write(compression_text)
    recovery_text = recovery(compression_text)
    with open('recovery.txt', 'w') as file:
        file.write(recovery_text)
    print(recovery_text)


