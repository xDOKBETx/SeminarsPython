# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:*
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input("Введите число N: "))

for i in range(-n, n): 
    print(i, end=',') # выведет через разделитель "," числа от -n до n - 1
print(n) # выведет последнее число n
