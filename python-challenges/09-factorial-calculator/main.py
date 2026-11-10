def calculateFactorial():
  askAgain = True
  num = None
  while askAgain:
    try:
      userInput = input('Input number: ')
      num = int(userInput)
      askAgain = False
    except:
      print('Only number please.')

  result = 1
  for i in range(num, 1, -1):
    result *= i
  print(f"Factorial of {num} is {result}")

calculateFactorial()