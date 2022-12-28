# Imports
from tinder import Tinder
from secret import email, password

# Main Program

bot = Tinder()
bot.login(email, password)
bot.likeLoop()