# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

result = []
with open("new_file_1.txt", 'r', encoding='UTF-8') as file:
    for el in file:
        result.append(len(el.split(' ')))

print(f'Всего строк в файле: {len(result)}')
for i, itm in enumerate(result, 1):
    print(f'В строке {i} содержится {itm} слов')
