import random

print("="*50, "Guess Game", "="*50)
name = input("Enter your name: ")
print('')
print(f"Dear {name},\nThis is a game, where you have to guess a number between 1 - 5. You have three oportunities. Good luck!")

number = random.randint(1, 6)
number2 = int(input("Enter a number between 1 - 6: "))
tries = 3

while number != number2:
    tries -= 1
    print(f"Number {number2} was incorrect, still you have {tries} tries")
    number2 = int(input("Enter a number between 1 - 6: "))

    if tries == 1 :
        print(f"Number {number2} was incorrect, still you have {tries} try")
        tries -= 1
        number2 = int(input("Enter a number between 1 - 6: "))

    if tries == 0 :
        print("Game over")
        print(f"The correct number was: {number}")
        print("="*50, "Guess Game", "="*50)
        exit()

print("Congrat you win!\n" f"My number was {number} too.")
print("="*50, "Guess Game", "="*50)
