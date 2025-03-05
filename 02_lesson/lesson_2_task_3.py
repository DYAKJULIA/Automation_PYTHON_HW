
x = float(input("Веедите сторону квадрата: "))

import math

def square(side):

    if side > 0:
        return math.ceil(side ** 2)

    else:
        return 0

print(f"Площадь квадрата со сторонйой {x} = {square(x)}")