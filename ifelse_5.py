# Даны координаты точки, не лежащей на координатных осях OX и OY. Определить номер координатной четверти, в которой находится данная точка. Координаты задаются пользователем, например (10, 15).

list_numbers = []

for i in range(2):
  list_numbers.append(int(input()))
  
if list_numbers[0] > 0 and list_numbers[1] > 0:
  print(f'Точка находится в первой четверти')
elif list_numbers[0] < 0 and list_numbers[1] < 0:
  print(f'Точка находится в третьей четверти')
elif list_numbers[0] < 0 and list_numbers[1] > 0:
  print(f'Точка находится во второй четверти')
elif list_numbers[0] > 0 and list_numbers[1] < 0:
  print(f'Точка находится в четвертой четверти')