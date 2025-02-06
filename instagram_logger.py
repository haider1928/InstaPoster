import instagrapi
from time import sleep
def login(username, password):


    if username and password:
        bot = instagrapi.Client()
        status = bot.login(username=username, password=password)
        return bot

def login_by_session_id(session_id):
    if session_id:
        bot = instagrapi.Client()
        status = bot.login_by_sessionid(sessionid=session_id)
        return bot
    

def logout(bot):
    status = bot.logout()
    return status