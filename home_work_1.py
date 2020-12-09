user_name = input("Добро пожаловать! Для заполнения анкеты, пожалуйста, введите ваше имя:\n>>>")
welcome_msg = f'Спасибо, {user_name}, нам также потребуются еще некоторые ваши данные'
print(welcome_msg)

user_surname = input("Введите вашу фамилию:\n>>>")

user_birth_year = input("Ваш год рождения:\n>>>")

user_city = input("Введите город вашего проживания:\n>>>")

sys_message = f'Новый пользователь: {user_surname} {user_name}\nГод рождения: {user_birth_year}\nГород: {user_city}'

print(sys_message)
