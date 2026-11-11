def findSmallestNum(numbers):
  smallestNumber = numbers[0]
  for number in numbers:
    if number < smallestNumber:
      smallestNumber = number
  print(f'Smallest number: {smallestNumber}')

numbers = [12, 45, 7, 89, 23, 3]
findSmallestNum(numbers)