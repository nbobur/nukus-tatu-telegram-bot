import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.Keymenu import menu

from loader import dp, dbUsers, bot

@dp.message_handler(CommandStart(), user_id=ADMINS)
async def bot_start_admin(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    language = message.from_user.language_code
    try:
        dbUsers.add_user(id=user_id, name=name, language=language)
    except sqlite3.IntegrityError as err:
        pass

    # cout bazadagi foydalanuvchilar soni
    count = dbUsers.count_users()[0]

    text = f"Salom, {message.from_user.full_name}!\nHozir Botdan <b>{count}</b> ta odam foydalanmoqda."

    await message.answer(text, reply_markup=menu, parse_mode=types.ParseMode.HTML)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    language = message.from_user.language_code
    # Foydalanuvchini bazaga qo'shish
    try:
        dbUsers.add_user(id=user_id, name=name, language=language)
        # Foydalanuvchiga xabar yuborish
        await message.answer(
            f"Assalomu aleykum {message.from_user.full_name}, TATU Nukus filiali rasmiy botiga hush kelibsiz",
            reply_markup=menu)

        # Adminga xabar berish
        count = dbUsers.count_users()[0]
        # cout foydalanuvchilar soni
        msg = f"{name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:

        await message.answer(
            f"Assalomu aleykum {message.from_user.full_name}, TATU Nukus filiali rasmiy botiga hush kelibsiz",
            reply_markup=menu)
