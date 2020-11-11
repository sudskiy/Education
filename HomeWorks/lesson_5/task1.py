# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('new_file_1.txt', 'a', encoding='utf-8') as file:
    while True:
        user_str = input('Введите строку для записи. Для завершения просто нажмите Enter: ')
        if len(user_str) != 0:
            file.write(user_str + '\n')
        else:
            print("Данные записаны в файл: new_file_1.txt ")
            break
