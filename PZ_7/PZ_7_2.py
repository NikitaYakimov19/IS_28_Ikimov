"""Дана строка-предложение. Зашифровать ее, поместив вначале все символы,
расположенные на четных позициях строки, а затем, в обратном порядке, все
символы, расположенные на нечетных позициях (например, строка «Программа»
превратится в «ргамамроП»)."""
sent = list(input("Введите строку/предложение: "))
even_char = ""
odd_char = ""
for index in range(len(sent)):
    if index % 2 == 0:
        even_char += sent[index]
    else:
        odd_char += sent[index]
print(odd_char + even_char[::-1])
