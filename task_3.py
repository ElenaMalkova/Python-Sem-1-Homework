# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("Введите значение Х: "))
y = int(input("Введите значение Y: "))
z = int(input("Введите значение Z: "))

left = not (x or y or z)
right = not x and not y and not z

if left == right:
    print("True")
else:
    print("False")

