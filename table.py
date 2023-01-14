import getpass

username = "Robert"
password = "pass123"
tries = 3

print("Welcome, please enter your username and password. (You have three tries.)")
username_input = input("Username: ")
#pswd = input("Password: ")
pswd = getpass.getpass('Password:')

while (username != username_input) and (password != pswd):
        tries -= 1
        if tries == 0:
            exit()

        print(f"Incorrect username or password! You have left {tries} tries!")
        username_input = input("Username: ")
        pswd = getpass.getpass('Password:')

        if (username == username_input) and (password == pswd):
            print(f"Hello {username}! Welcome.")

   






    

