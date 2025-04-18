"""1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Количество элементов первого и второго файлов:
Элементы последней трети:
Индекс максимального элемента последней трети:"""

import random

# Создание первого файла с положительными числами
with open('positive_numbers.txt', 'w') as pos_file:
    positive_numbers = [random.randint(1, 100) for _ in range(10)]  # 10 случайных положительных чисел
    pos_file.write(' '.join(map(str, positive_numbers)))

# Создание второго файла с отрицательными числами
with open('negative_numbers.txt', 'w') as neg_file:
    negative_numbers = [random.randint(-100, -1) for _ in range(10)]  # 10 случайных отрицательных чисел
    neg_file.write(' '.join(map(str, negative_numbers)))

# Чтение данных из файлов и обработка
with open('positive_numbers.txt', 'r') as pos_file, open('negative_numbers.txt', 'r') as neg_file:
    pos_numbers = list(map(int, pos_file.read().strip().split()))
    neg_numbers = list(map(int, neg_file.read().strip().split()))

# Формирование нового файла с результатами
with open('result.txt', 'w') as result_file:
    result_file.write("Элементы первого файла: " + ' '.join(map(str, pos_numbers)) + '\n')
    result_file.write("Элементы второго файла: " + ' '.join(map(str, neg_numbers)) + '\n')
    result_file.write("Количество элементов первого файла: " + str(len(pos_numbers)) + '\n')
    result_file.write("Количество элементов второго файла: " + str(len(neg_numbers)) + '\n')

    # Последняя треть элементов первого файла
    last_third_pos = pos_numbers[len(pos_numbers) * 2 // 3:]
    result_file.write("Элементы последней трети первого файла: " + ' '.join(map(str, last_third_pos)) + '\n')

    # Индекс максимального элемента последней трети
    if last_third_pos:
        max_index = pos_numbers.index(max(last_third_pos))
        result_file.write("Индекс максимального элемента последней трети: " + str(max_index) + '\n')
    else:
        result_file.write("Последняя треть первого файла пуста.\n")