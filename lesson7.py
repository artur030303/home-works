""" 1.Простое сложение. Напишите функцию add_numbers, которая принимает 
два целых числа и возвращает их сумму."""


# def add_numbers(a: int, b: int) -> int:
#     result = a+b
#     return result

# print(add_numbers(1, 7))
#
#
#
""" 2.Приветствие. Напишите функцию greet, которая принимает строку name и 
возвращает приветственное сообщение."""

# def greet(name: str) -> str:
#     return f"Hello " + name

# print(greet('Artur'))
#
#
#
""" 3.Факториал числа. Напишите функцию factorial, которая принимает целое число
 и возвращает его факториал."""

# def factorial(num: int) -> int:
#     factorial_of_num = 1
#     for i in range(2, num+1):
#         factorial_of_num *= i
#     return factorial_of_num

# print(factorial(5))
#
#
#
""" 4.Среднее значение. Напишите функцию average, которая принимает произвольное 
количество чисел и возвращает их среднее значение. Подумайте какие там будут 
типы данных"""


# def average(*args) -> float:
#     for arg in args:
#         return sum(args) / len(args)


# print(average(1, 2, 3, 5, 5, 7))
#
#
#
""" 5.Форматирование строки. Напишите функцию format_string, которая принимает строковый 
шаблон и произвольное количество именованных аргументов для подстановки в шаблон.
 Например format_string("some {value1}, another {value2}", value1="test", value2="something_else")"""


# def format_string(template: str, **kwargs: dict) -> str:
#     return template.format(**kwargs)


# print(format_string("some {value1}, another {value2}",
#                     value1="test", value2="something_else"))
#
#
#
""" 6.Объединение словарей. Напишите функцию merge_dicts, которая принимает произвольное количество словарей
 и объединяет их в один."""


# def merge_dicts(*args: dict) -> dict:
#     result = {}
#     for arg in args:
#         result.update(arg)
#     return result


# print(merge_dicts({'age1': 35, 'name1': 'Jan'}, {'age': 30, 'name': "David"}))
#
#
#
""" 7.Четные и нечетные числа. Напишите функцию even_odd, которая принимает произвольное количество целых чисел и
 возвращает кортеж из двух списков: один с четными числами, другой с нечетными. Продумайте типизацию"""


# def even_odd(*args: int) -> tuple[list[int],list[int]]:
#     even_numbers = []
#     odd_numbers = []
#     for arg in args:
#         if arg % 2 == 0:
#             even_numbers.append(arg)
#         else:
#             odd_numbers.append(arg)

#     return even_numbers, odd_numbers


# print(even_odd(34, 45, 25, 44, 3, 2, 44, 55, 778, 5))
#
#
#
""" 8.Фильтрация списка. Напишите функцию filter_list которая принимает список целых чисел и пороговое значение, и 
возвращает новый список с числами из оригинального списка, которые больше порога. Продумайте типизацию."""


# def filter_list(list_integers: list[int], threshold_value) -> list[int]:
#     beyond_the_threshold = []
#     for numbers in list_integers:
#         if numbers > threshold_value:
#             beyond_the_threshold.append(numbers)
#     return beyond_the_threshold


# print(filter_list([2, 34, 567, 23, 15, 65, 19, 21], 20))
#
#
#
""" 9.Калькулятор. Напишите функцию calculator, которая принимает два числа и строку, представляющую арифметическую
 операцию ('add', 'subtract', 'multiply', 'divide'), и возвращает результат этой операции. Продумайте типизацию. 
 Например calculator(4,5,"multiply") вернет 20."""


# def calculator(first_num: int, second_num: int, arithmetic_operation: str) -> float:

#     if arithmetic_operation == 'add':
#         return first_num + second_num
#     elif arithmetic_operation == 'subtract':
#         return first_num - second_num
#     elif arithmetic_operation == 'multiply':
#         return first_num * second_num
#     elif arithmetic_operation == 'divide':
#         if second_num == 0:
#             raise ZeroDivisionError("на ноль делить нельзя")
#         return first_num / second_num


# print(calculator(10, 4, 'divide'))
#
#
#
"""""""""""""""""""""""""""Лямбда-функции"""""""""""""""""""""""""'"""


""" 1.Применение функции ко всем элементам списка. Используя map и лямбда-функцию, напишите код, который принимает список 
целых чисел и возвращает список их квадратов."""

# list_integers = [1, 34, 3, 268, 43, 443, 3, 4, 8]
# list_squares_integers = list(map(lambda num: num**2, list_integers))

# print(list_squares_integers)
#
#
#
""" 2.Фильтрация нечетных чисел. Используя filter и лямбда-функцию, напишите код, который принимает список целых чисел и 
возвращает список только с нечетными числами."""

# list_integers = [1, 34, 3, 268, 43, 443, 3, 4, 8]
# list_odd_integers = list(filter(lambda num: num % 2, list_integers))

# print(list_odd_integers)
#
#
#
""" 3.Суммирование элементов списков. Используя zip и лямбда-функцию, напишите код, который принимает два списка одинаковой 
длины и возвращает список, где каждый элемент - это сумма элементов из входных списков на соответствующих позициях.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [5, 7, 9]"""

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list_element_sums = list(map(lambda num: num[0] + num[1], zip(list1, list2)))

# print(list_element_sums)
#
#
#
""" 4.Преобразование строк в числа. Используя map и лямбда-функцию, напишите код, который принимает список строковых 
представлений чисел и возвращает список этих чисел в виде целых чисел.
string_numbers = ["1", "2", "3", "4", "5"]
result = [1, 2, 3, 4, 5]"""

# string_numbers = ["1", "2", "3", "4", "5"]

# list_numbers = list(map(lambda x: int(x), string_numbers))

# print(list_numbers)
#
#
#
""" 5.Объединение списков словарей. Используя zip, напишите код, который принимает два списка словарей и возвращает 
список словарей, где каждый словарь - это объединение словарей из входных списков на соответствующих позициях.
list1 = [{'a': 1}, {'b': 2}]
list2 = [{'c': 3}, {'d': 4}]
result = [{'a': 1, 'c': 3}, {'b': 2, 'd': 4}]"""

# list1 = [{'a': 1}, {'b': 2}]
# list2 = [{'c': 3}, {'d': 4}]

# list_dictionaries = list({**list1, **list2}
#                          for list1, list2 in zip(list1, list2))

# print(list_dictionaries)
#
#
#
""" 6.Фильтрация строк по длине. Используя filter и лямбда-функцию, напишите код, который принимает список строк и 
возвращает только те строки, длина которых больше 3 символов."""


# list_str = ['asdf', 'dffggf', 'abc', 'dfffg']
# filter_numbers = list(filter(lambda x: len(x) > 3, list_str))
# print(filter_numbers)
#
#
#
""" 7.Вычисление длины строк Используя map и лямбда-функцию, напишите код, который принимает список строк и возвращает 
список их длин."""

# list_str = ['fgsv', 'dsgvd', 'vsds', 'dsvvdsvb']

# list_lens = list(map(lambda x: len(x), list_str))

# print(list_lens)
