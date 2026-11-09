def findLargestNumber(numbers):
  largestNumber = numbers[0]
  for number in numbers:
    if(number > largestNumber):
      largestNumber = number
  print(f"Largest number: {largestNumber}")

numbers1 = [12, 45, 7, 89, 23, 56]
numbers2 = [-15, -3, -25, -8, -11]
findLargestNumber(numbers1)
findLargestNumber(numbers2)