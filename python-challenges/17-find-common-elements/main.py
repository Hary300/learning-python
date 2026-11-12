def findCommonElements(listOfNumber1, listOfNumber2):
  common_elements = []
  for number in listOfNumber1:
    if number in listOfNumber2:
      common_elements.append(number)

  print(common_elements)
list_a = [1, 2, 3, 4, 5, 2]
list_b = [3, 4, 5, 6, 7, 4]

findCommonElements(list_a, list_b)