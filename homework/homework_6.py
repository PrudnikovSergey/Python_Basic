"""
Lesson 4. Task 6.

Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import count, cycle

# (a)
print('Использование функции count (подпункт "а" в задании):')
for el in count(3):
    if el > 10:
        break
    else:
        print(el)



# (b)

print('\n\n\nИспользование функции cycle (подпункт "б" в задании):')
s_list = [1, 2, 4, 5]
n = 0
for x in cycle(s_list):
    if n > 15:
        break
    print(x)
    n += 1