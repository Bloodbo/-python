def is_prime():
    n=int(input('введите простое число = '))
    if n < 2:
        print('False')
    if n == 2:
        print('True')
    if n%2 == 0:
        print('False')
    i = 3
    while i * i <= n:
        if n % i == 0:
            print('False')
        i += 2
    print('True')
is_prime()

# Если число меньше 2, то оно не может быть простым