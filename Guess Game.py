import random

print("="*50, "Guess Game", "="*50)
name = input("Enter your name: ")
print('')
print(f"Dear {name},\nThis is a game, where you have to guess a number between 1 - 5. You have three oportunities. Good luck!")
number = random.randint(1, 5)
number2 = str(input("Enter a number between 1 - 5: "))
tries = 2

while number != number2:
    print(f"Number {number2} was incorrect, still you have {tries} tries")
    tries -= 1
    number2 = str(input("Enter a number between 1 - 5: "))

    if tries == 1 :
        print(f"Number {number2} was incorrect, still you have {tries} try")
        tries -= 1
        number2 = str(input("Enter a number between 1 - 5: "))

    if tries == 0 :
        print("Game over")
        print(f"The correct number was: {number}")
        exit()

print("Congrat you win!\n", f"My number was {number} too.")
