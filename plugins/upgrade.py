from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit: **No LIMIT**
	Price 0
	
	**VIP**
        Donate Premium string and i will add you to premium"""
	keybord = InlineKeyboardMarkup([[ InlineKeyboardButton("ADMIN 🛂", url = "https://t.me/Shanks_Kun")]])
	await update.message.edit(text = text, reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit: **No LIMIT***
	Price 0
	
	**VIP **
        Donate Premium string and i will add you to premium"""
	keybord = InlineKeyboardMarkup([[ InlineKeyboardButton("ADMIN 🛂", url = "https://t.me/Shanks_kun")]])
	await update.message.edit(text = text, reply_markup = keybord)
