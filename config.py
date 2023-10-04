# Don't Remove Credit @joinwwm


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "3963229")

API_HASH = os.environ.get("API_HASH", "11a3a7d73784aacd3d6b7b2134948fd7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6698160546:AAGUr1DXZhha7VurKAf15Vq8P0NqznaJ_5w") 

FORCE_SUB = os.environ.get("FORCE_SUB", "wwmsupport") 

             # Don't Remove Credit @joinwwm


DB_NAME = os.environ.get("DB_NAME", "sample")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://mansur:<Mansur@786>@sample.m2976v6.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/baff44512cd9b207e4583.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '902249781').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @joinwwm

