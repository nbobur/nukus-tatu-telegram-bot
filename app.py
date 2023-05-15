from aiogram import executor

from loader import dp, dbBaza, dbUsers
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

    # Ma'lumotler ba'zasini yaratamiz
    try:
        dbUsers.create_table_hodimlar()
        dbUsers.create_table_user()
    except Exception as err:
        pass

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


