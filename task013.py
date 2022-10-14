# 13. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def negafibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for _ in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


negafibonacci_list = [0]
user_number_k = int(input('Введите любое число: '))
for e in range(1, user_number_k + 1):
    negafibonacci_list.append(fibonacci(e))
    negafibonacci_list.insert(0, negafibonacci(e))
print(negafibonacci_list)

####################################################################################################################

number_k = int(input('Введите размер списка Фибоначчи: '))
if number_k < 0:
    number_k = number_k * -1
n1 = n2 = 1
nega_fibonachi_list = [n1, n2]
for i in range(2, number_k):
    n1, n2 = n2, n1 + n2
    nega_fibonachi_list.append(n2)

n1 = n2 = 1
for i in range(-number_k, 1):
    n1, n2 = n2, n1 - n2
    nega_fibonachi_list.insert(0, n2)
print(nega_fibonachi_list)

#####################################################################################################################
