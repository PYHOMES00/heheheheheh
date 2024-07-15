import os

class Config:
    API_ID = "28243586"
    API_HASH = "4022d5686b9b7a7cf8891205921a0ab3"
    BOT_TOKEN = "7151356654:AAF5JV1bK-CzeB_KlAUKABipL_JjIjFwEzA"
    BOT_SESSION = "forward-bot" 
    DATABASE_URI = "mongodb+srv://madarazbotz:Olm2V88uGXRS5m8y@cluster0.i58ntas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_NAME = "Cluster0"
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '5340652544').split()]
    BOT_OWNER_ID = [int(id) for id in os.environ.get("BOT_OWNER_ID", '5340652544').split()]
    UPDATES_CHANNEL = "-1002198706552"

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    

