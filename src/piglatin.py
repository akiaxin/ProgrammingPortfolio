# Chloe Su | Jan 2024 
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
  if word[0] in vowels:
    return word + "yay"
  else:
    firstPart = ""
    secondPart = ""

  for char in word: 
    if char in vowels:
      break 
    else:
      firstPart += char
  secondPart = word[len(firstPart):]
  return secondPart + firstPart + "ay"

sentence = input("Enter text: ")
words = sentence.split()
translated_words = [pig_latin(word) for word in words]
translated_sentence = " ".join(translated_words)
print(translated_sentence)
