import random

dict1 = {1:'Snake',0:'Gun',-1:'Water'}

computer = random.choice([1,0,-1])
YourChoice = int(input("Enter your choice: "))
if not (YourChoice>=-1 and YourChoice<=1):
    YourChoice = int(input("Enter either 1,0 or -1: "))

print(f"Your choice is {dict1[YourChoice]}\nComputer's choice is {dict1[computer]}")

if(computer==YourChoice):
    print("Its a Draw")
else:
    if (computer==1 and YourChoice==0):
        print("You Win!")
    elif(computer==1 and YourChoice==-1):
        print("You Lose!")
    elif(computer==0 and YourChoice==1):
        print("You Lose!")
    elif(computer==0 and YourChoice==-1):
        print("You Win!")
    elif(computer==-1 and YourChoice==1):
        print("You win!")
    elif(computer==-1 and YourChoice==0):
        print("You Lose!")
    else:
        print("Something went wrong....")