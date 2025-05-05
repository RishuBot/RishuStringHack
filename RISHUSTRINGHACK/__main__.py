import asyncio
import importlib
import threading
import time
import requests
from flask import Flask
from pyrogram import idle
from RISHUSTRINGHACK import LOG
from RISHUSTRINGHACK.modules import ALL_MODULES

# Flask app initialize kar rahe hain
flask_app = Flask(__name__)

# Flask app ka ek basic route
@flask_app.route('/')
def home():
    return "Flask app running on port 8000"

# Flask app ko alag thread mein run karne ka function
def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

# Keep-alive function jo regular ping bhejta rahega
def keep_alive():
    while True:
        try:
            # Apne Render app ka URL daal kar ping karein
            requests.get("https://nearby-tabbie-pyrogram-f99a60ab.koyeb.app/")
        except Exception as e:
            print(f"Ping error: {e}")
        # Har 5 minute mein ping karein
        time.sleep(150)

# Bot ke start karne ka async function
async def start_bot():
    # Modules ko dynamically import kar rahe hain
    for all_module in ALL_MODULES:
        importlib.import_module("RISHUSTRINGHACK.modules." + all_module)
    
    LOG.print("[bold yellow]𝗛𝗔𝗖𝗞 𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐄𝐃 𝐍𝐎𝐖 𝗙𝗨𝗖𝗞 𝗔𝗟𝗟 𝗧𝗚 𝗜𝗗")
    
    # Bot ko idle mode mein daal rahe hain taaki continuous run ho
    await idle()

    LOG.print("[bold red]𝐂𝐀𝐍𝐂𝐋𝐄 𝐀𝐋𝐋 𝐓𝐀𝐒𝐊🤐..........")

# Flask app ko alag thread mein start kar rahe hain
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Keep-alive function ko alag thread mein start kar rahe hain
keep_alive_thread = threading.Thread(target=keep_alive)
keep_alive_thread.start()

# Bot ko asyncio loop ke through run kar rahe hain
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
