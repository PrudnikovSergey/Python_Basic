"""
Lesson 5. Task 4.

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dict_numbers = {
    'rus': ('один', 'два', 'три', 'четыре'),
    'eng': ('one', 'two', 'three', 'four'),
    'num': ('1', '2', '3', '4')
}

my_f = open("data5_4.txt", 'r', encoding='UTF-8')
my_f_result = open("result5_4.txt" , 'x', encoding='UTF-8')

for line in my_f:
    number = line.split()[2]
    pos = dict_numbers.get('num').index(number)
    rus_word = dict_numbers.get('rus')[pos]
    result = f'{rus_word} - {number}'
    print(result)
    my_f_result.write(result + '\n')
    
my_f.close()
my_f_result.close()
print('Данные внесены в новый файл result5_4.txt')