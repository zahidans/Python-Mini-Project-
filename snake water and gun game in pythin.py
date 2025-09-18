import random
"""
1 for snake
-1 for water
0 for gun
"""
computer = random.choice ([-1, 0, 1])
youstr = input("Enter your choice :")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reversDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youstr]

print(f"You chose {reversDict[you]}\nComputer chose {reversDict[computer]}")

if(computer == you):
    print("its a drow!")

else:
    if(computer == -1 and you == -1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("you lose!")

    elif(computer == 1 and you == -1):
        print("you lose!")

    elif(computer ==1 and you == 0):
        print("you Win!")

    elif(computer == 0 and you == -1):
        print("you Win!")

    elif(computer == 0 and you == 1):
        print("you lose!")

    else:
        print("somthing went wrong !")