name = input("Type your name: ")
print("Welcome to jungle",name,"choose your own path to leave this forest and save your life..Get ready for your adventure!")

answer = input("You have two path which path do you want to choose?(right/left): ").lower()
if answer == "right":
    right = input("You chosen right! you have to choose a vehile to ride on that road which vehicle do you want to choose?(bike/cycle/walk)").lower()
    if right == "bike":
        print ("You choose bike, your bike ran out of petrol and you lost the game!")
    elif right == "cycle":
        print("You choose cycle, after travelling for 2 hours you found a village you won!")
    else:
        print("after travelling you ran out of energy you lost!")
elif answer == "left":
    print ("you chooes the wrong path, so you are again trapped in the forest")
    left = input("if you want to escape you have two options, which is either making a tent to stay tonight or walking for a whole night?(tent/walking): ")
    if left == "tent":
        print ("its a good choice, morning try to move this place and find some food to eat. You won!")
    elif left == "walking":
        print ("there are wild animals, they are roaming and they found you and ate you so you lost the game!")

print("Thank you playing",name)
