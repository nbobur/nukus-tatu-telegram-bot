from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menuKeyAbt = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🏛 Universitet haqida", callback_data="univer1")],
        [InlineKeyboardButton(text="📚 Yo'nalishlar", callback_data="yonalish")],
        [InlineKeyboardButton(text='📊 Kirish ballar', url="https://tatunf.uz/index.php?r=site%2Fmagliwmat&id=400")],

        [InlineKeyboardButton(text="📨 Savol Javob", callback_data='faq')],
        [InlineKeyboardButton(text="🧑‍💻 Adminga Murojat", callback_data='murojat')],
        [InlineKeyboardButton(text='🔍 Qudiruv', switch_inline_query_current_chat=""),
         InlineKeyboardButton(text='➡️ Ulashish', switch_inline_query="Ajoyib bot")],
    ]
)
tugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Batafsil", url="https://tatunf.uz/#"),
         InlineKeyboardButton(text="Manzil", url="https://goo.gl/maps/oEQfXGajMbS2QYUMA")],
        [InlineKeyboardButton(text="🔙Ortga", callback_data="cancel")]
    ]
)
menuyonalish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Batafsil", url="https://tatunf.uz/index.php?r=site%2Fmagliwmat&id=36")],
        [InlineKeyboardButton(text="🔙Ortga", callback_data="ortgayonalish")]
    ]
)
