# Реализуйте программу калькулятор. На вход подается три значения: 
# первое число, второе число и операция( *, /, + или -) . 
# На выходе должны получить число, после выполнения операции.


def calculator(left_operand: int, right_operand: int, operator: str):
    match operator:
        case '*':
            return f'{left_operand * right_operand}'
        case '/':
            try:
                return f'{left_operand / right_operand}'
            except ZeroDivisionError:
                print('Делить на ноль нельзя')
        case '+':
            return f'{left_operand + right_operand}'
        case '-':
            return f'{left_operand - right_operand}'
        case _:
            return "Данная функция в разработке"


operator = input()
try:
    left_operand = int(input())
    right_operand = int(input())
except ValueError:
    print("Ввели неправильный операнд, Введите число")
    

print(calculator(left_operand=left_operand, right_operand=right_operand, operator=operator))