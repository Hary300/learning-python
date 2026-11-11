def separatePositiveAndNegative(numbers):
  positiveNumber = []
  negativeNumber = []

  for number in numbers:
    if number > 0:
      positiveNumber.append(number)
    elif number < 0:
      negativeNumber.append(number)

  print(f'Positive numbers: {positiveNumber}')
  print(f'Negative numbers: {negativeNumber}')

numbers = [10, -5, 0, 8, -2, 3, -1]
separatePositiveAndNegative(numbers)