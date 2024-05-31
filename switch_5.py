# Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа, например: 
# 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».

def check_range(number: int) -> int | Exception:
    """Функция проверяет что заданное число находится в диапазоне от 100 до 999

    Args:
        number (int): Число введенное пользователем

    Returns:
        int: Число от 100 до 999
    """
    if number in range(100, 1000):
        return number
    return 0


def get_hundred(number: int) -> int:
    """Получаем из трехзначного числа сотки

    Args:
        number (int): Трехзначное число

    Returns:
        int: Сотая часть числа
    """
    return number // 100


def get_ten(number: int) -> int:
    """Получение десяток из трехзначного числа

    Args:
        number (int): трехзначное число введенное пользователем

    Returns:
        int: десятая часть числа, если десятая часть в диапазоне 11..19 то вернется число из этого диапазона
    """
    
    if number % 100 in range(11, 20):
        return number % 100
    return number // 10 % 10


def get_unit(number: int) -> int:
    """Получение единиц из трехзначного числа

    Args:
        number (int): Трехзначное число введенное пользователем

    Returns:
        int: Единичная часть трехзначного числа
    """
    return number % 10


def hundred_str(number: int) -> str:
    """Получение строкового описания сотой части трехзначного числа

    Args:
        number (int): Сотая часть трехзначного числа

    Returns:
        str: Строковое описание трехзначного числа
    """
    hundred_str = {
        1: 'Сто',
        2: 'Двести',
        3: 'Триста',
        4: 'Четыреста',
        5: 'Пятьсот',
        6: 'Шестьсот',
        7: 'Семьсот',
        8: 'Восемьсот',
        9: 'Девятьсот'
    }
    return hundred_str.get(number, '')
    

def ten_str(number: int) -> str:
    """Получаем строковое описание десятой части трехзначного числа

    Args:
        number (int): Десятая часть

    Returns:
        str: Строковое описание десятой части
    """
    return {
            2: 'двадцать',
            3: 'тридцать',
            4: 'сорок',
            5: 'пятьдесят',
            6: 'шестьдесят',
            7: 'семьдесят',
            8: 'восемьдесят',
            9: 'девяносто'
        }.get(number, '')
    
    
def unit_str(number: int) -> str:
    """Получение строкового описания единиц трехзначного числа

    Args:
        number (int): Единицы трехзначного числа

    Returns:
        str: Строковое описание единиц
    """
    return {
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять'    
    }.get(number, '')
    
    
def special_ten_and_unit_str(number: int) -> str:
    """Получение строкового описания десятой части трехзначного числа если она в диапазоне 11..19

    Args:
        number (int): Десятая часть в диапазоне 11..19

    Returns:
        str: Строковое описание десятой части
    """
    return {
        11: 'одиннадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать'
    }.get(number, '')
    

try:
    number = int(input())
except ValueError:
    print("Неверно введено число, необходимо ввести число от 100 до 999 включительно")
    
    
checked_number = check_range(number)

hundred_number_str = hundred_str(get_hundred(number))
ten_number = get_ten(number)
if ten_number not in range(11, 20):
    ten_number_str = ten_str(ten_number)
    unit_number_str = unit_str(get_unit(number))
else:
    ten_number_str = special_ten_and_unit_str(get_ten(number))
    unit_number_str = ''

print(hundred_number_str, ten_number_str, unit_number_str)