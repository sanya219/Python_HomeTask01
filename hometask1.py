import math
# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение
print("Задача 1")
days = {1: "понедельник", 
        2: "вторник", 
        3: "среда",
        4: "четверг",
        5: "пятница",
        6: "суббота",
        7: "воскресенье"}
day = int(input("Введите номер дня недели: "))
if day > 7 or day < 1:
    print("Такого дня не существует!")
else:
    print(days[day])

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
print("\nЗадача 2")
print("Введите координаты точки A:")
xA = int(input("x = "))
yA = int(input("y = "))
print("Введите координаты точки B:")
xB = int(input("x = "))
yB = int(input("y = "))
print(f"Расстояние между точками A({xA},{yA}) и B({xB},{yB}) равно {round(math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2), 2)}")

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0
print("\nЗадача 3")
quarters = {
    1: "x > 0, y > 0",
    2: "x > 0, y < 0",
    3: "x < 0, y < 0",
    4: "x < 0, y > 0"}
quarter = int(input("Введите номер четверти:"))
if quarter < 1 or quarter > 4:
    print("Неверный номер четверти")
else:
    print(quarters[quarter])
