# Rock-paper-scissor-game-

import random
computer = random.choice([1,2,3])
yourstr=input("enter your choice: ")
youDict={"R":1,"P":2,"S":3}
reverseDict={1:"Rock",2:"paper",3:"scissor"}
you = youDict[yourstr]
print(f"you choose {reverseDict[you]} \ncomputer choose {reverseDict[computer]} ")
if(you==computer):
    print("it's a draw")
else:
    if(you == 1 and computer == 2):
        print("you lose!")
    elif(you == 1 and computer == 3):
        print("you win!")
    elif(you == 2 and computer == 1):
        print("you win!")
    elif(you == 2 and computer == 3):
        print("you lose!")    
    elif(you == 3 and computer == 1):
        print("you lose!")
    elif(you == 3 and computer == 2):
        print("you win!")       
        
