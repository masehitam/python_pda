import string
from collections import defaultdict


# basic python
# name = input("please enter your name")
# nim = input('please enter your nim')
#
# print('Hello welcome to IF 5100 class !')
# print('My name is {}, m11y identity 1number is {}'.format(name, nim))
# print(f'My name is {name}, my identity number is {nim}')
# print('My name is ' + name + ', my identity number is ' + nim)
# print('My name is', name, ', my identity number is', nim)

# conditional statemen and looping
# def operations_by_input(a: int, b: int):
#     if a and b > 0:
#         if a > 10:
#             if b >= 10:
#                 print(a / b)
#             else:
#                 # B < 10
#                 print(a + b)
#         else:
#             # A <= 10
#             if b >= 10:
#                 print(a * b)
#             else:
#                 # B < 10
#                 print(a - b)
#                 pass
#     else:
#         print('Input number <A> and <B> is invalid!')


# operations_by_input(10, 10)

# a = int(input('please input A : '))
# for x in range(a):
#     b = int(input('please input B : '))
#     if b < 0:
#         # ternary operations
#         a += b if b > a else a - b
#         # if b > a :
#         #     a += b
#         # else:
#         #     a -= b
#     else:
#         print(a)

# abstrac and function
# n = int(input())
# for i in range(n):
#     print('*' * (i + 1))


# abstrac and function string operations
# def reverse_string(word1: str, word2: str = ''):
#     return word2[::-1] + word1[::-1]
#
#
# def loopingWord(word: str, n: int = 1):
#     for i in range(n):
#         print(word + str(i))
#
#
# print(reverse_string('Happy'))
# print(reverse_string('Coding', 'Happy'))
# print(reverse_string('Study', 'Boring'))
# loopingWord('yppaHngidoC', 4)

# Modules and Files
# odd_numbers = []
# while len(odd_numbers) <= 5:
#     try:
#         num = int(input("input number : "))
#         if num % 2 == 1:
#             odd_numbers.append(str(num))
#     except:
#         print('input bukan number')
#
# # file_handler = open("First_Ten_Odd_Numbers.txt", 'w')
# # file_handler.write('\n'.join(odd_numbers))
# # file_handler.close()
#
# with open("First_Ten_Odd_Numbers.txt", 'w') as file_handler:
#     file_handler.write('\n'.join(odd_numbers))
#
# # file_reader = open("First_Ten_Odd_Numbers.txt", 'r')
# # for i in file_reader:
# #     print(i, end='')
# # file_reader.close()
#
# with open("First_Ten_Odd_Numbers.txt", 'r') as file_reader:
#     for i in file_reader:
#         print(i, end='')

# Data structures
# univs = ['ITB', 'UI', 'UGM', 'ITS', 'UNPAD', 'UNDIP', 'USU']
# iDelete = int(input('masukan index hapus : '))
# del univs[iDelete]
# print(univs)

# iNumber = [[8, 9, 2], [-4, 1, -1], [0, 3, 1], [7, 5, 6]]
# for i in iNumber:
#     print(i)
#
# personInfo = [
#     {},
#     {
#         'name' : 'Andi',
#         'age' : 25,
#         'nim' : 23523018
#     },
#     {
#         'name' : 'Budi',
#         'age' : 23,
#         'nim' : 23523019
#     },
#     {
#         'name' : 'Cynthia',
#         'age' : 28,
#         'nim' : 23523020
#     },
# ]
# for i in personInfo:
#     print(i)

def count_word(lyr: list):
    num_lyrics = defaultdict(int)
    for word in lyr:
        num_lyrics[word] += 1

    return dict(num_lyrics)


lyrOg = "Indonesia tanah airku Tanah tumpah darahku Di sanalah aku berdiri Jadi pandu ibuku Indonesia kebangsaanku Bangsa dan tanah airku Marilah kita berseru Indonesia bersatu Hiduplah tanahku Hiduplah neg'riku Bangsaku rakyatku semuanya Bangunlah jiwanya Bangunlah badannya Untuk Indonesia Raya"
translator = str.maketrans('', '', string.punctuation)
lyrList = lyrOg.lower().translate(translator).split(' ')
print(count_word(lyrList))
