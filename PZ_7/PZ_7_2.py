"""Дана строка-предложение. Зашифровать ее, поместив вначале все символы,
расположенные на четных позициях строки, а затем, в обратном порядке, все
символы, расположенные на нечетных позициях (например, строка «Программа»
превратится в «ргамамроП»)."""
sent = input("Введите строку/предложение: ")
print("Исходная строка/предложение ", sent)
sent2 = list(sent)
even_char = ""
odd_char = ""
for index in range(len(sent2)):
    if index % 2 == 0:
        even_char += sent2[index]
    else:
        odd_char += sent2[index]
print(odd_char + even_char[::-1])
