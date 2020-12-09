user_number = input("Введите любое число, которое будет обозначать количество секунд, необходимых к переводу "
                    "в часы и минуты\n>>>")

while user_number.isdigit() == "false":
    user_number = input("Ошибка ввода! Введите число:\n>>>")
else:
    user_number = int(user_number)


minutes_total = user_number // 60 # вычисляю целое количество минут
seconds = user_number % 60 # вычисляю остаток в секундах, который пойдёт в итоговый результат
hours = minutes_total // 60 # вычисляю целое количество часов
minutes = minutes_total % 60 # вычисляю остаток в минутах, который пойдёт в итоговый результат

result = f'Результат перевода числа секунд в формат (ЧЧ:ММ:СС): {hours}:{minutes}:{seconds}'
print(result)
