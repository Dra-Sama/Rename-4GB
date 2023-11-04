import os 
from config import *
from pyrogram import Client, filters
from pyrogram.types import ParseMode 
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
        f"<b>🌟 Total Users:</b> {total_user()}<br>"
        f"<b>🤖 Bot:</b> <a href='https://t.me/Wizard_Bots'>Wizard Bots</a><br>"
        f"<b>👤 Creator:</b> <a href='https://t.me/cant_think_1'>Tenjiku</a><br>"
        f"<b>📚 Language:</b> Python3<br>"
        f"<b>📦 Library:</b> Pyrogram<br>"
        f"<b>🖥️ Server:</b> VPS Server<br>"
        f"<b>📂 Total Renamed Files:</b> {total_rename}<br>"
        f"<b>💽 Total Size Renamed:</b> {humanbytes(int(total_size))}",
        quote=True,
    )



