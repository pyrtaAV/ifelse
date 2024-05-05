# Даны три числа. Найти наименьшее из них.

list_numbers = []

for i in range(3):
  list_numbers.append(int(input()))
  
temp_number = list_numbers[0]
for i in range(1, len(list_numbers)):
  if list_numbers[i] < temp_number:
    temp_number = list_numbers[i]
    
print(f'Наименьшее из трех чисел: {temp_number}')
