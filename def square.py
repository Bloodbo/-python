from math import *
def square():
    a = int(input('введите сторону квадрата =  '))
    S = a**2
    print('площадь данного квадрата равна = ', S)
    D = a*sqrt(2)
    print('диагональ квадрата = ', D)
    P = 4 * a
    print('периметр квадрата = ', P)

square()