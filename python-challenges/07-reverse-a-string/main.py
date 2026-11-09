def reverseText():
  userInput = input("Input text: ")
  reversedText = ''
  for i in range(len(userInput) - 1, -1, -1):
    reversedText += userInput[i]
  print(f"Reversed text: {reversedText}")

reverseText()