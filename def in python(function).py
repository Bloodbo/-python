#comments def имя_функции(параметры):
    #определениие_функции
k=float(input('k='))
y=float(input('y='))
z=float(input('z='))
x=float(input('x='))
def f(x):
    return x*2+3
print('результат после функции =', f(x))
def f(k, y, z):
    return k+y+z/3
print('результат второй функции (она ищет ср арифметическое) = ', f(k, y, z))