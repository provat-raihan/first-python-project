import random

def get_computer_choice():
    choices = [1, 2, 3]
    return random.choice(choices)


computer_choice = get_computer_choice()
# print(computer_choice)
validchoice=0
win=0
lose=0
for i in range(0,100):
    playerChoice=int(input("enter 1 for Rock:\nenter 2 for paper:\nenter 3 for scissors:\n"))
    if(validchoice>=5):
        break
    if(0<playerChoice<4):
        validchoice+=1
        if(playerChoice==computer_choice):
            print("draw",i)
            
        else:
            if((playerChoice==1 and computer_choice==2)or(playerChoice==2 and computer_choice==3) or (playerChoice==3 and computer_choice==1)):
                print("you lost",i)
                lose+=1
            elif((playerChoice==1 and computer_choice==3)or(playerChoice==2 and computer_choice==1) or (playerChoice==3 and computer_choice==2)):
                print("you win",i)
                win+=1
    else:
        print("enter valid choice",i)
        i-=1
if(win>lose):
    print("you won the game")
elif(win<lose):
    print("you lost the game")
else:
    print("you have drawn the game")