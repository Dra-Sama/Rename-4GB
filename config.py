import os
from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start

API_ID = int(os.getenv("API_ID", "13675555"))
API_HASH = os.environ.get("API_HASH", "c0da9c346d2c45dbc7ec49a05da9b2b6")
TOKEN = os.environ.get("TOKEN", "5304876457:AAFeoeZbD4IPwaOZEpgzqk_tQKVlHtoebgY")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5591954930")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DB_NAME = os.environ.get("DB_NAME", "kagut")
DB_URL = os.getenv("DB_URL", "mongodb+srv://f2l:f2l@cluster0.fjjge1y.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5591954930")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []


#  Optionnal variables
STRING = os.environ.get("STRING", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001728546137")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Wizard_Bots") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://graph.org//file/20df394e337acdfcc4b43.jpg') # image when someone hit /start # image when someone hit /start
# LINK_BYPASS = "False"
