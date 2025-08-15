def convert_kg_to_g(kilograms):
    return kilograms * 1000
def convert_g_to_kg(grams):
    return grams / 1000
def convert_tons_to_kg(tons):
    return tons * 1000
def convert_kg_to_tons(kilograms):
    return kilograms / 1000
def get_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    print('Введите цифру')
    print('1 - из кг в г')
    print('2 - из г в кг')
    print('3 - из тонн в кг')
    print('4 - из кг в тонны')

    choice = int(input())

    if choice == 1:
        kilograms = get_user_input('Введите кол-во кг, которые необходимо перевести в г =  ')
        grams = convert_kg_to_g(kilograms)
        print(f"{kilograms} кг = {grams} г")

    elif choice == 2:
        grams = get_user_input('Введите кол-во г, которые необходимо перевести в кг =  ')
        kilograms = convert_g_to_kg(grams)
        print(f"{grams} г = {kilograms} кг")

    elif choice == 3:
        tons = get_user_input('Введите кол-во тонн, которые необходимо перевести в кг')
        kilograms = convert_tons_to_kg(tons)
        print(f"{tons} тонн = {kilograms} кг")

    elif choice == 4:
        kilograms = get_user_input('Введите кол-во кг, которые необходимо перевести в тонны =  ')
        tons = convert_kg_to_tons(kilograms)
        print(f"{kilograms} кг = {tons} тонн")

    else:
        print("Некорректный выбор. Пожалуйста, введите число от 1 до 4.")
        main()

if __name__ == "__main__":
    main()