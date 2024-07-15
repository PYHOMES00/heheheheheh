import os
from config import Config

class Translation(object):
  START_TXT = """ʜᴇʟʟᴏ {}

➻ ɪ'ᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟʟ ᴀᴜᴛᴏ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ
  
➻ ɪ ᴄᴀɴ ғᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ
  
➻ ᴡɪᴛʜ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs.
ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ
  
<b>👨🏼‍💻 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: @FILM_NEST</b>"""


  HELP_TXT = """<b><u>🛠️ Help</b></u>

<b><u>📚 Available Commands :</u></b>
⏣ __/start - Check I'm Alive__ 
⏣ __/forward - Forward Messages__
⏣ __/unequify - Delete Duplicate Messages In Channels__
⏣ __/settings - Configure Your Settings__
⏣ __/reset - Reset Your Settings__

<b><u>💢 Features :</b></u>
► __Forward Message From Public Channel To Your Channel Without Admin Permission. If The Channel Is Private Need Admin Permission__
► __Forward Message From Private Channel To Your Channel By Using Userbot(User Must Be Member In There)__
► __Custom Caption__
► __Custom Button__
► __Support Restricted Chats__
► __Skip Duplicate Messages__
► __Filter Type Of Messages__
► __Skip Messages Based On Extensions & Keywords & Size__
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding :</b></u>
  
► __Add A Bot Or Userbot__
► __Add Atleast One To Channel (Your Bot/Userbot Must Be Admin In There)__
► __You Can Add Chats Or Bots By Using /settings__
► __If The **From Channel** Is Private Your Userbot Must Be Member In There Or Your Bot Must Need Admin Permission In There Also__
► __Then Use /forward To Forward Messages__"""
  
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
  
  STATUS_TXT = """<b><u>Bot Status</u></b>
  
<b>👱 Total Users :</b> <code>{}</code>

<b>🤖 Total Bots :</b> <code>{}</code>

<b>🔃 Forwardings :</b> <code>{}</code>
"""
  
  FROM_MSG = "<b><u>Set Source Chat</></>\n\nForward The Last Message Or Last Message Link Of Source Chat.\n/cancel - To Cancel This Process"
  TO_MSG = "<b><u>Choose Target Chat</u></b>\n\nChoose Your Target Chat From The Given Buttons.\n/cancel - To Cancel This Process"
  SKIP_MSG = "<b><u>Set Message Skiping Number</u></b>\n\nSkip The Message As Much As You Enter The Number And The Rest Of The Message Will Be Forwarded\nDefault Skip Number = <code>0</code>\n<code>eg: You Enter 0 = 0 Message Skiped\nYou Enter 5 = 5 Message Skiped</code>\n/cancel - To Cancel This Process"
  CANCEL = "Process Cancelled Succefully !"
  BOT_DETAILS = "<b><u>📄 Bot Details</u></b>\n\n<b>➣ Name :</b> <code>{}</code>\n<b>➣ Bot ID :</b> <code>{}</code>\n<b>➣ Username :</b> @{}"
  USER_DETAILS = "<b><u>📄 UserBot Details</u></b>\n\n<b>➣ Name :</b> <code>{}</code>\n<b>➣ User ID :</b> <code>{}</code>\n<b>➣ Username :</b> @{}"  
         
  TEXT = """<b><u>Forwarded Status</u></b>

<b>🕵 Fetched Message :</b> <code>{}</code>

<b>✅ Successfully Forward :</b> <code>{}</code>

<b>👥 Dublicate Message :</b> <code>{}</code>

<b>🗑 Deleted Message :</b> <code>{}</code>

<b>🪆 Skipped :</b> <code>{}</code>

<b>📊 Stats :</b> <code>{}</code>

<b>⏳ Progress :</b> <code>{}</code>

<b>⏰ ETA :</b> <code>{}</code>

{}"""

  DUPLICATE_TEXT = """<b><u>Unequify Status</u></b>

<b>🕵 Fetched Files :</b> <code>{}</code>

<b>👥 Dublicate Deleted :</b> <code>{}</code>

{}
"""
  DOUBLE_CHECK = """<b><u>Double Checking</u></b>
  
Before Forwarding The Messages Click The Yes Button Only After Checking The Following

<b>★ Your Bot :</b> [{botname}](t.me/{botuname})
<b>★ From Channel :</b> <code>{from_chat}<>
<b>★ To Channel :</b> <code>{to_chat}</code>
<b>★ Skip Messages :</b> <code>{skip}</code>

<i>° [{botname}](t.me/{botuname}) Must Be Admin In <b>Target Chat</b></i> (<code>{to_chat}</code>)
<i>° If The <b>Source Chat</b> Is Private Your Userbot Must Be Member Or Your Bot Must Be Admin In There Also</i>

<b>If The Above Is Checked Then The Yes Button Can Be Clicked</b>"""
