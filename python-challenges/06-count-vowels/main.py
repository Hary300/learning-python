def countVowels():
  vowels = ['a', 'e', 'i', 'o', 'u']
  foundVowels = []
  userInput = input('Input a word or sentence: ')

  for letter in userInput:
    for vowel in vowels:
      if letter.lower() == vowel and letter not in foundVowels:
        foundVowels.append(letter)
        

  print(f"Total vowels: {len(foundVowels)}")

countVowels()