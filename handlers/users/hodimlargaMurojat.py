from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram import types

from keyboards.default.Keymenu import menu
from keyboards.inline.murojatButton import javob_button
from loader import dp, dbBaza, bot



@dp.callback_query_handler(Text(startswith="hodim_id=", ignore_case=True))
async def asmindan_javob(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        text="Sizning habariningi <b>🦹🏻‍♂️ANANIM</b> tarzda yuborilib barcha ma'lumotingiz sir tutiladi."
             "\nAgar o'zingizni tanitmoqchi bo'lsangiz o'zingiz haqingizda ham ma'lumot kiriting!",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=types.ParseMode.HTML)
    await state.set_state("hodimga_xabar")
    id = call.data
    id = id[9:]
    print(id)
    await state.update_data(
        {"hodim_id": id}
    )
    # await state.set_state("admindanjavob")

    # await call.message.answer("✉️ Foydalanuvchiga xabar yuborish:", reply_markup=ReplyKeyboardRemove())
    # await call.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup())


@dp.message_handler(state="hodimga_xabar")
async def xabar_yuborish_funk(msg: types.Message, state: FSMContext):

    user_id = f"user_id={msg.from_user.id}"

    data = await state.get_data()
    hodim_id = data.get("hodim_id")

    try:
        await bot.send_message(chat_id=hodim_id, text=f"<b>📬 XABAR</b>\n{msg.text}",
                               reply_markup=javob_button(user_id),
                               parse_mode=types.ParseMode.HTML)
        await msg.answer("Xabar yuborildi ✅", reply_markup=menu)
    except Exception as err:
        await msg.answer("Xabar yuborilmadi ❌", reply_markup=menu)

    await state.finish()

@dp.callback_query_handler(Text(startswith="user_id=", ignore_case=True))
async def userga_javob(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup())

    text = "✉️ Javob yuborish:"

    await call.message.answer(text=text, reply_markup=ReplyKeyboardRemove())

    id = call.data
    id = id[8:]
    print(call.from_user.id)
    await state.update_data(
        {call.from_user.id: id}
    )

    await state.set_state("userga_javob")

@dp.message_handler(state="userga_javob")
async def userga_javob_yuborish(msg: types.Message, state: FSMContext):

    data = await state.get_data()
    id = data.get(msg.from_user.id)

    try:
        await bot.send_message(chat_id=id,
                               text=f"<b>✉️ Hodimdan xat:</b>\n{msg.text}",
                               parse_mode=types.ParseMode.HTML)

        await msg.answer("Xabar yuborildi ✅", reply_markup=menu)

    except Exception as err:
        await msg.answer("Xabar yuborilmadi ❌", reply_markup=menu)

    await state.finish()