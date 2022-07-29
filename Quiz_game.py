print("Welcome to my computer Quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay! Lets start our quiz...Get ready")
score = 0
answer = input("Do you like python? ").strip()
if answer.lower() == "yes":
    print ("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what is RAM stands for? ").strip()
if answer.lower() == "random access memory":
    print ("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what is CPU stands for? ").strip()
if answer.lower() == "central processing unit":
    print ("Correct")
    score += 1
else:
    print("Incorrect")

print ("Very Good! You got " + str(score) + " questions correct!" )
print ("You got " + str((score / 3) * 100) + "%" )




