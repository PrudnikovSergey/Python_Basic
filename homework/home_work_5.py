proceeds = input("Введите значение выручки фирмы за период (в рублях):\n>")
if proceeds.isdigit():
    proceeds = int(proceeds)
else:
    print("Ошибка ввода. Вы ввели не числовое значение")
    exit()

costs = input("Введите значение издержек фирмы за период (в рублях):\n>")
if costs.isdigit():
    costs = int(costs)
else:
    print("Ошибка ввода. Вы ввели не числовое значение")
    exit()

profit = proceeds - costs

if profit > 0:
    employees = input("Введите среднесписочную численность сотрудников фирмы за период:\n>")
    if employees.isdigit():
        employees = int(employees)
    else:
        print("Ошибка ввода. Вы ввели не числовое значение")
        exit()

    profit_per_men = profit / employees
    profit_per_men = float(profit_per_men)
    print(f'Предприятие отработало отчетный период с прибылью {profit} рублей')
    print(f'Средняя прибыль на одного сотрудника составила {profit_per_men:.2f} рублей')

elif profit == 0:
    print("Предприятие отработало отчетный период в 0. Выручка полностью перекрыла издержки, прибыли не получено")
else:
    print(f'Предприятие отработало отчетный период в убыток {0 - profit} рублей.\nНеобходимо улучшать показатели.')
