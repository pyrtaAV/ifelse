# Даны два числа. Вывести вначале большее, а затем меньшее из них.
list_numbers = []

for i in range(2):
  list_numbers.append(int(input()))
  
if list_numbers[0] > list_numbers[1]:
  print(f'Наибольшее: {list_numbers[0]}, Наименьшее: {list_numbers[1]}')
else:
  print(f'Наибольшее: {list_numbers[1]}, Наименьшее: {list_numbers[0]}')
