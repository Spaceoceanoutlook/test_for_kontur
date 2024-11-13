import random


def generate_number():
    numbers = [str(i) for i in range(1, 10)]
    random.shuffle(numbers)
    list_numbers = []
    for number in numbers:
        if len(list_numbers) == 4:
            return "".join(list_numbers)
        if number not in list_numbers:
            list_numbers.append(number)


def checking_user_number_for_letters(number: str):
    for n in number:
        if not n.isdigit():
            print('Некорректный запрос: вы ввели не число')
            return False
    return True


def checking_user_number_for_length(number: str):
    if len(number) != 4:
        print('Некорректный запрос: число должно быть четырехзначным')
        return False
    return True


def checking_user_number_for_uniqueness(number: str):
    if len(list(number)) != len(set(number)):
        print('Некорректный запрос: вы ввели неуникальные цифры')
        return False
    return True


if __name__ == "__main__":
    print('Игра "Быки и коровы"')
    print('Нужно отгадать четырехзначное число из уникальных цифр')
    secret_number = generate_number()
    print(secret_number)
    while True:
        bulls, cows = 0, 0
        user_number = input('Введите число: ')
        checks = [checking_user_number_for_letters,
                  checking_user_number_for_length,
                  checking_user_number_for_uniqueness]
        for check in checks:
            if not check(user_number):
                break
        else:
            if user_number == secret_number:
                print('Число угадано')
                break
            for num in user_number:
                if num in secret_number and user_number.index(num) == secret_number.index(num):
                    bulls += 1
                elif num in secret_number:
                    cows += 1
            print(f'{bulls} бык., {cows} кор.')
