spisok = input("Пожалуйста, введите последовательность чисел через пробел: ")
spisok_list = [int(a) for a in spisok.split()]
user_num = int(input("Пожалуйста, введите любое число: "))

if user_num % 1 == 0:
    spisok_list.append(user_num)
    print("Список до сортировки:", spisok_list)

def my_sort(spisok_list):
    for i in range(len(spisok_list)):
        i_min = i
        for j in range(i, len(spisok_list)):
            if spisok_list[j] < spisok_list[i_min]:
                i_min = j
        if i != i_min:
            spisok_list[i], spisok_list[i_min] = spisok_list[i_min], spisok_list[i]
    return spisok_list

print("Список после сортировки:", my_sort(spisok_list))