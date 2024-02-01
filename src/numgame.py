# Chloe Su | Jan 2024
import random

print("Welcome to the number guessing game!")
print("Your goal is to guess a number between in a given range (with hints).")

num2 = input("How many numbers would you like to play with? (recommended: 100) ")
print(" ")

while not num2.isdigit():
  print("Please enter a valid number.")
  num2 = input("How many numbers would you like to play with? (recommended: 100) ")
  print(" ")

num = random.randint(1, int(num2))

guess = int(input("Guess a number between 1-" + num2 + ": "))
attempts = 1

while int(guess) != num:
  if int(guess) < num:
    guess = int(input(str(guess) + " is too low! Guess again: "))
    attempts += 1
  elif int(guess) > num:
    guess = int(input(str(guess) + " is too high! Guess again: "))
    attempts += 1
else:
  print("You guessed " + str(guess) + ". That was correct! :D")
  print("You guessed the number in " + str(attempts) + " tries!")
