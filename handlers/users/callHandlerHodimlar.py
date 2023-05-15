from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram import types

from data.config import ADMINS
from keyboards.inline.murojatButton import button_hodimlar
from loader import dp, dbBaza, bot


@dp.callback_query_handler(text="direktor")
async def direktor_funk(call: CallbackQuery):

    list = dbBaza.select_hodimlar(kalit="direktor")
    data_id_hodim = f"hodim_id={list[0]}"
    rasmURL = list[2]
    info = list[3]

    await call.message.answer_photo(photo=rasmURL,
                                    reply_markup=button_hodimlar(data_id_hodim),
                                    caption=info,
                                    parse_mode=types.ParseMode.HTML)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="boshqa")
async def direktor_funk(call: CallbackQuery):

    list = dbBaza.select_hodimlar(kalit="boshqa")
    data_id_hodim = f"hodim_id={list[0]}"
    rasmURL = list[2]
    info = list[3]

    await call.message.answer_photo(photo=rasmURL,
                                    reply_markup=button_hodimlar(data_id_hodim),
                                    caption=info,
                                    parse_mode=types.ParseMode.HTML)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="bo'lim")
async def direktor_funk(call: CallbackQuery):

    list = dbBaza.select_hodimlar(kalit="bo'limlar")
    data_id_hodim = f"hodim_id={list[0]}"
    rasmURL = list[2]
    info = list[3]

    await call.message.answer_photo(photo=rasmURL,
                                    reply_markup=button_hodimlar(data_id_hodim),
                                    caption=info,
                                    parse_mode=types.ParseMode.HTML)
    await call.answer(cache_time=60)