def compareNum():
  askAgain = True
  num1 = 0
  num2 = 0

  while askAgain:
    userInput1 = input('input the first number: ')
    try:
      num1 = int(userInput1)
    except:
      print('it has to be a number')

    userInput2 = input('input the second number: ')

    try:
      num2 = int(userInput2)
      askAgain = False
    except:
      print('it has to be a number')

  if num1 < num2:
    print(f"{num2} is greater than {num1}")
  elif num1 > num2:
    print(f"{num1} is greater than {num2}")
  else:
    print("Both numbers are equal")
  


compareNum()