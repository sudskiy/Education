# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

slovar = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}

with open('new_file_3.txt', 'r', encoding='utf-8') as start:
    with open('new_new_file_3.txt', 'a', encoding='utf-8') as finish:
        for el in start:
            word = el[:el.index(' ')]
            string = el.replace(word, slovar[word])
            finish.write(string)
