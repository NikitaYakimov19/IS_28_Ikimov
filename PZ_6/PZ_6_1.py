""" Дан список размера N. Поменять местами его минимальный и максимальный
элементы. """

try:
    user_input = input("Введите список чисел, разделенных запятыми: ")

    # Проверка на наличие запятых
    if ',' not in user_input:
        print("Ошибка: Введите числа, разделенные запятыми.")
    else:
        user_input = user_input.split(',')
        user_input = [int(num.strip()) for num in user_input]  # Преобразуем каждое число в целое

        # Находим индекс максимального числа
        max_index = user_input.index(max(user_input))

        # Находим индекс минимального числа
        min_index = user_input.index(min(user_input))

        # Сохраняем значения максимального и минимального чисел
        max_value = user_input[max_index]
        min_value = user_input[min_index]

        # Меняем местами максимальное и минимальное числа
        user_input[max_index] = min_value
        user_input[min_index] = max_value

        print("Поменяв местами максимальный и минимальный элемент списка получилось: ", user_input)

except ValueError:
    print("Ошибка: Убедитесь, что вы ввели корректные целые числа.")
except Exception as e:
    print("Произошла ошибка:", e)
