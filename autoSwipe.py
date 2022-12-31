# Imports
from tinder import Tinder
from bumble import Bumble
from secret import email, password

# Main Program

choice = 'NULL'

while choice != 1 and choice != 2:
    choice = input("1. Tinder" + "\n" + "2. Bumble" + "\n")

    if choice in '1':
        tinder_bot = Tinder()
        tinder_bot.login(email, password)
        tinder_bot.likeLoop()

    elif choice in '2':
        bumble_bot = Bumble()
        bumble_bot.login(email, password)
        bumble_bot.likeLoop()

    else:
        print("Invalid input.")