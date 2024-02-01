# Chloe Su and Chloe Zou | Chloe team for life! | Jan 2024

import random
import time

prefixes = [  "anti","auto","de","dis","en","fore","in","inter","mid","mis","micro",
"non","over","pre","re","semi","sub","super","trans","un","under"
]
suffixes = [
"able","act","al","ance","dom","er","ed","est","ful","ic",
"ing","tion","ty","ive","less","or","ment","ness","ous"  
]
roots = [
"bio","act","dyn","gen","log","macro","micro","mort","necro","phil",
"phys","psy","stat","co","con","de","dict","care","eco","ex","form",
"hypo","in","inter","intra","iso"
]
defPrefix = [
"against", "oneself", "remove", "opposite of", "cause to", "before", "in", "between",
"middle", "wrongly", "small", "not", "excessive", "before", "again", "half",
"under", "above", "across", "not", "below"
]
defSuffix = [
"can be done", "to do", "having characteristics of",
"having the ability to", "under judgement of", "one who", 
"past tense of","most", "full of", "of/pertaining to", 
"verb form/present participle of", "a process of", "a state of", 
"being", "without", "one that does something", "a process of doing", 
"a state of", "full of"
]
defRoot = [
"life", "move", "power", "born", "speak", "large", "small", "death",
"dead tissue", "loving", "natural order", "spirit or mind", "to stand",
"together", "thoroughly", "away from", "to speak", "concern or grief",
"the environment", "out of", "shape", "beneath", "in, on, or not",
"among us", "within", "equal to"
]

p = random.randint(0, len(prefixes) - 1)
s = random.randint(0, len(suffixes) - 1)
r = random.randint(0, len(roots) - 1)

# Welcome! :D
print("Welcome to the ✨ Word Wizard Thing ✨ :0")
time.sleep(1)
print(" ")
reply = input("Would you like to create a word? (yes/no) ")
reply = reply.lower()

# word maker!!
def run():
  p = random.randint(0, len(prefixes) - 1)
  s = random.randint(0, len(suffixes) - 1)
  r = random.randint(0, len(roots) - 1)
  print(" ")
  print(prefixes[p] + roots[r] + suffixes[s])
  if s < len(defSuffix) and p < len(defPrefix) and r < len(defRoot): 
    print("definition: " + defSuffix[s] + " " + defPrefix[p] + " " + defRoot[r])
  else:
    print("definition: not available")
    print(" ")
    
# chooses an amount of words to make
def num():
  reply = input("How many word(s) would you like to create? ")
  num_words = int(reply)
  for _ in range(num_words):
    run()

# if the user decides to be a killjoy
def no():
  print(" ")
  print("Lame.")
  time.sleep(1.2)
  print("You suck.")
  time.sleep(1.5)
  print("Why do you always have to ruin everything?")
  time.sleep(2)
  print("The entire point of being here is to make words.")
  time.sleep(2)
  print("You get")
  time.sleep(.5)
  print("ONE")
  time.sleep(.7)
  print("more chance.")
  time.sleep(2.5)
  print("Don't mess this up.")
  time.sleep(2)

# killjoy pt. 2
def no2():
  print(" ")
  print("...")
  time.sleep(1.7)
  print("I'm leaving ლ(｀ー´ლ)")
  time.sleep(2)
  print("...")
  time.sleep(2.3)
  print("...")
  time.sleep(2.6)
  print("...")
  time.sleep(2.9)
  print("...")
  print("┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻")

# main program logic
while reply == "yes" or reply == "y":
  num()
if reply == "no" or reply == "n":
  no()
  reply = input("Are you going to create a word? (yes/no) ")
  if reply == "yes" or reply == "y":
    num()
  elif reply == "no" or reply == "n":
    no2()

# Hall of Fame:
# translogive. d: being not speak (how ironic)