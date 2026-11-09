def count(numbers):
  positiveNumber = 0
  for i in range(len(numbers)):
    if numbers[i] > 0:
      positiveNumber += 1
  print(f"Positive number: {positiveNumber}")

count([10, -5, 0, 8, -2, 3, -1])