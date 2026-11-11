def removeDuplicate(numbers):
  result = []
  for number in numbers:
    if number not in result:
      result.append(number)
  print(result)

numbers = [1, 2, 3, 2, 4, 1, 5, 3]
removeDuplicate(numbers)

