def multipliedByOneToTen():
  askAgain = True
  num = None
  while askAgain:
    userInput = input('Input number: ')
    try:
      num = int(userInput)
      for i in range(10):
        print(f'{num} x {i + 1} = {num * (i + 1)}')
        askAgain = False
    except:
      print('Only number')

multipliedByOneToTen()