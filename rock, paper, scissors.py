import random, os

LIST = ["rock", "paper", "scissors"]
USER = input("Enter you name: ").title()

def main ():
    clear()
    print("*"*30, f"Dear {USER}, have three options: rock, paper, scissors.", "*"*30)
    rule()
    new_game()

def choice():
    player1 = input("Enter your choise: ").lower()
    player2 = random.choice(LIST)
    return player1, player2

def rule():
    choices = choice()
    if choices[0] == choices[1]:
        print("Draw")
        print(choices[1])
    elif (choices[0] == "rock") and (choices[1] == "scissors"):
        print(f"{USER}, you won!")
        print(choices[1])
    elif (choices[0] == "paper") and (choices[1] == "rock"):
        print(f"{USER}, you won!")
        print(choices[1])
    elif (choices[0] == "scissors") and (choices[1] == "paper"):
        print(f"{USER}, you won!")
        print(choices[1])
    else:
        print("You lose!")
        print(choices[1])

def clear():
    os.system("cls")

def new_game():
    quest = input(f"{USER}, would you like to start a new game? y/n")
    if quest == "y":
        clear()
        main()

    else:
        exit()

main()
