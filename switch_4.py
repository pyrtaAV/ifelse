# Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток) 
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо. 
# Дан символ C — исходное направление робота и целое число N — посланная ему команда. 
# Вывести направление робота после выполнения полученной команды.


def check_action(turn_key: str, action: int):
    """Функция вызывает необходимое действие с направлением в зависимости от действия

    Args:
        turn_key (str): Текущее направление
        action (int): Действие для изменения направления

    Returns:
        _type_: str
    """
    match action:
        case 0:
            return turn_key
        case 1:
            return change_turn_left(turn_key=turn_key)
        case -1:
            return change_turn_right(turn_key=turn_key)
            

def change_turn_left(turn_key: str):
    new_turn = {
        'С': 'З',
        'З': 'Ю',
        'Ю': 'В',
        'В': 'С'
    }
    return new_turn.get(turn_key, "Такого направления не существует")
      
      
def change_turn_right(turn_key: str):
    new_turn = {
        'С': 'В',
        'В': 'Ю',
        'Ю': 'З',
        'З': 'С'
    }
    return new_turn.get(turn_key, "Такого направления не существует")


turn_key = input()
try:
    action = int(input())
except ValueError:
    print('Неправильное действие, выберите 0, 1 или -1')


print(check_action(turn_key=turn_key, action=action))
