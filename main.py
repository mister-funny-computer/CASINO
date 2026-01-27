import random

score = 100
number1 = random.randint(1,6)
number2 = random.randint(1,6)

print("Если сумма выпавших цифр меньше 7 и играющий задумал число меньшее 7, он выигрывает сделанную ставку. Если сумма выпавших цифр больше 7 и играющий задумал число большее 7, он также выигрывает сделанную ставку. Если играющий угадал сумму цифр, он получает в четыре раза больше очков, чем сделанная ставка. Ставка проиграна, если не имеет место ни одна из описанных ситуаций. При израсходовании всех очко игра заканчивается, после каждой попытки предлагается закончить игру.")
while score > 0:
    no_or_yes = input("Вы хотите продолжить?: ")
    if no_or_yes == "нет":
        break
    print(f"У вас {score} очков ")
    user_number = int(input("Введите сумму от 2 до 12: "))
    bet = int(input(f"Выберете ставку 1 до {score}: "))


    print(f"Бросаем кубики.Выпадает число {number1} и {number2}.")

    if number1 + number2 < 6 and user_number < 6:
        print("ВЫ ВЫИГРАЛИ СТАВКУ!!!!")
        score = score + bet
        print(f"Вот ваши очки {score}")
    elif number1 + number2 > 6 and user_number > 6:
        print("ВЫ ВЫИГРАЛИ СТАВКУ!!!!")
        score = score + bet
        print(f"Вот ваши очки {score}")
    elif number1 + number2 == user_number:
        score = score + bet * 4
        print(f"ВЫ ВЫИГРАЛИ И СОРВАЛИ ДЖЕКПОТ ваши очки {score}")
    else:
        print("LOL")
        score = score - bet
        print(score)
