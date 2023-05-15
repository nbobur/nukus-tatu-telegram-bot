from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def button(id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✉️ Javob yuborish", callback_data=id)
            ]
        ]
    )

def button_hodimlar(hodim_data: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✉️ Xabar yuborish", callback_data=hodim_data)
            ]
        ]
    )

def javob_button(user_data: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✉️ Javob yuborish", callback_data=user_data)
            ]
        ]
    )



