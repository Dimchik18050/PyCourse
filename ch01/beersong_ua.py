word = "пляшок"

for beer_num in range(99, 0, -1):
    print(beer_num, word, "пива на стіні.")
    print(beer_num, word, "пива.")
    print("Візьми одну.")
    print("Пусти по колу.")
    if beer_num == 1:
        print("Не має більше пляшок пива на стіні.")
    else:
        new_num = beer_num - 1
        if new_num >= 11 and new_num <= 19:
            word = "пляшок"
        else:
            if new_num % 10 == 1:
                word = "пляшка"
            elif new_num % 10 in [2, 3, 4]:
                word = "пляшки"
            else:
                word = "пляшок"
        print(new_num, word, "пива на стіні.")
    print()
