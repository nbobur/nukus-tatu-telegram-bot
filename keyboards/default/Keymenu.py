from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='👨‍💻Abiturient'),
            KeyboardButton(text='👨‍🎓Talaba')],
    ],
    resize_keyboard=True
)