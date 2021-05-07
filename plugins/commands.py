#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('📜𝐒𝐮𝐩𝐩𝐨𝐫𝐭', url='https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ'),
        InlineKeyboardButton('𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥♻️', url='https://t.me/Mo_Tech_YT')
    ],[
        InlineKeyboardButton('💡𝐒𝐨𝐮𝐜𝐞𝐂𝐨𝐝𝐞💡', url='https://github.com/MRK-YT/File-Auto-Forword-Bot')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('𝐜𝐥𝐨𝐬𝐞 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.HELP_TXT,
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('💡𝐒𝐨𝐮𝐜𝐞𝐂𝐨𝐝𝐞', url='https://github.com/MRK-YT/File-Auto-Forword-Bot'),
        InlineKeyboardButton('𝐜𝐥𝐨𝐬𝐞🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        parse_mode="html"
    )

        
