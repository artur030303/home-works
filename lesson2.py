""" 
1.Пользователь задает переменную возраст. Если он старше 18, распечатайте,
    что все хорошо, если нет, то распечатайте, что не все хорошо.

2.Добавить к первому условию: если возраст больше 100, распечатать текст, что 
  пользователь вводит нас в заблуждение.

3.Добавить принты, является ли введенный возраст четным или нечетным.

4.Добавить, что пользователь вводит еще и имя. И если в имени есть буква 'a', 
  то написать, что мы даже не собираемся его проверять.

5.Проверить, если в имени есть буква 'v', большая или маленькая, без разницы. 
  И если возраст пользователя четный, то написать, что он выиграл приз, если нет,
  то не выиграл."""
#
#
# name = input("Enter your name: ")

# try:
#     age = int(input("Enter your age: "))

#     if 'a' in name:
#         print("Проверка отменена")

#     else:
#         if age > 18:
#             print("Все хорошо")
#         elif age > 100:
#             print("Вы нас вводите в заблуждение! ")
#         else:
#             print("Не все хорошо ")

#         if age % 2 == 0:
#             print("Ваш возраст четный")
#             print("Вы выйграли приз")
#         else:
#             print("Ваш возраст нечетный")
#             print("Вы не выйграли приз")

#     if 'v' in name.lower():
#         print("В вашем имени есть буква v")

# except ValueError:
#     print("Вы ввели не число")

""" 6.Спросить у пользователя возраст, пол и имя. Для всех младше 15 мы пишем, 
что рекомендуем теннис, для мальчиков старше 15 рекомендуем футбол, для 
девочек - баскетбол, но если в имени есть буква 'с' или 'т', пишем, что не 
рекомендуем заниматься спортом."""
#
#
# try:
#     age = int(input("Введите свой возраст: "))
# except ValueError:
#     print("Вы должны вводить числа для возраста")
# else:
#     try:
#         gender = input(
#             "Введите ваш пол('мальчик' или 'девочка'): ").strip().lower()
#         if gender != 'мальчик' and gender != 'девочка':
#             raise ValueError(
#                 "Неправильный пол. Пожалуйста, введите только 'мальчик' или 'девочка'.")
#         name = input("Введите ваше имя: ")

#         if 'с' in name or 'т' in name:
#             print("Не рекомендуем заниматься спортом")
#         else:
#             if age < 15:
#                 print("Мы вам рекомендуем тенис")
#             elif age >= 15:
#                 if gender == 'мальчик':
#                     print("Мы вам рекомендуем футбол")
#                 elif gender == 'девочка':
#                     print("Мы вам рекомендуем баскетбол")

#     except ValueError as e:
#         print(e)