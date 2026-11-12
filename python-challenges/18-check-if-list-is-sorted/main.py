def checkSortedList(listOfNumber):
  is_sorted = True

  for i in range(len(listOfNumber) - 1):
    if listOfNumber[i] > listOfNumber[i + 1]:
      is_sorted = False

  if(is_sorted):
    print('The list is sorted.')
  else:
    print('The list is not sorted.')


numbers = [1, 3, 2, 4, 5]
checkSortedList(numbers)