"""Описать функцию SortDec3(A, B, C), меняющую содержимое переменных A, B, C
таким образом, чтобы их значения оказались упорядоченными по убыванию (A, B,
C — вещественные параметры, являющиеся одновременно входными и
выходными). С помощью этой функции упорядочить по убыванию два данных
набора из трех чисел: (A1, B1, C1) и (A2, B2, C2)."""


def SortDec(A, B, C):
    if A >= B and A >= C:
        max_num = A
        if B >= C:
            mid_num = B
            min_num = C
        else:
            mid_num = C
            min_num = B
    elif B >= A and B >= C:
        max_num = B
        if num1 >= num3:
            mid_num = num1
            min_num = num3
        else:
            mid_num = num3
            min_num = num1
    else:
        max_num = num3
        if num1 >= num2:
            mid_num = num1
            min_num = num2
        else:
            mid_num = num2
            min_num = num1

    return max_num, mid_num, min_num


# Пример наборов чисел
first_number1, first_number2, first_number3 = 5.2, 3.8, 4.1
second_number1, second_number2, second_number3 = 2.5, 3.6, 1.9

# Сортируем первый набор чисел
first_number1, first_number2, first_number3 = sort_numbers_descending(first_number1, first_number2, first_number3)
print(
    f"Первый набор отсортирован: first_number1 = {first_number1}, first_number2 = {first_number2}, first_number3 = {first_number3}")

# Сортируем второй набор чисел
second_number1, second_number2, second_number3 = sort_numbers_descending(second_number1, second_number2, second_number3)
print(
    f"Второй набор отсортирован: second_number1 = {second_number1}, second_number2 = {second_number2}, second_number3 = {second_number3}")
