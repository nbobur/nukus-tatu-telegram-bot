from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-qavat
menuTanishuv = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📂 Direktsiya", callback_data="direktor")],
        [InlineKeyboardButton(text="📂 Bugalteriya", callback_data="bugalter")],
        [InlineKeyboardButton(text="📂 Fakultetlar", callback_data="fakultet")],
        [InlineKeyboardButton(text="📂 Kafedralar", callback_data="kafedra")],
        [InlineKeyboardButton(text="📂 Bo'limlar", callback_data="bo'lim")],
        [InlineKeyboardButton(text="📂 Mas'ullar", callback_data="masullar")],
        [InlineKeyboardButton(text="📂 Markaz va sektorlar", callback_data="markaz")],
        [InlineKeyboardButton(text="📂 Boshqa hodimlar", callback_data="boshqa")],

        [InlineKeyboardButton(text='🔍 Qudiruv', switch_inline_query_current_chat=""),
         InlineKeyboardButton(text='➡️ Ulashish', switch_inline_query="Ajoyib bot")],
        [InlineKeyboardButton(text="🔙 Ortga", callback_data="ortgaTanishuv")],
    ]
)
menuFakultet = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📂 T.T VA KASB TA’LIMI",
                              callback_data="ttvk")],
        [InlineKeyboardButton(text="📂 KOMPYUTER INJINIRINGI", callback_data="kif")],
        [InlineKeyboardButton(text="🔙 Ortga", callback_data="ortgaFak")],

    ]
)
menuKafedra = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📂 D.I.M.M", callback_data="dimm")],
        [InlineKeyboardButton(text="📂 Axborot texnologiyalari", callback_data="dimm")],
        [InlineKeyboardButton(text="📂 Kompyuter tizimlari", callback_data="dimm")],
        [InlineKeyboardButton(text="📂 O'zbek tili va chet tillar", callback_data="dimm")],
        [InlineKeyboardButton(text="📂 TEL. injineringi", callback_data="dimm")],
        [InlineKeyboardButton(text="📂 Axborot xavfsizligi", callback_data="dimm")],
        [InlineKeyboardButton(text="📂 Tabiiy va aniq fanlar", callback_data="dimm")],
        [InlineKeyboardButton(text="📂 Raqamli iqtisodiyot", callback_data="dimm")],
        [InlineKeyboardButton(text='🔍 Qudiruv', switch_inline_query_current_chat="kafedra"),
         InlineKeyboardButton(text='➡️ Ulashish', switch_inline_query="Ajoyib bot")],
        [InlineKeyboardButton(text="🔙 Ortga", callback_data="ortgaKaf")]
    ]
)
