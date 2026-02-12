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
    # if we calculate computer-you we will find a pattern based on whic
    # we can decrease the no of line of codes
    # if(computer == -1 and younum == 1):  , computer-you = -2
    #     print("You Win!")
    # elif(computer == -1 and younum == 0): , computer-you = -1
    #     print("You Lose!")
    # elif(computer == 1 and younum == -1): , computer-you = 2
    #     print("You Lose!")
    # elif(computer == 1 and younum == 0): , computer-you = 1
    #     print("You Win!")
    # elif(computer == 0 and younum == -1): , computer-you = 1
    #     print("You Win!")
    # elif(computer == 0 and younum == 1): , computer-you = -1
    #     print("You Lose!")
    # every time we win we get computer- you = -2,1 
    # and every time we lose we get computer - you = -1,2
    # so based on this values:

    if((computer -younum ) == -1 or (computer -younum ) == 2):
        print("You Lose!")
    else:
        print("You Win")