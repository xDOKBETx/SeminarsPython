# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

def numberArray():
    listNumber = []
    for _ in range(5):
        number = int(input("Введите число: "))
        listNumber.append(number)
    maxNumber = listNumber[0]
    for num in listNumber:
        if num > maxNumber:
            maxNumber = num
    return maxNumber

print(numberArray())
