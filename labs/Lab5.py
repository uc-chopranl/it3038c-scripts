import random

random_number = random.randint(0, 50)

user_guess = 0

while user_guess != random_number:

  user_guess = input("Guess a number between 1 and 50: ")

  user_guess = int(user_guess)

  if user_guess > random_number:

    print("Too high! Guess again.")

  elif user_guess < random_number:

    print("Too low! Guess again.")
    
  if user_guess == random_number:
      
    print("You guessed the number correctly!" + " " + str(random_number))
      
    break