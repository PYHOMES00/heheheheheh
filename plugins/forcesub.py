# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey!  


import asyncio
from config import Config
import pyrogram
from pyrogram import Client,filters, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message



async def ForceSub(c: Client, m: Message):
    try:
        invite_link = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        invite_link = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except Exception as err:
        print(f"Uɴᴀʙʟᴇ ᴛᴏ ᴅᴏ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ {Config.UPDATES_CHANNEL}\n\nError: {err}")
        return 200
    try:
        user = await c.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=m.from_user.id)
        if user.status == "kicked":
            await c.send_message(
                chat_id=m.from_user.id,
                text="Sᴏʀʀʏ sɪʀ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴍʏ ᴀᴅᴍɪɴ @Film_Nest .",
                disable_web_page_preview=True,
                parse_mode="Markdown",
                
            )
            return 400
    except UserNotParticipant:
        await c.send_message(
            chat_id=m.from_user.id,
            text="**Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ!**\n\n Oɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Jᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url=invite_link.invite_link)
                    ]
                ]
            )
            
        )
        return 400
    except Exception:
        await c.send_message(
            chat_id=m.from_user.id,
            text="Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ ᴀᴅᴍɪɴ.",
            disable_web_page_preview=True,
            parse_mode="Markdown",
        )
        return 400
    return 200


# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey!  
