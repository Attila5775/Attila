import random, os, time

LIST = ["rock", "paper", "scissors"]
USER = input("Enter you name: ").title()
POINTS_USER = 0
POINTS_Machine = 0

def main ():
    clear()
    print("*"*30, f"Dear {USER}, you have three options: rock, paper, scissors.", "*"*30)
    print(f"Points of {USER}: {POINTS_USER} \nPoints of Computer: {POINTS_Machine}")
    rule()
    new_game()

def choice():
    player1 = input("Enter your choise: ").lower()
    player2 = random.choice(LIST)
    if player1 not in LIST:
        print("Incorrect value, please try it again from the following options: rock, paper, scissors.")
        time.sleep(6)
        clear()
        main()

    return player1, player2

def rule():
    global POINTS_USER, POINTS_Machine
    choices = choice()
   
    if choices[0] == choices[1]:
        print("Draw. Once again.")
        print("Computer has showed: ", choices[1])
        rule()
    elif (choices[0] == "rock") and (choices[1] == "scissors"):
        print(f"{USER}, you won!")
        print("Computer has showed: ", choices[1])
        POINTS_USER += 1
    elif (choices[0] == "paper") and (choices[1] == "rock"):
        print(f"{USER}, you won!")
        print("Computer has showed: ", choices[1])
        POINTS_USER += 1
    elif (choices[0] == "scissors") and (choices[1] == "paper"):
        print(f"{USER}, you won!")
        print("Computer has showed: ", choices[1])
        POINTS_USER += 1
    else:
        print("You lose!")
        print("Computer has showed: ", choices[1])
        POINTS_Machine += 1

def clear():
    os.system("cls")

def new_game():
    print("*"*50, "Game over", "*"*50)
    quest = input(f"{USER}, would you like to start a new game? y/n")
    if quest == "y":
        clear()
        main()

    else:
        clear()
        print(f"Final result: \nPoints of {USER}: {POINTS_USER} \nPoints of Computer: {POINTS_Machine}")
        exit()

main()
