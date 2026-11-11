def calculateAverage(numbers):
  total = 0
  for number in numbers:
    total += number
  average = total / len(numbers)
  print(f'Average = {average}')


numbers = [10, 20, 30, 40, 50]
calculateAverage(numbers)