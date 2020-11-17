# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('new_file_4.txt', 'w+', encoding='utf-8') as file:
    file.write(input('Введите ваши числа через пробел: '))
    file.seek(0)
    numbers_str = file.read()

print(sum([int(n) for n in numbers_str.split()]))
