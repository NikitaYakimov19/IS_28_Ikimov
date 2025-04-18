"""2. Из предложенного текстового файла (text18-32.txt) вывести на экран его содержимое,
количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно вставив после каждой
строки строку из символов «*»."""

import string

# Чтение содержимого файла с указанием кодировки
with open('text18-32.txt', 'r', encoding='utf-16') as file:
    lines = file.readlines()

# Вывод содержимого на экран
print("Содержимое файла:")
for line in lines:
    print(line, end='')

# Подсчет знаков пунктуации в первых четырех строках
punctuation_count = sum(1 for line in lines[:4] for char in line if char in string.punctuation)
print(f"\nКоличество знаков пунктуации в первых четырех строках: {punctuation_count}")

# Создание нового файла с текстом в стихотворной форме
with open('poetic_text.txt', 'w', encoding='utf-8') as poetic_file:
    for line in lines:
        poetic_file.write(line.strip() + '\n')  # Записываем строку
        poetic_file.write('*' * len(line.strip()) + '\n')  # Записываем строку из символов '*'