def findIndex(listOfElement, target):
  found_index = -1
  for i in range(len(listOfElement)):
    if listOfElement[i] == target:
      found_index = i
      break

  if found_index is not -1:
    print(f"Element found at index: {found_index}")
  else:
    print('Element not found.')



numbers = [10, 20, 30, 40, 50]
target = 99

findIndex(numbers, target)