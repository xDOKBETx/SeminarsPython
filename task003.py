# 3. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

a = float(input("Введите дробное число: "))
if a % 1 != 0:
    b = a * 10
    print(int(b % 10))
else:
    print("Нет")