#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
a = int(input("Введите количество секунд: "))
hours = a // 3600
if hours < 10:
    hours = "0" + str(hours)
minutes = a % 3600 // 60
seconds = a % 3600 % 60
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)
print(f"Получившееся время - {hours}:{minutes}:{seconds}")
