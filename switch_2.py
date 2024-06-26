# Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). Определить количество 
# дней в этом месяце для невисокосного года.

def days_in_month(month: int):
    """Функция возвращает количество дней в месяце в невисокосный год

    Args:
        month (int): Передается номер месяца от 1 до 12

    Returns:
        _type_: str
    """
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return "В месяце 31 день"
        case 2:
            return "В месяце 28 дней"
        case 4 | 6| 9 | 11:
            return "В месяце 30 дней"
        case _:
            return "Такого месяца не существует"
        

try:
    month = int(input())
except ValueError:
    print("Неправильно введен номер месяца! Введите число от 1 до 12")
    

print(days_in_month(month=month))
        