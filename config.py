# TEAM RISHU ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "YOUR API ID"
    API_HASH = "YOUR API HASH"  
    TOKEN = os.environ.get("TOKEN", "YOUR BOT TOKEN")
    MONGO_URL = "YOUR MANGO DB URL"
    START_PIC = "https://files.catbox.moe/g2leyq.jpg"
    SUDOERS = filters.user(["YOUR OWNER ID"])
