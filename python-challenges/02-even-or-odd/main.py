def checkNumber():
  askAgain = True
  num = 0
  while askAgain: 
    userInput = input('Input numbers: ')
    
    try:
      num = int(userInput)
      askAgain = False
    except:
      print('Input number please.')
      
  if num % 2 == 0:
    print(f"{num} is an even number")
  else:
    print(f"{num} is an odd number")

checkNumber()