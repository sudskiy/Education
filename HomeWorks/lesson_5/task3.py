# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('new_file_2.txt', 'r', encoding='utf-8') as file:
    employees = dict(map(lambda x: x.split(), [line for line in file]))

    low_salary = ', '.join([el[0] for el in employees.items() if int(el[1]) < 20000])
    print(f'Работники с з/п меньше  20000 : {low_salary}')

    salaries = [int(el[1]) for el in employees.items()]
    average_salary = sum(salaries) // len(salaries)
    print(f'Средняя заработная плата: {average_salary}')
