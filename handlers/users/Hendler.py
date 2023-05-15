from aiogram.types import Message
from data import textlar, photoURL
from keyboards.inline.KeyAbt import menuKeyAbt
from keyboards.inline.KeyStd import menuKeyStd
from loader import dp

##########     Bosh menyu       ####################

@dp.message_handler(text_contains="👨‍💻Abiturient")
async def select_category(message: Message):
    await message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.abtText, reply_markup=menuKeyAbt)

@dp.message_handler(text_contains="‍🎓Talaba")
async def select_category(message: Message):
    await message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.stdText, reply_markup=menuKeyStd)

