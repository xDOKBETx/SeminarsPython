# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    if num1 * num1 == num2:
        print("Второе число является квадратом первого")
    elif num2 * num2 == num1:
        print("Первое число является квадратом второго")
    else:
        print("Квадраты отсутствуют")
except:
    print("Надо вводить целые числа!")


#####################################################################################################################

def seek_squares(num1, num2):
    if num1 * num1 == num2:
        print("Второе число является квадратом  первого")
    elif num2 * num2 == num1:
        print("Первое число является квадратом второго")
    else:
        print("Квадраты отсутствуют")


try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    seek_squares(a, b)
except:
    print("Надо вводить целые числа!")
