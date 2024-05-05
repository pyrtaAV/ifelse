list_numbers = []

for i in range(2):
  list_numbers.append(int(input()))
  
if list_numbers[0] > list_numbers[1]:
  print(f'Наибольшее из двух чисел: {list_numbers[0]}')
else:
  print(f'Наибольшее из двух чисел: {list_numbers[1]}')
