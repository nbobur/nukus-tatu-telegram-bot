from aiogram import types
from loader import dp

@dp.inline_handler()
async def search_quare(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="dk001",
                title="Toshkent axborot texnologiyalari universiteti Nukus filiali direktori",
                input_message_content=types.InputTextMessageContent(
                    message_text="Toshkent axborot texnologiyalari universiteti Nukus filiali direktori"
                        "\nKaipbergenov Batirbek Tulepbergenovich "
                        "\nTelefon 8361) 222-49-10 "
                        "\nFaks (8361) 222-49-10 "
                ),
                thumb_url="https://tatunf.uz/images/stories/people/kaipbergenov.jpg",
                description="Toshkent axborot texnologiyalari universiteti Nukus filiali direktori"
            ),
            types.InlineQueryResultArticle(
                id="dk00243",
                title="Yadgarov Sherzod Abdullaevich",
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali O'quv-metodik bo'limi boshlig'i</b> "
                ),
                thumb_url="https://tatunf.uz/images/stories/people/sherzod.jpg",
                description="Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali O'quv-metodik bo'limi boshlig'i"
            ),
            types.InlineQueryResultArticle(
                id="dk0033",
                title="Seytkamalov Xayratdin Maulenovich",
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>Toshkent axborot texnologiyalari universiteti Nukus filiali o’quv va tarbiyaviy ishlar bo’yicha direktor o’rinbosari</b> "
                ),
                thumb_url="https://tatunf.uz/images/stories/people/seytkamalov_q.jpg",
                description="Toshkent axborot texnologiyalari universiteti Nukus filiali o’quv va tarbiyaviy ishlar bo’yicha direktor o’rinbosari",
            ),
            types.InlineQueryResultArticle(
                id="dk003333",
                title="Utewliev Nietbay Utewlievich",
                input_message_content=types.InputTextMessageContent(
                    message_text="Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali Dasturiy injinirin kafedrasi mudiri, fizika-matematika fanlari doktori, professor"
                ),
                thumb_url="https://tatunf.uz/images//stories/people/utewliev.jpg",
                description="Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali Dasturiy injiniring kafedrasi mudiri, fizika-matematika fanlari doktori, professor",
            ),
            types.InlineQueryResultArticle(
                id="dk00323",
                title="Seytkamalov Xayratdin Maulenovich",
                input_message_content=types.InputTextMessageContent(
                    message_text="<b>Toshkent axborot texnologiyalari universiteti Nukus filiali ilmiy ishlar va innovatsiyalar bo'yicha direktor o’rinbosari</b> "
                ),
                thumb_url="https://tatunf.uz/images/stories/people/aytmuratovb.jpg",
                description="Toshkent axborot texnologiyalari universiteti Nukus filiali ilmiy ishlar va innovatsiyalar bo'yicha direktor o’rinbosari",
            )
        ]
    )
