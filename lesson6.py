""" 1.Создать два множества в которых есть общие элементы. Найти, какие элементы 
есть в обоих множествах, какие есть только в первом, какие только во втором. 
Найти множество в котором будут элементы из обоих множеств"""

# set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# set_two = {11, 12, 13, 14, 15, 16, 3, 5, 16, 9}

# print(set_one & set_two)
# print(set_one - set_two)
# print(set_one | set_two)

""" 2.Создать список с повторениями, удалить повторения"""

# my_set = {1, 34, 3, 6778, 45, 123, 0, 66, 446, 7, 3, 3, 0, 5, 567, 4, 4}
# set_without_duplicates = list(set(my_set))
# print(set_without_duplicates)

""" 3.Создать два списка. Написать код, который будет печатать True, если в 
списках есть общие элементы и False если нет"""

# set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# set_2 = {11, 12, 13, 14, 15, 16, 3, 5, 16, 9}
# if set_1 & set_2:
#     print(True)
# else:
#     print(False)

""" 1.Перевернуть словарь (было {1:2, 3:4} стало {2:1, 4:3}). После этого сделать
 это же через компрешеншен"""

# my_dict = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }
# rev = {}
# for key, val in my_dict.items():
#     rev[val] = key

# print(rev)

# new_d = {val: key for key, val in my_dict.items()}
# print(new_d)


""" 2.Есть два списка одинаковой длинны, создать словарь, где ключи из это элементы 
первого списка, а значения элементы второго. Например [1,2,3], [4,5,6], 
результат {1:4, 2:5, 3:6}"""

# list_one = [1, 2, 3]
# list_two = [4, 5, 6]

# result = {i: list_two[i] for i in range(len(list_one))}

# print(result)
#
#
#
""" 3.Есть строка с предложением, в котором есть повторяющиеся слова. Создать список(ты наверное хотел написать словарь), 
где ключи это слова из этого предложения, а значение, это кол-во раз которое встречается 
это слово, пример: "привет я хочу привет я", результат {"привет": 2, "я": 2, "хочу": 1}"""

# my_str = "привет я хочу привет я"
# splitted_str = my_str.split()

# result = {word: splitted_str.count(word) for word in set(splitted_str)}

# print(result)

# BANKNOTES = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
# MAX_AMOUNT = 10
# amount = int(input("Please input number "))
# result = dict.fromkeys(BANKNOTES, 0)

# for i in range(1, len(BANKNOTES)+1):
#     cutted_banknotes = BANKNOTES[:i]
#     if sum(cutted_banknotes) * MAX_AMOUNT >= amount:
#         user_banknotes = cutted_banknotes
#         break
# while amount:
#     amount -= user_banknotes[-1]
#     result[user_banknotes[-1]] += 1
#     if amount <= sum(user_banknotes[:-1]) * MAX_AMOUNT:
#         user_banknotes = user_banknotes[:-1]

# print(result)
