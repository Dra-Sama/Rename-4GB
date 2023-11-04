import os 
from config import *
from pyrogram import Client, filters
token = TOKEN
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(
    f"🌟 *Total User:* {total_user()}\n"
    f"🤖 *Bot:* @Wizard_Bots\n"
    f"👤 *Creator:* @cant_think_1\n"
    f"📚 *Language:* Python3\n"
    f"📦 *Library:* Pyrogram\n"
    f"🖥️ *Server:* VPS Server\n"
    f"📂 *Total Renamed Files:* {total_rename}\n"
    f"💽 *Total Size Renamed:* {humanbytes(int(total_size))}",
    quote=True,
    parse_mode=ParseMode.MARKDOWN
)

