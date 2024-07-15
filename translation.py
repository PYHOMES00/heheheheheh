import os
from config import Config

class Translation(object):
  START_TXT = """ʜᴇʟʟᴏ {}

➻ ɪ'ᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟʟ ᴀᴜᴛᴏ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ
  
➻ ɪ ᴄᴀɴ ғᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ
  
➻ ᴡɪᴛʜ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs.
ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ
  
<b>👨🏼‍💻 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: @FILM_NEST</b>"""

  HELP_TXT = """<b><u>🔆 HELP</b></u>

<u>**📚 Available commands:**</u>
<b>⏣ __/start - check I'm alive__ 
⏣ __/forward - forward messages__
⏣ __/unequify - delete duplicate messages in channels__
⏣ __/settings - configure your settings__
⏣ __/reset - reset your settings__</b>

<b><u>💢 Features:</b></u>
<b>► __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission__
► __Forward message from private channel to your channel by using userbot(user must be member in there)__
► __custom caption__
► __custom button__
► __support restricted chats__
► __skip duplicate messages__
► __filter type of messages__
► __skip messages based on extensions & keywords & size__</b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
<b>► __add a bot or userbot__
► __add atleast one to channel__ `(your bot/userbot must be admin in there)`
► __You can add chats or bots by using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
► __Then use /forward to forward messages__</b>"""
  
  ABOUT_TXT = """<b>╭──────❰ 🤖 Bot Details ❱──────〄
│ 
│ 🤖 Mʏ Nᴀᴍᴇ : <a href=https://t.me/FNforward_bot>ғᴏʀᴡᴀʀᴅ ʙᴏᴛ</a>
│ 👨‍💻 ᴅᴇᴠᴘʟᴏᴇʀ : <a href=https://t.me/Anmol0700>ᴍɪɢᴜᴇʟ ᴏ’ʜᴀʀᴀ!</a>
│ 🤖 ᴜᴘᴅᴀᴛᴇ  : <a href=https://t.me/Film_Nest>FilmNest </a>
│ 📡 ʜᴏsᴛ ᴏɴ : <a href=http://microsoft.com/>Microsoft Altair 8800 computer</a>
│ 🗣️ ʟᴀɴɢᴜᴀɢᴇ  : ᴘʏᴛʜᴏɴ 3 
{python_version}
│ 📚 ʟɪʙʀᴀʀʏ  : ᴘʏʀᴏɢʀᴀᴍ  
╰────────────────────⍟</b>"""
  
  STATUS_TXT = """
╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼👥 Tᴏᴛᴀʟ Usᴇʀs: {}
║┃
║┣⪼🤖 Tᴏᴛᴀʟ Bᴏᴛ: {}
║┃
║┣⪼🔃 Fᴏʀᴡᴀʀᴅɪɴɢs: {}
║┃
║┣⪼📢 Tᴏᴛᴀʟ Cʜᴀɴɴᴇʟs: {}
║┃
║┣⪼🚫 Bᴀɴɴᴇᴅ Usᴇʀs: {}
║┃
║╰━━━━━━━━━━━━━━━➣
╚═════════════❍⊱❁۪۪
""" 
  
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """
╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼𖨠 ғᴇᴄʜᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼𖨠 sᴜᴄᴄᴇssғᴜʟʟʏ ғᴏʀᴡᴀʀᴅᴇᴅ: </b> <code>{}</code>
║┃
║┣⪼𖨠 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼𖨠 ᴅᴇʟᴇᴛᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼𖨠 sᴋɪᴘᴘᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼𖨠 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs: </b> <code>{}</code>
║┃
║┣⪼𖨠 ᴘᴇʀᴄᴇɴᴛᴀɢᴇ: </b> <code>{}</code>%
║╰━━━━━━━━━━━━━━━➣ 
╚════❰{}❱══❍⊱❁۪۪
"""

  TEXT1 = """<b>╭─❰ <u>Forwarded Status</u> ❱─❍
┃
┣⊸🕵𝙁𝙚𝙘𝙝𝙚𝙙 𝙈𝙨𝙜 : {}
┣⊸✅𝙎𝙪𝙘𝙘𝙚𝙛𝙪𝙡𝙮 𝙁𝙬𝙙 : {}
┣⊸👥𝘿𝙪𝙥𝙡𝙞𝙘𝙖𝙩𝙚 𝙈𝙨𝙜: {}
┣⊸🗑𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝙈𝙨𝙜: {}
┣⊸🪆𝙎𝙠𝙞𝙥𝙥𝙚𝙙 : {}
┣⊸📊𝙎𝙩𝙖𝙩𝙨 : {}
┣⊸⏳𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 : {}
┣⊸𝙀𝙏𝘼 : {}
┃
╰─⌊ {} ⌉─❍</b>"""

  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>★ YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>★ FROM CHANNEL:</b> `{from_chat}`
<b>★ TO CHANNEL:</b> `{to_chat}`
<b>★ SKIP MESSAGES:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) must be admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** is private your userbot must be member or your bot must be admin in there also</b></i>

<b>If the above is checked then the yes button can be clicked</b>"""
