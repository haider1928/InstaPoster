import instagrapi
from time import sleep
def login(username, password):


    if username and password:
        bot = instagrapi.Client()
        status = bot.login(username=username, password=password)
        return bot
