def getNumberInput(step):
  askAgain = True
  num = None

  while askAgain:
      userInput = input(f'input the {step} number: ')
      try:
        num = int(userInput)
        askAgain = False
      except:
        print('it has to be a number')
  return num

def compareNum():
  num1 = getNumberInput('first')
  num2 = getNumberInput('second')

  if num1 < num2:
    print(f"{num2} is greater than {num1}")
  elif num1 > num2:
    print(f"{num1} is greater than {num2}")
  else:
    print("Both numbers are equal")
  
compareNum()

