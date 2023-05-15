
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types
from data.config import ADMINS
from keyboards.default.Keymenu import menu

from keyboards.inline.murojatButton import button
from loader import dp, bot



@dp.callback_query_handler(text="murojat")
async def murojar_funk(call: CallbackQuery, state: FSMContext):
    # photo = InputFile(path_or_bytesio="data/admin.jpg")
    # photo = Image.open("")
    text = "🧑‍💻 Adminga savolingiz bo'lsa yo'llashingiz mumkin."
    # await call.message.answer_photo(photo="photo", caption=text)
    await call.message.answer(text=text, reply_markup=ReplyKeyboardRemove())

    await state.set_state("admingamurojat")



@dp.message_handler(state="admingamurojat")
async def adminga_murojat(msg: types.Message, state: FSMContext):
    text=f"<b>✉️ Foudalanuvchidan Murojat:\n</b>{msg.text}"

    await msg.answer("Xabar yuborildi ✅", reply_markup=menu)

    id = f"id={msg.from_user.id}"

    await bot.send_message(chat_id=ADMINS[0], text=text,
                           reply_markup=button(id=id),
                           parse_mode=types.ParseMode.HTML)
    await state.finish()



@dp.callback_query_handler(Text(startswith="id=", ignore_case=True))
async def asmindan_javob(call: CallbackQuery, state: FSMContext):

    id = call.data
    id=id[3:]
    await state.update_data(
        {"id": id}
    )

    await state.set_state("admindanjavob")
    await call.message.answer("✉️ Foydalanuvchiga xabar yuborish:", reply_markup=ReplyKeyboardRemove())
    await call.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup())



@dp.message_handler(state="admindanjavob")
async def admindan_foydalanuvchiga_javob_yuborish(msg: types.Message, state: FSMContext):

    data = await state.get_data()
    user_id = data.get("id")

    text = f"<b>🧑‍💻 Admindan javob</b>\n{msg.text}"

    await bot.send_message(chat_id=user_id, text=text, parse_mode=types.ParseMode.HTML)
    await msg.answer(text="Xabar yuborildi! ✅", reply_markup=menu)

    await state.finish()