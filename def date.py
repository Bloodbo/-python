def date():
    a = int(input('введите номер дня в календаре = '))
    b = int(input('введите номер месяца в календаре = '))
    c = int(input('введите год в календаре = '))
    if a == 31 or 1 <= a <= 30:
        print('True')
    if b == 12 or 1 <= a <= 11:
        print('True')
    if c>0:
        print('True')
    if  a>31:
        print('Error')
    if b>12:
        print('Error')
date()
