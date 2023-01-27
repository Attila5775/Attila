import os, time, random

GAMER = input("Enter your name: ")
TRIES = 3
MACHINE_NUMBER = random.randint(1, 6)

def main():
    clear_screen()
    #print(f"Dear {GAMER}, \nWelcome in the GUESS GAME! :)")
    #time.sleep(3)
    clear_screen()
    intro()
    game()
    exit()

def intro():
    print("="*50, "Guess Game", "="*50)
    print(f"You have to guess a number between 1-6. You will have {TRIES} tries.")
    #time.sleep(5)

def game():
    global TRIES, MACHINE_NUMBER
    TRIES = 3
    MACHINE_NUMBER = random.randint(1, 6)
    user_guess = input("Enter your guess: ")
    while str(MACHINE_NUMBER) != user_guess:
        TRIES -= 1
        print(f"Your guess was incorrect, please try it again. You still have {TRIES} tries.")
        user_guess = input("Enter your guess: ")
        if TRIES == 1:
            print(f"The number was: {MACHINE_NUMBER}")
            print("Game over! You lost.")
            print("="*50, "Guess Game", "="*50)
            new_game()

    if str(MACHINE_NUMBER) == user_guess:
        print("You won! Congratulation!")
        print(f"The number was: {MACHINE_NUMBER}")
        print("="*50, "Guess Game", "="*50)
        new_game()

def clear_screen():
    os.system('cls')

def new_game():
    new_games = input("Would you like it again: y/n: ")
    if new_games == "y":
        game()

    else:
        exit()

main()

