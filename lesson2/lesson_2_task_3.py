# Вычисление площади квадрата по одной стороне
def square(sq):
    if (sq > 0):
        return True
    else:
        return False
sq = int(input("Введите длинну стороны квадрата: "))
size = sq * sq
print(f"Площадь квадрата со стороной {sq} = {size}")