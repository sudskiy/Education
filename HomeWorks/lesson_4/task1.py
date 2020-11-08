# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import  argv

_, hours, money_per_hour, bonus = argv

def paycheck(hours, money_per_hour, bonus):
    return hours * money_per_hour + bonus

print(paycheck(hours, money_per_hour, bonus))
