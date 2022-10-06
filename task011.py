# 11. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def search_number(list_of_elements, number_on_the_list):
    global f
    for i in range(len(list_of_elements)):
        if number_on_the_list in list_of_elements[i]:
            f = 1
            break


try:
    number_in_the_list = int(input("Введите число: "))
except:
    print('Вводите числа!')
    exit()

f = 0
list1 = ['asd', 'qwwe', 'ddfgg', 'eeee', 'werwer3wewe34343w', '4', '233', 'wew']
search_number(list1, str(number_in_the_list))
if f == 1:
    print("есть")
else:
    print("нет")
