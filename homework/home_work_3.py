user_number = input("Введите число\n>")

if user_number.isdigit():
    double = user_number + user_number
    triple = user_number + user_number + user_number
    user_number = int(user_number)
    double = int(double)
    triple = int(triple)
else:
    print("Ошибка ввода. Вы ввели не число")
    exit()

print("Программа запрашивает у пользователя число (n). Результат выполнения программы - вычисление n + nn + nnn")

result = user_number + double + triple
message = f'Результат выполнения программы: {user_number} + {double} + {triple} = {result}'

print(message)
