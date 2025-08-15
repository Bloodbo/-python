def season():
    a = int(input('введите номер месяца и получите название сезона: '))
    if a == 12 or 1 <= a <= 2:

        print("Зима")

    elif 3 <= a <= 5:

        print("Весна")

    elif 6 <= a <= 8:

        print("Лето")

    elif 9 <= a <= 11:

        print("Осень")

    else:

        print("Неверно введён номер месяца!")


season()