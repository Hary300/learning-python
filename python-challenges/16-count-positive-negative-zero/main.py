def countPositiveNegativeZero(listOfNumbers):
  positive_count = 0
  negative_count = 0
  zero_count = 0

  for number in listOfNumbers:
    if number > 0:
      positive_count += 1
    elif number < 0:
      negative_count += 1
    else:
      zero_count +=1

  print(f'Positive numbers: {positive_count}')
  print(f'Negative numbers: {negative_count}')
  print(f'Zeros: {zero_count}')



numbers = [10, -5, 0, 8, -2, 3, -1, 0]
countPositiveNegativeZero(numbers)