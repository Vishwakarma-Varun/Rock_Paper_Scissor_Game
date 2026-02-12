# Rock,Paper and Scissor Game
'''
To play this game please Enter 
r for Rock
p for Paper
s for Scissor
'''

'''
Rock is 1
Paper is 0
Scissor is -1
'''
import random

computer = random.choice([1,0,-1])

youstr = input("Enter your choice: ")
youdict = {"r" : 1, "p" : 0, "s" : -1}
younum = youdict[youstr]
reversedict ={1 : "Rock", 0 : "Paper", -1 : "Scissor" }

print(f"You choose {reversedict[younum]} and Computer choose {reversedict[computer]}")

if(computer == younum):
    print("It's a draw!")
else:
    if(computer == -1 and younum == 1):
        print("You Win!")
    elif(computer == -1 and younum == 0):
        print("You Lose!")
    elif(computer == 1 and younum == -1):
        print("You Lose!")
    elif(computer == 1 and younum == 0):
        print("You Win!")
    elif(computer == 0 and younum == -1):
        print("You Win!")
    elif(computer == 0 and younum == 1):
        print("You Lose!")
    else:
        print("Something Went Wrong")
    