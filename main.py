import random


def generate_number() -> str:
    """ Возвращает четырехзначное число из уникальных цифр """
    numbers = random.sample(range(1, 10), 4)
    return ''.join(map(str, numbers))


def checking_user_number_for_letters(number: str) -> bool:
    """ Проверяет входящее значение на цифровые символы """
    if not number.isdigit():
        print('Некорректный запрос: вы ввели не число')
        return False
    return True


def checking_user_number_for_length(number: str) -> bool:
    """ Проверяет входящее значение на длину """
    if len(number) != 4:
        print('Некорректный запрос: число должно быть четырехзначным')
        return False
    return True


def checking_user_number_for_uniqueness(number: str) -> bool:
    """ Проверяет входящее значение на уникальность символов"""
    if len(set(number)) != 4:
        print('Некорректный запрос: вы ввели неуникальные цифры')
        return False
    return True


if __name__ == '__main__':
    print('Игра "Быки и коровы"')
    # Получаем загаданное число
    secret_number = generate_number()
    while True:
        bulls, cows = 0, 0
        user_number = input('Введите число: ')
        # Проверяем число на корректность
        checks = [checking_user_number_for_letters,
                  checking_user_number_for_length,
                  checking_user_number_for_uniqueness]
        if all(check(user_number) for check in checks):
            if user_number == secret_number:
                print('Число угадано!')
                break
            # Находим количество быков и коров в переданном числе

            for user_digit, secret_digit in zip(user_number, secret_number):
                if user_digit == secret_digit:
                    bulls += 1
                elif user_digit in secret_number:
                    cows += 1
            print(f'{bulls} бык., {cows} кор.')
