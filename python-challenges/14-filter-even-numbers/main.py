def filterEvenNumber(numbers):
  result = []
  for number in numbers:
    if(number % 2 == 0):
      result.append(number)
  print(f'Even numbers: {result}')

numbers = [-3, -2, -1, 0, 1, 2]
filterEvenNumber(numbers)
