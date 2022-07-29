import random

print("Welcome to guessing game!")
range_number = int(input("Enter a range: "))
random_number = random.randint(0,range_number)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Enter a quess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    if user_guess > random_number:
        print("Your guess is above the Random number")
    else :
        print("Your guess is below the Random number")

print("You got it in",guesses,"guesses")

