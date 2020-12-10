number = input("Введите число\n>")

if number.isdigit():
    number = int(number)
else:
    print("Ошибка ввода. Вы ввели не число")
    exit()

max_symbol = 0

while number > 0:
    a = number % 10
    if a > max_symbol:
        max_symbol = a
    number = (number - a) / 10

max_symbol = int(max_symbol)

print(f'Самая большая цифра в введеном вами числе - {max_symbol}')
