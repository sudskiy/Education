#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
a = int(input("Введите число: "))
a1 = 0
while True:
    b = a % 10
    a = a // 10
    if a1 == 0:
        a1 = b
    if a1 <= a % 10:
        a1 = a % 10
    if a == 0:
        break
print("Наибольшее число: ", a1)
