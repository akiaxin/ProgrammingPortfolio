# Chloe Su | Jan 2024 

import time

print("       __,---.__")
print("    ,-'         `-.__")
print("  &/           `._\\ _\\")
print("  /              o o\_")
print("  |                 (\")")
print("  |__/--..--|__|--''")
print(" ")
print("Welcome to the Pig Latin Translator!")
print(" ")

def pig_latin(word):
  word = word.lower()
  length = len(word)
  vowels = ['a', 'e', 'i', 'o', 'u', 'y']  
  punctuation = ''
  
  if not word[-1].isalnum():
    punctuation = word[-1]
    word = word[:-1]
    
  if word[0] in vowels:
    return word + "yay" + punctuation
  else:
    firstPart = ""
    secondPart = ""

  for char in word: 
    if char in vowels:
      break 
    else:
      firstPart += char
  secondPart = word[len(firstPart):]
  return secondPart + firstPart + "ay" + punctuation

reply = 'y'
while reply.lower() == "y" or reply.lower() == "yes":
  sentence = input("Enter text: ")
  words = sentence.split()
  translated_words = [pig_latin(word) for word in words]
  translated_sentence = " ".join(translated_words)
  print("Translation: " + translated_sentence)
  print(" ")
  time.sleep(1)
  reply = input("Translate more text? (y/n): ")
else:
  print("Farewell, thank you for using the Pig Latin Translator!")