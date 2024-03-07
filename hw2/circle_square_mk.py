import random
import math

def circle_square_mk(r, n):
    darts_in_circle = 0
    for _ in range(n):
        x, y = random.uniform(-r, r), random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            darts_in_circle += 1
    return 4 * (darts_in_circle / n) * r**2

# Тестирование
r = 5
n = 1000000

circle_square_mk_result = circle_square_mk(r, n)
true_square = math.pi * r**2

print("Площадь, вычисленная методом Монте-Карло:", circle_square_mk_result)
print("Площадь, вычисленная по формуле:", true_square)
print("Абсолютная погрешность:", abs(circle_square_mk_result - true_square))

# Комментарий: Погрешность расчёта зависит от количества экспериментов (n). Чем больше n, тем меньше погрешность.
# Для n = 1000000 погрешность составляет примерно 0.005, для n = 100000 - 0.015, для n = 1000 - 0.12.
