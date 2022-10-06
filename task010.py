# 10. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

path = "file.txt"


def fill_list(n):
    list = []
    for _ in range(0, n):
        list.append(random.randint(-n, n))
    return list


# по хорошему здесь нужно добавить на вход длину списку и чекать его при добавлении индекса из файла в новый список
def read_file(len_list):
    file = open(path, "r")
    list = []
    for line in file:
        # добавляю условие проверки индекса с длиной списка элементов
        if 0 <= int(line) < len_list:
            list.append(int(line))
    file.close()
    return list


def multi_on_pos(list, pos):
    result = 1
    for i in range(0, len(pos)):  # здесь проходили по списку элементов - было len(list), надо по списку позиций
        # значение не по i, а по pos[i]
        result *= list[pos[i]]  # берем значение из list по позиции из pos, список которых получили из файла
        # если просто так делать без проверок длины списка элементов, получаем IndexError: list index out of range
        # поэтому можно проверку длины добавить в момент заполнения в ф-цию read_file
        # или вообще по другому записать цикл, типа:
    # for pos_item in pos:
    #     result*=list[pos_item]
    return result


def main():
    n = int(input("Enter N: "))
    list = fill_list(n)
    print(list)
    positions = read_file(len(list))
    print(positions)
    print("Произведение элементов на указанных позициях: ", multi_on_pos(list, positions))


if __name__ == "__main__":
    main()
