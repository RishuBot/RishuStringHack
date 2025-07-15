# TEAM RISHU ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "14050586"
    API_HASH = "42a60d9c657b106370c79bb0a8ac560c"  
    TOKEN = os.environ.get("TOKEN")
    MONGO_URL = os.environ.get("MONGO_URL")
    START_PIC = "https://envs.sh/enO.jpg"
    SUDOERS = filters.user(["5738579437"])
