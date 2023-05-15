from aiogram.types import CallbackQuery
from data import textlar, photoURL, FAQabt, FAQstd
from keyboards.inline.Hodimlar import menuTanishuv, menuFakultet, menuKafedra
from keyboards.inline.KeyAbt import tugma, menuyonalish
from keyboards.inline.KeyStd import menuKeyStd, tugma2
from keyboards.inline.menuFAQ import FAQmenu, FAQmenuStd
from loader import dp

# ###########     Abiturient bo'limi      #########################

@dp.callback_query_handler(text="univer1")
async def process_help_command(call: CallbackQuery):
    await call.message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.univertext, reply_markup=tugma)
    await call.answer(cache_time=1)


@dp.callback_query_handler(text="cancel")
async def cancel_call(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=1)

# ############      Talaba Bo'limi       ###########################

@dp.callback_query_handler(text="univer2")
async def process_help_command(call: CallbackQuery):
    await call.message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.univertext, reply_markup=tugma2)
    await call.answer(cache_time=1)

# #############     bosh menu uchun         ############################

@dp.callback_query_handler(text="cancel2")
async def cancel_call(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=1)

@dp.callback_query_handler(text="tanishuv")
async def call_tanishuv(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.bolimlar, reply_markup=menuTanishuv)

@dp.callback_query_handler(text="ortgaTanishuv")
async def cancel_call(call: CallbackQuery):
    await call.message.edit_caption(caption=textlar.bolimlar, reply_markup=menuKeyStd)
    await call.answer(cache_time=1)


# ###########    Fakultet bo'limi    ##############################

@dp.callback_query_handler(text="fakultet")
async def call_tanishuv(call: CallbackQuery):
    await call.message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.bolimlar, reply_markup=menuFakultet)
    await call.answer(cache_time=1)

@dp.callback_query_handler(text="ortgaFak")
async def cancel_call(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menuTanishuv)
    await call.answer(cache_time=1)


# #########   Kafedra bo'limi    ###########################################

@dp.callback_query_handler(text="kafedra")
async def call_tanishuv(call: CallbackQuery):
    await call.message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.bolimlar, reply_markup=menuKafedra)

@dp.callback_query_handler(text="ortgaKaf")
async def cancel_call(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menuTanishuv)
    await call.answer(cache_time=1)

@dp.callback_query_handler(text="yonalish")
async def call_yonalish(call: CallbackQuery):
    await call.message.answer_photo(photo=photoURL.univerPhoto, caption=textlar.yonalishlar, reply_markup=menuyonalish)

@dp.callback_query_handler(text="ortgayonalish")
async def cancel_call(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=1)



# ###        FAQ Abiturient hendler          ####################################

@dp.callback_query_handler(text="faq")
async def call_yonalish(call: CallbackQuery):
    await call.message.answer_photo(photo=photoURL.FAQ, caption=FAQabt.SavollarABT, reply_markup=FAQmenu)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="cancel3")
async def cancel_call(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=1)

@dp.callback_query_handler(text="1")
async def call_faq1(call: CallbackQuery):
    await call.message.answer(text=FAQabt.javob1)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="2")
async def call_faq2(call: CallbackQuery):
    await call.message.answer(text=FAQabt.javob2)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="3")
async def call_faq3(call: CallbackQuery):
    await call.message.answer(text=FAQabt.javob3)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="4")
async def call_faq4(call: CallbackQuery):
    await call.message.answer(text=FAQabt.javob4)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="5")
async def call_5(call: CallbackQuery):
    await call.message.answer(text=FAQabt.javob5)
    await call.answer(cache_time=2)

# ########     FAQ Student hendler        ############################

@dp.callback_query_handler(text="faq2")
async def call_yonalish(call: CallbackQuery):
    await call.message.answer_photo(photo=photoURL.FAQ, caption=FAQabt.SavollarABT, reply_markup=FAQmenuStd)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="cancel4")
async def cancel_call(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=1)

@dp.callback_query_handler(text="1a")
async def call_faq1(call: CallbackQuery):
    await call.message.answer(text=FAQstd.answer1)
    await call.answer(cache_time=2)


@dp.callback_query_handler(text="2a")
async def call_faq2(call: CallbackQuery):
    await call.message.answer(text=FAQstd.answer2)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="3a")
async def call_faq3(call: CallbackQuery):
    await call.message.answer(text=FAQstd.answer3)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="4a")
async def call_faq4(call: CallbackQuery):
    await call.message.answer(text=FAQstd.answer4)
    await call.answer(cache_time=2)

@dp.callback_query_handler(text="5a")
async def call_5(call: CallbackQuery):
    await call.message.answer(text=FAQstd.answer5)
    await call.answer(cache_time=2)


@dp.callback_query_handler(text="bugalter")
@dp.callback_query_handler(text="fakultet")
@dp.callback_query_handler(text="kafedra")
@dp.callback_query_handler(text="masullar")
@dp.callback_query_handler(text="markaz")
@dp.callback_query_handler(text="ttvk")
@dp.callback_query_handler(text="kif")
async def call_hend(call: CallbackQuery):
    await call.answer(text="Hodim Kiritilmagan")
    await call.answer(cache_time=1)





