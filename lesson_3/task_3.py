# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif b >= a and c >= a:
        return b + c
    elif a >= b and c >= b:
        return a + c

