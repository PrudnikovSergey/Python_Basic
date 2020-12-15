"""
Урок 2. Задание 3.

Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict
"""
while True:
    user_num = input('Введите номер месяца (число от 1 до 12):\n>')
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num < 1 or user_num > 12:
            print('Ваше число не соответствует диапазону от 1 до 12')
        else:
            break
    else:
        print('Ошибка ввода, это не число')


#  решение с использованием List
season_list = ['зима', 'весна', 'лето', 'осень']


if user_num == 3 or user_num == 4 or user_num == 5:
    print(season_list[1])
elif user_num == 6 or user_num == 7 or user_num == 8:
    print(season_list[2])
elif user_num == 9 or user_num == 10 or user_num == 11:
    print(season_list[3])
else:
    print(season_list[0])




#  через Словарь

year_dict = dict(
    зима=(12, 1, 2),
    весна=(3, 4, 5),
    лето=(6, 7, 8),
    осень=(9, 10, 11)
)

if user_num in year_dict.get("весна"):
    print("весна")
elif user_num in year_dict.get("лето"):
    print("лето")
elif user_num in year_dict.get("осень"):
    print("осень")
else:
    print("зима")