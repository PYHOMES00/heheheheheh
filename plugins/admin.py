import aiohttp
import os, sys, asyncio, time
from config import *
from database import *
from .utils import get_readable_time
from translation1 import *
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

botStartTime = time.time()


@Client.on_message(filters.private & filters.command(["ping", "p"]))
async def ping(_, message):
    start_t = time.time()
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    
    # Fetch the picture from the provided URL
    picture_url = "https://telegra.ph/file/c05c0889dcd0c1054de3f.jpg"
    
    # Send the picture along with the ping response
    await message.reply_photo(
        photo=picture_url,
        caption=f"Ping 🔥!\n{time_taken_s:.3f} ms"
    )
    return time_taken_s



@Client.on_message(filters.command(["stats", "status", "s"]) & filters.user(Config.OWNER_ID))
async def get_stats(bot, message):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    uptime = get_readable_time(time.time() - botStartTime)    
    time_taken_s = (time.time() - botStartTime) * 1000

    # Fetch the picture from the provided URL
    picture_url = "https://telegra.ph/file/c05c0889dcd0c1054de3f.jpg"

    # Send the picture along with the statistics message
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=picture_url,
        caption=f"**--Bot Status--** \n\n**⌚ Bot Uptime :** `{uptime}` \n**🐌 Current Ping :** `{time_taken_s:.3f} ms` \n**👭 Total Users :** `{users_count}` \n\n**🤖 Total Bots :** `{bots_count}` \n**🔥 Total Channel :** `{total_channels}` \n**🚫 Banned Users :** `{temp.BANNED_USERS}`"
    )


@Client.on_message(filters.private & filters.command(["donate", "d"]))
async def donate(client, message):
    # Fetch the picture from the provided URL
    picture_url = "https://telegra.ph/file/c05c0889dcd0c1054de3f.jpg"
    
    text = """</b>❤️ᴛʜᴀɴᴋs ꜰᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ 😟
ᴅᴏɴᴀᴛᴇ ᴜs ᴛᴏ ᴋᴇᴇᴘ ᴏᴜʀ sᴇʀᴠɪᴄᴇs ᴄᴏɴᴛɪɴᴏᴜsʟʏ ᴀʟɪᴠᴇ 😢
ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴀɴʏ ᴀᴍᴏᴜɴᴛ 
ᴏꜰ 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ ...ᴀs ʏᴏᴜ ᴡɪsʜ 😊
📨 ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs 💳
ɢᴏᴏɢʟᴇᴘᴀʏ / ᴘᴀʏᴛᴍ / ᴘʜᴏɴᴘᴀʏ / ɴᴇᴛ ʙᴀɴᴋɪɴɢ ... 
❤️ꜰᴏʀ ᴅᴏɴᴀᴛɪᴏɴ ᴍᴇssᴀɢᴇ ᴍᴇ💬 
 👉 <i>@shubham_X_official</i> [or here via this bot]
ᴏʀ ʏᴏᴜ ᴄᴀɴ sᴄᴀɴ ᴛʜᴇ ǫʀ ᴄᴏᴅᴇ 👇
ᴜᴘɪ ʟɪɴᴋ 🔗 ᴀʟsᴏ ᴛʜᴇʀᴇ 😇
🌹 ᴛʜᴀɴᴋɪɴɢ ʏᴏᴜ 🌹</b>

🛍 UPI ID:</b> <code>maurya-shubham@fam</code>"""
    keybord = InlineKeyboardMarkup([[
        InlineKeyboardButton('💳 ᴅᴏɴᴀᴛᴇ 💳', url='https://te.legra.ph/Donate-Us-07-05')
        ]])
    
    # Send the picture along with the donation message
    await client.send_photo(
        chat_id=message.chat.id,
        photo=picture_url,
        caption=text,
        reply_markup=keybord
    )
