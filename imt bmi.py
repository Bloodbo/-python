a = int(input('введите ваш вес = '))
b = float(input('введите ваш рост = '))

def bmi():
    c=0
    c=b**2

    bmi=0
    bmi=a//c
    if bmi<=18:
        print('недостаточный вес',bmi)

    if bmi<=25:
        print('нормальный',bmi)

    if bmi<=30:
        print('избыточный вес', bmi)

    if bmi>30:
        print('ожирение!', bmi)

bmi()
#comments  ваш фактический вес делим на ваш рост (в метрах) в квадрате