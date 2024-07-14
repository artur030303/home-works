# my_list = [24, 0, -4, 77, 3457]

# 1.
"""Найти наибольшее и наименьшее значение в списке"""

# print(min(my_list), max(my_list))


# 2.
"""Найти среднее арифметическое из списка чисел"""

# print(sum(my_list) / len(my_list))


# 3.
"""Найти второе по величине значение в списке ( [10, 2, 5, 8, 0] -> результат 8)"""

# print(sorted(my_list)[1])


# 4.
"""Проверить является ли список уже отсортированным."""

# if sorted(my_list) == my_list:
#     print('yes')
# else:
#     print('no')

# 5.
"""Используя any, выяснить есть ли в списке положительные числа"""

# print(any(x > 0 for x in my_list))

# 6.
"""Используя all, выяснить все ли числа в списке четные"""

# print(all(x % 2 == 0 for x in my_list))


# 7.
"""Заданы два числа, вывести все нечетные значения между ними"""

# num_1 = int(input('Number 1: '))
# num_2 = int(input('Number 2: '))

# for i in range(num_1, num_2+1):
#     if i % 2:
#         print(i)


# 8.
"""Заданы два числа, найти сумму всех значений между ними"""

# num_1 = int(input('Number 1: '))
# num_2 = int(input('Number 2: '))

# print(sum(range(num_1, num_2+1)))

# 9.
"""Заданы два числа, вывести все числа между ними в обратном порядке"""

# num_1 = int(input('Number 1: '))
# num_2 = int(input('Number 2: '))

# for i in range(num_2, num_1-1, -1):
#     print(i)


# 10.
"""Сложная! Используя цикл for, range и свойства списков найти заданное число Фибоначчи"""

# тут я немного намудрил.хотел через Comprehension попробовать(если у нас есть список чисел), что бы так сказать лучше усвоить

# while True:
#     try:
#         n = int(input("Задайте число: "))
#     except ValueError:
#         print("Введите число")
#     else:
#         break

# numbers_f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
#              233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]

# my_num = [x for x in numbers_f if x == numbers_f[n-1] + numbers_f[n-2]]
# result = str(my_num[0])

# print(f"{n} = {result} число Фибоначчи")
#
#
#
# тут уже нормальный вариант

# n = int(input("Задайте число: "))

# first_num_fib, second_num_fib = 0, 1

# for i in range(n):
#     first_num_fib, second_num_fib = second_num_fib, first_num_fib + second_num_fib

# fib_num = first_num_fib

# print(f"{n} = {fib_num} число Фибоначчи")
#
#
#
""" 1.Создать список чисел от 5 до 100"""

# numbers = [x for x in range(5, 101)]

# print(numbers)
#
#
#
""" 2.Создать список нечетных чисел от 5 до 100"""

# odd_numbers = [x for x in range(5, 101) if x % 2]

# print(odd_numbers)
#
#
#
""" 3.Есть список слов, создать список который будет содержать первые буквы из каждого слова"""

# my_list = ['red', 'blue', 'green', 'white']

# new_list = [x[0] for x in my_list]
# print(new_list)
#
#
#
""" 4.Не связано с компрехеншенами. Из прошлого списка сделать строку"""

# my_list = ['red', 'blue', 'green', 'white']
# my_str = ','.join(my_list)

# print(my_str)
#
#
#
""" 5.Есть список чисел. Создать список на его основе, но взять только отрицательные значения"""

# my_list = [12, 56, 34, -6, 75, -56, 45, -333, 445, -34]

# negative_numbers = [x for x in my_list if x < 0]

# print(negative_numbers)
#
#
#
""" 6.Создать список квадратов чисел в указанном пользователем диапазоне"""

# try:
#     first_num = int(input("Введите число от: "))
#     end_num = int(input("Введите число до: "))
# except ValueError:
#     print("Вы ввели не число")

# list_of_squares = [x**2 for x in range(first_num, end_num+1)]

# print(list_of_squares)
#
#
#
#
"""""""""""""""""""""""""""""""Работа с файлами"""""""""""""""""""""""""""""""""""""


""" 1.Чтение файла и вывод его содержимого: Cоздайте текстовый
 файл sample.txt с несколькими строками текста. Написать
 программу, которая открывает файл и выводит его содержимое
 на экран.
"""

# with open('sample.txt', 'r') as file:
#     text = file.read()
#     print(text)
#
#
#
""" 2.Запись в файл: Написать программу, которая запрашивает у
пользователя несколько строк текста и записывает их в файл с
именем output.txt."""

# with open('output.txt', 'w') as file:
#     text = file.write(input("Напишите несколько строк"))
#     print(text)
#
#
#
""" 3.Копирование файла: Создайте два текстовых файла source.txt и
 destination.txt. Написать программу, которая читает содержимое
 source.txt и записывает его в destination.txt."""

# with open('source.txt', 'r') as file:
#     text = file.read()
#     with open('destination.txt', 'w') as file:
#         new_text = file.write(text)

""" 4.Анализ файла: Создайте текстовый файл со списком чисел. Написать
 программу, которая читает файл, и печатает самое большое число из файла."""


# with open('list_numbers.txt', 'r') as file:
#     text = file.read()

#     numbers = [int(num) for num in text.split()]

# max_number = max(numbers)
# print(max_number)
#
#
#
""" 5.Конвертация файлов: Создайте текстовый файл с температурами в градусах
Цельсия. Написать программу, которая читает файл, конвертирует температуры
в градусы Фаренгейта и записывает результаты в новый файл."""

# with open('temp_of_celsius.txt', 'r') as file:
#     celsius_num = file.read()
#     fahrenheit_numbers = [str(int(num)*9/5 + 32)
#                           for num in celsius_num.split()]
# with open('temp_fahrenheit_numbers.txt', 'w') as file:
#     text_in_fahrenheit_numbers_txt = file.write(', '.join(fahrenheit_numbers))
#
#
#
""" 6.Подсчет слов в файле: Написать программу, которая считает количество слов
 в текстовом файле."""

# with open('text_word_count.txt', 'r') as file:
#     text_file = file.read()
#     text_count = len(text_file.split())

# print(text_count)
#
#
#
""" 7.FizzBuzz: Реализовать физбаз с прошлого занятия, но записывать результаты
 в файл"""


count = 1
try:
    n = int(input("Введите число до которого хотите считать: "))
    first_divisor = int(input("Введите первый делитель: "))
    second_divisor = int(input("Введите второй делитель: "))

    result = []

    while count <= n:
        if count % first_divisor == 0 and count % second_divisor == 0:
            result.append('FizzBuzz')
        elif count % first_divisor == 0:
            result.append('Fizz')
        elif count % second_divisor == 0:
            result.append('Buzz')
        else:
            result.append(str(count))
        count += 1

        with open("FizzBuzz.txt", 'w') as file:
            file.write('\n'.join(result))
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("Вы пропускали уроки математики в школе и поэтому пытаетесь делить на 0")
