# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input("Введите координату точки по оси Х, (X ≠ 0): "))
y = int(input("Введите координату точки по оси Y, (Y ≠ 0): "))
quarter = 0
if x > 0 and y > 0:
    quarter = 1
    print(f"Точка лежит в {quarter} четверти координатной плоскости")
elif x < 0 and y > 0:
    quarter = 2
    print(f"Точка лежит в {quarter} четверти координатной плоскости")
elif x > 0 and y < 0:
    quarter = 3
    print(f"Точка лежит в {quarter} четверти координатной плоскости")
elif x < 0 and y < 0:
    quarter = 4
    print(f"Точка лежит в {quarter} четверти координатной плоскости")
else:
    print ("Точка находится на одной из осей")
