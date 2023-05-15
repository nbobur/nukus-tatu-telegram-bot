from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menuKeyStd = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🏛 Universitet haqida', callback_data="univer2")],
        [InlineKeyboardButton(text="🤵‍♂️🤵‍♀️Hodimlar bilan tanishish va Xabar yuborish", callback_data="tanishuv")],
        [InlineKeyboardButton(text="📨 Savol Javob", callback_data='faq2')],
        [InlineKeyboardButton(text="🌐 HEMIS Platformasi", url="https://student.tatunf.uz/dashboard/login")],
        [InlineKeyboardButton(text='🧑‍💻 Adminga Murojat', callback_data="murojat")],
        [InlineKeyboardButton(text='🔍 Qudiruv', switch_inline_query_current_chat=""),
            InlineKeyboardButton(text='➡️ Ulashish', switch_inline_query="Ajoyib bot")],
    ]
)
tugma2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Batafsil", url="https://tatunf.uz/#"),
         InlineKeyboardButton(text="Manzil", url="https://goo.gl/maps/oEQfXGajMbS2QYUMA")],
        [InlineKeyboardButton(text="🔙Ortga", callback_data="cancel2")]
    ]
)
