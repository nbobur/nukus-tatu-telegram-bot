from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

FAQmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="1"),
         InlineKeyboardButton(text="2", callback_data="2"),
         InlineKeyboardButton(text="3", callback_data="3"),
         InlineKeyboardButton(text="4", callback_data="4"),
         InlineKeyboardButton(text="5", callback_data="5")],
        [InlineKeyboardButton(text="Boshqa savollar", callback_data="next")],
        [InlineKeyboardButton(text="🔙Ortga", callback_data="cancel3")]
    ]
)

FAQmenuStd = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="1a"),
         InlineKeyboardButton(text="2", callback_data="2a"),
         InlineKeyboardButton(text="3", callback_data="3a"),
         InlineKeyboardButton(text="4", callback_data="4a"),
         InlineKeyboardButton(text="5", callback_data="5a")],
        [InlineKeyboardButton(text="Boshqa savollar", callback_data="next2")],
        [InlineKeyboardButton(text="🔙Ortga", callback_data="cancel4")]
    ]
)
