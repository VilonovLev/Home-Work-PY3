import math
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

# 1 решение
list_num = [0, 1, 0, 1, 0, 1, 0, 1]
_sum = 0
for i in range(1, len(list_num), 2):
    _sum += list_num[i]
print(f"Cумма элементов с нечетным индексом: {_sum}")
# 2 решение
_sum = sum(i for i in  list_num if list_num.index(i) % 2 != 0)
print(f"Cумма элементов с нечетным индексом: {_sum}")

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
num_list = [2, 3, 5, 6, 5]
print(num_list)
print(list(num_list[i]*(num_list[-i - 1]) for i in range(math.ceil(len(num_list)/2))))

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
real_nums = [1.1, 1.2, 3.1, 5.6, 10.01]
remains = [(real_nums[i] - math.floor(real_nums[i])) for i in range(len(real_nums))]
print(f"Разница между Max & Min дробными частями: {round(max(remains) - min(remains),2)}")

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# 1 вариант
n = int(input("Введите число N: "))
k = n
result = ""
while n > 0:
    result = str(n % 2) + result 
    n //= 2
print(f"Число N в двоичном виде: {result}")
# 2 вариант
print(f"Число N в двоичном виде: {bin(k)[2:]}")

# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
x = int(input("Задайте число: "))
fib_num = [0]
if x > 0:
    fib_num.append(1)
    fib_num.insert(0, 1)
if x > 1:
    fib_num.append(1)
    fib_num.insert(0, -1)
if x > 2:
    for i in range(x - 2):
        fib_num.append(fib_num[-1] + fib_num[-2])
        fib_num.insert(0, fib_num[1] - fib_num[0])
print(fib_num)
