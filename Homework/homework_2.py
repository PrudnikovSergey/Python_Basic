"""
Урок 2. Задание 2.

Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input().

"""

start_list = input("Введите элементы списка через пробел:\n>>>").split()
print(f'Исходный список: {start_list}')

if len(start_list) % 2 == 1:
    last_element = start_list[len(start_list) - 1]
    start_list.remove(start_list[-1])
    i = 0
    new_list = []
    while i < (len(start_list)):
        tmp1 = start_list[i]
        tmp2 = start_list[i + 1]
        new_list.append(tmp2)
        new_list.append(tmp1)
        i += 2
    new_list.append(last_element)
    print(f'Новый список: {new_list}')
else:
    i = 0
    new_list = []
    while i < (len(start_list)):
        tmp1 = start_list[i]
        tmp2 = start_list[i + 1]
        new_list.append(tmp2)
        new_list.append(tmp1)
        i += 2
    print(f'Новый список: {new_list}')
