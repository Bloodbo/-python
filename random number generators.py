count=int(input('введите число:'))
import random
number = random.randint(10,50)
while count!=number:
    count=int(input('введите число ещё раз: '))
    if count > number:
        print('Число должно быть меньше')
    elif count < number:
        print('Число должно быть больше')
    else:
        print('Вы угадали число!!!')
