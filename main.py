# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# |||||||||||||||||||||||||||||||||
# my_list = [2, 3, 5, 9, 3,1,1,0,3]
# res = 0
# for item in range(1, len(my_list), 2):
#     res += my_list[item]
# print(f'Список чисел {my_list}')
# print(f'Сумма элементов списка, стоящих на нечетной позиции = {res}')
#________________________________________________
# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
# ||||||||||||||||||||||||||||||||||||||
# roster = [2, 3, 4, 5, 6]
# my_list = []
# count, num = 0, 0
# for item in roster:
#     count += 1
# if count % 2 == 0:
#     num = (count//2)
# else:
#     num= (count//2)+1
# for i in range(num):
#     res = roster[i]*roster[-(i+1)]
#     my_list.append(res)
# print(f'{roster} => {my_list}')
#_______________________________________________________
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#|||||||||||||||||||||||||||||||||||||||||||||||||
# my_list = [1, 1.04, 3.1, 15.02,9, 10.02, 9, 1.8, 1.3, 2.09, 1.2, 10000.02]
# work_list = []
# for item in my_list:
#     if type(item) == float:
#         work_list.append(item) # закидываем в новый список только числа float
# print(work_list)
# my_list1 = []
# for item in work_list:
#     res = (int(item * 100) % 100) * 100
#     my_list1.append(res) # возводим числа после . в целые
# print(my_list1)
# max_num = 0
# min_num = my_list1[0]
# for item in my_list1:
#     if item > max_num:
#         max_num = item # Находим максимальное число
#     if item < min_num:
#         min_num = item # Находим минимальное число
# print(min_num)
# print(max_num)
# print(f'Список {my_list} => {float(max_num - min_num)/10000}')
#__________________________________________________________________________
# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
#|||||||||||||||||||||||||||||||||||||||
# a = 45
# res = ''
# while a > 0:
#     res = str(a % 2) + res
#     a = a // 2
# print(res)
#________________________________________________________
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num = 8
f1 = 0
f2 = 1
i = 0
fib_list = []
while i < num:
    f_summa = f1 + (-f2)
    f1 = f2
    f2 = f_summa
    num -= 1
    fib_list.append(f1)
print(fib_list)
fib1_list = []
for i in fib_list:
    i = i * (-1)
    if i < 0:
        i = i * (-1)
        fib1_list.append(i)
    else:
        fib1_list.append(i)
fib_list.reverse()
for i in fib1_list:
    fib_list.append(i)
print(fib_list)



