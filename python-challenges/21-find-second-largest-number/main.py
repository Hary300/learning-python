def findSecondLargest(list_of_numbers): 
  largest = list_of_numbers[0]
  second_largest = None

  for number in list_of_numbers:
    if(largest < number and (second_largest == None or second_largest < largest)):
      second_largest = largest
      largest = number
    
    if(largest > number and (second_largest == None or second_largest < number)):
      second_largest = number

  print(f'Second largest number: {second_largest}')

numbers = [10, 10, 8, 5, 8]
findSecondLargest(numbers)