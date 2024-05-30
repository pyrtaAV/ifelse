# Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. 
# Вывести значения D и M для даты, следующей за указанной.

def next_day_and_month(day: int, month: int):
    """Функция возвращает следующую дату невисокосного года

    Args:
        day (int): Принимает день
        month (int): Принимает месяц

    Returns:
        _type_: str
    """
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10:
            if day != 31:
                return f'Следующий день {day + 1}, следующий месяц {month}'
            return f'Следующий день {1}, следующий месяц {month + 1}'
        case 2:
            if day != 28:
                return f'Следующий день {day + 1}, следующий месяц {month}'
            return f'Следующий день {1}, следующий месяц {month + 1}'
        case 4 | 6| 9 | 11:
            if day != 30:
                return f'Следующий день {day + 1}, следующий месяц {month}'
            return f'Следующий день {1}, следующий месяц {month + 1}'
        case 12:
            if day != 31:
                return f'Следующий день {day + 1}, следующий месяц {month}'
            return f'Следующий день {1}, следующий месяц {1}'
        case _:
            return "Такой даты не существует"


try:
    day = int(input())
    month = int(input())
except ValueError:
    print("Неправильно введена дата!")
    

print(next_day_and_month(day=day, month=month))
