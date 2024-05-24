import os 
from config import *
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
token = TOKEN
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client, message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    await message.reply_text(
        f"<b>🌟 Total Users:</b> {total_user()}\n"
        f"<b>🤖 Bot:</b> <a href='https://t.me/Wizard_Bots'>Wizard Bots</a>\n"
        f"<b>👤 Creator:</b> <a href='https://t.me/Shanks_Kun'>Tenjiku</a>\n"
        f"<b>📚 Language:</b> Python3\n"
        f"<b>📦 Library:</b> Pyrogram\n"
        f"<b>🖥️ Server:</b> VPS Server\n"
        f"<b>📂 Total Renamed Files:</b> {total_rename}\n"
        f"<b>💽 Total Size Renamed:</b> {humanbytes(int(total_size))}",
        quote=True,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )



