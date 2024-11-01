'''Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
целые степени числа A от 1 до N.'''
def calculate(A, N):
    if N <= 0:
        raise ValueError("Параметр N должен быть больше 0.")

    for i in range(1, N + 1):
        power = A ** i
        print(A, "^", i, " = ", power)


try:
    # Пример значений A и N
    A = float(input("Введите вещественное число A: "))
    N = int(input("Введите целое число N (>0): "))

    calculate(A, N)

except ValueError:
    print("Ошибка.")
