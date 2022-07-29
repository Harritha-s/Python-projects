import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    random_number = random.randint(0,2)
    user = input("Type rock or paper or scissors or q to quit: " ).lower()
    computer =  options[random_number]
    print("Computer picked", computer +".")
    if user == "q":
        break
    if user not in options:
        continue
    if user == "rock" and computer == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user == "paper" and computer == "rock":
        print ("You won!")
        user_wins += 1
        
    elif user == "scissors" and computer == "paper":
        print ("You won!")
        user_wins += 1
    else:
        print("You lost")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won",computer_wins,"times.")
print ("Goodbye!")