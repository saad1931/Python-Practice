
from termcolor import colored
import random
print (colored("Snake,Water & Gun Game", color='green'))
# print (colored("Snake,Water & Gun Game", attrs=['bold']))
# print colored()
Turns=0
cwins=0
uwins=0
while(Turns<10):
    Turns = Turns + 1
    print("Turn Number:", Turns)
    choice=["snake","water","gun"]
    # print(random.choice(choice))
    computer=random.choice(choice)
    user=input("Enter your choice snake,water or gun:")
    if user=="snake":
        if computer=="snake":
            print("It's a tie!")
        elif computer=="water":
            print("User wins!")
            uwins =uwins+1
        elif computer == "gun":
            print("Computer wins!")
            cwins=cwins+1

    elif user=="gun":
        if computer=="gun":
            print("It's a tie!")
        elif computer=="water":
            print("Computer wins!")
            uwins =uwins+1
        elif computer == "snake":
            print("Computer wins!")
            cwins=cwins+1


    elif user=="water":
        if computer=="water":
            print("It's a tie!")
        elif computer=="gun":
            print("User wins!")
            uwins =uwins+1
        elif computer == "snake":
            print("Computer wins!")
            cwins=cwins+1

    else:
        print("Please enter either snake,water or gun")
        Turns = Turns-1
print("--------------------------------------------------------------")
print (colored("Final result of game:",color='green') )
if uwins>cwins:
    print("Turns win by you:",uwins)
    print("Turns win by computer:", cwins)
    print("So congratulations you won the game!")
elif cwins>uwins:
    print("Sorry computer won the game!")
    print("Turns win by you:", uwins)
    print("Turns win by computer:", cwins)
elif cwins==uwins:
    print("It's a tie!!!")
    print("Turns win by you:", uwins)
    print("Turns win by computer:", cwins)

