def bank():
    a = int(input('введите кол-во рублей = '))
    if a == 0 or a < 1000:
        print('наш вклад начинается от 1000')

    years = int(input('введите на сколько лет/год хотите оформить вклад = '))

    if years<3:
        print('так нельзя!')

    if years==3 or years>3:
        stavka = int(input('введите ставку = '))
        if stavka == 2 or stavka<2:
            print('так нельзя!')
        if stavka>2:
            for i in range(years):
                a = int(a + stavka * a / 100)
                print("По итогу вы получаете рублей = ", a)


bank()
#comments функция которая считает вклад, выводит результат по годам