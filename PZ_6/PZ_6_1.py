""" Дан список размера N. Поменять местами его минимальный и максимальный
элементы. """

user_input = input("Введите список чисел, разделенных запятыми: ")
user_input = user_input.split(',')
user_input = [int(num) for num in user_input]  # Преобразуем каждое число в целое

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

# Выводим измененный список как строку без скобок и запятых
result = ', '.join(map(str, user_input))
print(result)

