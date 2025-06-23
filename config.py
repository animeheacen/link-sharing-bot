import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

#Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7748292535:AAG890IR05QTS0OZsTXP4Lz3Eyr1iYRBYxk")
APP_ID = int(os.environ.get("APP_ID", "20793620"))
API_HASH = os.environ.get("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")

##---------------------------------------------------------------------------------------------------

#Main 
OWNER_ID = int(os.environ.get("OWNER_ID", "6853851676"))
PORT = os.environ.get("PORT", "8010")

##---------------------------------------------------------------------------------------------------

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://newato9089:wBrKhGpz8Mf5fs61@cluster0.twhxnyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "links-sharing")

##---------------------------------------------------------------------------------------------------

#Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "") #No Need keep it blank
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7825330156").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

##---------------------------------------------------------------------------------------------------        

#Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = None

##---------------------------------------------------------------------------------------------------

#Admin == OWNERID
ADMINS.append(OWNER_ID)
ADMINS.append(5090651635)

##---------------------------------------------------------------------------------------------------

#Default
LOG_FILE_NAME = "links-sharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
##---------------------------------------------------------------------------------------------------
