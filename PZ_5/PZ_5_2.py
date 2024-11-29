"""Описать функцию SortDec3(A, B, C), меняющую содержимое переменных A, B, C
таким образом, чтобы их значения оказались упорядоченными по убыванию (A, B,
C — вещественные параметры, являющиеся одновременно входными и
выходными). С помощью этой функции упорядочить по убыванию два данных
набора из трех чисел: (A1, B1, C1) и (A2, B2, C2)."""

input
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
        if B >= C:
            mid_num = A
            min_num = C
        else:
            mid_num = C
            min_num = A
    else:
        max_num = C
        if A >= B:
            mid_num = A
            min_num = B
        else:
            mid_num = B
            min_num = A

    return max_num, mid_num, min_num

# Сортируем первый набор чисел
print("Первый набор отсортирован:", first_number1 = first_number1, first_number2 = first_number2, first_number3 = first_number3")

# Сортируем второй набор чисел
second_number1, second_number2, second_number3 = sort_numbers_descending(second_number1, second_number2, second_number3)
print(
    f"Второй набор отсортирован: second_number1 = {second_number1}, second_number2 = {second_number2}, second_number3 = {second_number3}")
