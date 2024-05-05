list_numbers = []
count = 0

for i in range(3):
  list_numbers.append(int(input()))
  
for item in list_numbers:
  if item > 0:
    count += 1
    
print(f'Количество положительных чисел: {count}')
