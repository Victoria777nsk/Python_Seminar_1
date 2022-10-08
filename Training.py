#1 Выяснить, является ли число четным.
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print(f'Число {number} четное')
# else:
#     print(f'Число {number} нечетное')



#2 Вывести все четные числа от 1 до N.
# number = int(input('Введите число: '))
# number2 = 2
# if number > 1:
#     while number2 <= number:
#         print(number2)
#         number2 += 2
# else:
#     print(f'Ошибка! Число {number} должно быть > 1!')

# 2-ой вариант решения:
# number = int(input('Введите число: '))
# for i in range(2, number + 1, 2):
#     print(i)



# Задача 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8, 9 -> нет

# numberA = int(input('Введите первое число: '))
# numberB = int(input('Введите второе число: '))
# if numberA * numberA == numberB:
#     print(f'Число {numberB} является квадратом числа {numberA}') 
# elif numberB * numberB == numberA:
#     print(f'Число {numberA} является квадратом числа {numberB}')
# else:
#     print(f'Ни одно из чисел не является квадратом другого')



# Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# numbers = [3, 45, 78, 4, 9]
# max = numbers[0]
# for i in numbers:
#     if i > max:
#         max = i
# print(f'Максимальное число = {max}')

# Ввод 5 чисел пользователем:
# my_list = [int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))]
# print(my_list)
# max = my_list[0]
# for i in my_list:
#     if i > max:
#         max = i
# print(f'Максимальное число = {max}')


# Задача 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = int(input('Введите число: '))
# for i in range(-number, number + 1):
#     print(i)

# Вывод через строку (НЕ числа):
# number = int(input('Введите число: '))
# s = ' '
# for i in range(-number, number + 1):
#     s += str(i) + ' '
# print(s)

# Решение через функцию:
# def get_numbers():
#     num = int (input ('Введите число: '))
#     return [i for i in range (-num, num + 1)]
# print(get_numbers())



# Задача 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# print(int (float (input("Введите дробное число: ")) * 10) % 10)



# Задача 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# number = int(input('Введите число: '))
# if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
#     print("Число удовлетворяет условию")
# else:
#     print("Число НЕ удовлетворяет условию")

# Решение через функцию:
# def check_mult():
#     num = int (input ('Введите число: '))
#     return (num % 5 == 0 or num % 10 == 0 or num % 15 ==0) and num % 30 != 0
# print (check_mult()) - вывод True или False