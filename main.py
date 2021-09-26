import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked

from service.credentials import TG_TOKEN
from service.core_api import CoreAPI


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
)

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)
core = CoreAPI(
    'Телеграм', 
    'Модуль для работы с телеграмм чатами',
    'Социальное'
)


@dp.message_handler()
async def scan_messages(message: types.Message):
    rating = len(message.text) / 10
    if rating < 1:
        rating = -2
    core.send_data(message.from_user.username, rating)


if __name__ == '__main__':
    logging.info('TELEGRAM MODULE STARTED')
    core.register_module()
    executor.start_polling(dp, skip_updates=True)
