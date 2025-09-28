import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from RISHUSTRINGHACK import app

# --- Configure required channels ---
# You can put either the channel username ("MyChannel"), or the numeric chat id (-1001234567890).
# For private channels prefer using numeric id -100xxxxxxxxx and make the bot an admin there.
REQUIRED_CHANNELS = [
    # public channel by username
    {"id": "vip_robotz", "display_name": "Vip_Robotz"},
    # example private channel by numeric id (replace with your actual -100... id)
    {"id": -1002021738886, "display_name": "Ur_Rishu_143"},
    # add more if needed
]

IMAGES = [
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
    "https://graph.org/file/37248e7bdff70c662a702.jpg",
    "https://graph.org/file/0bfe29d15e918917d1305.jpg",
    "https://graph.org/file/16b1a2828cc507f8048bd.jpg",
    "https://graph.org/file/e6b01f23f2871e128dad8.jpg",
    "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
    "https://graph.org/file/ddc5d6ec1c33276507b19.jpg",
    "https://graph.org/file/39d7277189360d2c85b62.jpg",
    "https://graph.org/file/5846b9214eaf12c3ed100.jpg",
    "https://graph.org/file/ad4f9beb4d526e6615e18.jpg",
    "https://graph.org/file/3514efaabe774e4f181f2.jpg",
]

# Updated list of random captions
CAPTIONS = [
    "๏ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ {channel_name} ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ!",
    "๏ ɪᴛ sᴇᴇᴍs ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ {channel_name} ʏᴇᴛ. ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ.",
    "๏ ᴊᴏɪɴ {channel_name} ᴛᴏ ᴜɴʟᴏᴄᴋ ғᴜʟʟ ᴀᴄᴄᴇss ᴛᴏ ᴍʏ ғᴇᴀᴛᴜʀᴇs!",
    "๏ ᴛᴏ ᴜsᴇ ᴍᴇ, ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ {channel_name}. ᴛᴀᴘ ᴛʜᴇ ʟɪɴᴋ ʙᴇʟᴏᴡ.",
    "๏ {channel_name} ᴍᴜsᴛ ʙᴇ ᴊᴏɪɴᴇᴅ ʙᴇғᴏʀᴇ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛɪɴᴜᴇ!",
    "๏ ᴊᴏɪɴ {channel_name} ғᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ᴄᴏɴᴛᴇɴᴛ ᴀɴᴅ ғᴜᴛᴜʀᴇ ᴜᴘᴅᴀᴛᴇs!",
    "๏ {channel_name} ɪs ᴀ ʀᴇǫᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴀᴄᴄᴇss ᴛʜɪs ʙᴏᴛ. ᴊᴏɪɴ ɴᴏᴡ!",
    "๏ ɴᴇᴠᴇʀ ᴍɪss ᴏᴜᴛ! ᴊᴏɪɴ {channel_name} ᴛᴏ ᴇɴᴊᴏʏ ᴛʜᴇ ғᴜʟʟ ᴇxᴘᴇʀɪᴇɴᴄᴇ.",
    "๏ {channel_name} ᴋᴇᴇᴘs ʏᴏᴜ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ʙᴇsᴛ! ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.",
    "๏ ᴛʜɪs ʙᴏᴛ ʀᴇǫᴜɪʀᴇs ᴍᴇᴍʙᴇʀsʜɪᴘ ɪɴ {channel_name}. ᴘʟᴇᴀsᴇ ᴊᴏɪɴ.",
    "๏ ᴊᴏɪɴ {channel_name} ᴀɴᴅ sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ! ʏᴏᴜ'ʟʟ ɴᴇᴇᴅ ɪᴛ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.",
    "๏ {channel_name} ɪs ᴀ ᴘʟᴀᴄᴇ ғᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ᴄᴏɴᴛᴇɴᴛ. ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ᴜɴʟᴏᴄᴋ!",
]

async def send_join_message(msg: Message, link: str, channel_name: str):
    image = random.choice(IMAGES)
    caption = random.choice(CAPTIONS).format(channel_name=channel_name)
    try:
        await msg.reply_photo(
            photo=image,
            has_spoiler=True,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴊᴏɪɴ •", url=link)]]
            ),
        )
        await msg.stop_propagation()
    except ChatWriteForbidden:
        # user blocked the bot or bot can't write to the user
        pass

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channels(app: Client, msg: Message):
    if not REQUIRED_CHANNELS:
        return

    try:
        for chan in REQUIRED_CHANNELS:
            chat_id = chan["id"]
            display_name = chan.get("display_name") or str(chat_id)

            # check membership
            try:
                await app.get_chat_member(chat_id, msg.from_user.id)
                # user is already a member -> continue to next channel
                continue
            except UserNotParticipant:
                # not a member -> prepare an invite/join link
                invite_link = None

                # Try to export/create an invite link (bot must be admin in that channel)
                try:
                    # export_chat_invite_link works for bots (Bot API). If your Pyrogram version has
                    # create_chat_invite_link you can use that instead for more control.
                    invite_link = await app.export_chat_invite_link(chat_id)
                except ChatAdminRequired:
                    # bot is not admin and can't export invite link
                    await msg.reply_text(
                        f"⚠️ I need admin rights in **{display_name}** to create an invite link. "
                        "Make the bot an admin in that channel and try again."
                    )
                    await msg.stop_propagation()
                    return
                except Exception:
                    # export failed (maybe channel is public but has no username, or other error)
                    invite_link = None

                # Fallback: if chat_id is a username string, use t.me/username
                if not invite_link:
                    if isinstance(chat_id, str) and not str(chat_id).startswith("-"):
                        invite_link = f"https://t.me/{chat_id}"

                # If still no valid link, notify owner/admin (or show generic message)
                if not invite_link:
                    await msg.reply_text(
                        f"⚠️ Cannot generate a join link for **{display_name}**. "
                        "Ensure the bot is admin in that channel or provide a public username."
                    )
                    await msg.stop_propagation()
                    return

                # send join message with the obtained link
                await send_join_message(msg, invite_link, display_name)

    except ChatAdminRequired:
        # This happens if the bot tried some admin action and wasn't admin somewhere
        print("Please make the bot admin in the required channels to allow invite link generation.")