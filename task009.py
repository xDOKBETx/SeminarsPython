# 9. Задайте список из n чисел последовательности (1 + 1/n)*n и выведите на экран их сумму.

def sequence(n):
    return (1 + 1 / n) ** n


def feel_list(n):
    list = []
    for i in range(1, n + 1):
        list.append(sequence(i))
    return list


def main():
    n = int(input("Enter the number n: "))
    list_sequence = feel_list(n)
    print(list_sequence)
    print("Summary of the sequence: ", "%.2f" % sum(list_sequence))


if __name__ == "__main__":
    main()
