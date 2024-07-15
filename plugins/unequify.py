import re
from database import db
from config import temp
from .test import CLIENT, start_clone_bot
from pyrogram import Client, filters
from pyropatch.utils import unpack_new_file_id
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CLIENT = CLIENT()
COMPLETED_BTN = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('📢 Updates', url='https://t.me/Madflix_Bots')],
        [InlineKeyboardButton('💬 Support', url='https://t.me/MadflixBots_Support')]
    ]
)

CANCEL_BTN = InlineKeyboardMarkup([[InlineKeyboardButton('✖️ Cancel ✖️', 'terminate_frwd')]])

class Translation:
    DUPLICATE_TEXT = """
    ╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
    ║╭━━━━━━━━━━━━━━━➣
    ║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
    ║┃
    ║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code>
    ║╰━━━━━━━━━━━━━━━➣
    ╚════❰ {} ❱══❍⊱❁۪۪
    """

@Client.on_message(filters.command("unequify") & filters.private)
async def unequify(client, message):
    user_id = message.from_user.id
    temp.CANCEL[user_id] = False
    
    if temp.lock.get(user_id) and str(temp.lock.get(user_id)) == "True":
        return await message.reply("Please Wait Until Previous Task Complete")

    _bot = await db.get_bot(user_id)
    if not _bot or _bot['is_bot']:
        return await message.reply("Need Userbot To Fo This Process. Please Add A Userbot Using /settings")

    target = await client.ask(user_id, text="Forward The Last Message From Target Chat Or Send Last Message Link.\n/cancel - To Cancel This Process")
    if target.text.startswith("/"):
        return await message.reply("Process Cancelled !")
    elif target.text:
        regex = re.compile(r"(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
        match = regex.match(target.text.replace("?single", ""))
        if not match:
            return await message.reply('Invalid Link')
        chat_id = match.group(4)
        last_msg_id = int(match.group(5))
        if chat_id.isnumeric():
            chat_id = int("-100" + chat_id)
    elif fromid.forward_from_chat.type in ['channel', 'supergroup']:
        last_msg_id = target.forward_from_message_id
        chat_id = target.forward_from_chat.username or target.forward_from_chat.id
    else:
        return await message.reply_text("Invalid !")

    confirm = await client.ask(user_id, text="Send /yes To Start The Process And /no To Cancel This Process")
    if confirm.text.lower() == '/no':
        return await confirm.reply("Process Cancelled !")

    sts = await confirm.reply("Processing..")

    try:
        bot = await start_clone_bot(CLIENT.client(_bot))
    except Exception as e:
        print(f"Error in start_clone_bot: {e}")
        return await sts.edit(e)

    try:
        k = await bot.send_message(chat_id, text="testing")
        await k.delete()
    except Exception as e:
        print(f"Error sending test message: {e}")
        await sts.edit(f"Please Make Your [Userbot](t.me/{_bot['username']}) Admin In Target Chat With Full Permissions")
        return await bot.stop()

    MESSAGES = []
    DUPLICATE = []
    total = deleted = 0
    temp.lock[user_id] = True

    print("Started processing messages")

    try:
        await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "Progressing"), reply_markup=CANCEL_BTN)
        async for message in bot.search_messages(chat_id=chat_id, filter="document"):
            print(f"Processing message ID: {message.message_id}")

            if temp.CANCEL.get(user_id) == True:
                await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "Cancelled"), reply_markup=COMPLETED_BTN)
                return await bot.stop()

            try:
                file = message.document
                file_id = unpack_new_file_id(file.file_id)
                print(f"File ID: {file_id}")
            except AttributeError as e:
                print(f"AttributeError: {e}")
                continue  # Skip this message

            if file_id in MESSAGES:
                DUPLICATE.append(message.id)
            else:
                MESSAGES.append(file_id)

            total += 1
            if total % 10000 == 0:
                await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "Progressing"), reply_markup=CANCEL_BTN)
            if len(DUPLICATE) >= 100:
                await bot.delete_messages(chat_id, DUPLICATE)
                deleted += 100
                await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "Progressing"), reply_markup=CANCEL_BTN)
                DUPLICATE = []

        if DUPLICATE:
            await bot.delete_messages(chat_id, DUPLICATE)
            deleted += len(DUPLICATE)

    except Exception as e:
        print(f"Error during message processing: {e}")
        temp.lock[user_id] = False
        await sts.edit(f"**Error**\n\n`{e}`")
        return await bot.stop()

    temp.lock[user_id] = False
    await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "Completed"), reply_markup=COMPLETED_BTN)
    await bot.stop()
