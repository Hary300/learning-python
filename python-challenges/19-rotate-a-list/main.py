def rotateList(listOfNumbers):
  rotated_number = []
  rotated_number.append(listOfNumbers[len(listOfNumbers) - 1])
  for i in range(len(listOfNumbers) - 1):
    rotated_number.append(listOfNumbers[i])
  print(f"Rotated list: {rotated_number}")

numbers = [1, 2, 3, 4, 5]
rotateList(numbers)