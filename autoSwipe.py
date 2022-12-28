# Imports
from tinder import Tinder
from bumble import Bumble
from secret import email, password

# Main Program

bot = Tinder()
bot.login(email, password)
bot.likeLoop()

# bot = Bumble()
# bot.login(email, password)
# bot.likeLoop()