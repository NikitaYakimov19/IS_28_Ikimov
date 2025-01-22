"""Дан словарь на 6 персон, найти и вывести их средний возраст. (Пример,
{"Андрей": 32, "Виктор": 29, "Максим": 18, …}, среднее 26,33)."""
diction = {}
inf = input("Введите имя и возраст человека(до 6 персон): ")
data = inf.split()
max_persons = min(6, len(data) // 2)
are_age = data[1:6:2]
for index in range(max_persons):
    name = data[index * 2]
    age = int(data[index * 2 + 1])
    diction[name] = age
if diction:  # Проверяем, что словарь не пуст
    average_age = sum(diction.values()) / len(diction)  # Вычисляем средний возраст
else:
    average_age = 0

print("Средний возраст: ", average_age)
