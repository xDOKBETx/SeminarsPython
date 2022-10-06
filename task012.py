# 12. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
#  - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#  - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#  - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#  - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#  - список: [], ищем: "123", ответ: -1

list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
search = input("Enter string: ")


def find_second(list1, search):
    result = -1
    count = 0
    for i in range(len(list1)):
        if list1[i] == search:
            count += 1
            if count == 2:
                result = i
    return result


print(find_second(list1, search))
