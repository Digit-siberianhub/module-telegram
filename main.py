import asyncio
import logging

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked

import credentials.telegram as tg 
from app.handlers import register_handlers, checking_updates, db

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
)

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot, loop=asyncio.get_event_loop())
register_handlers(dp)


async def scheduled(wait_for):
    # Функции возможно не будет
    while True:
        # сбор статы
        # отправка в ядро
        await asyncio.sleep(wait_for)


if __name__ == '__main__':
    dp.loop.create_task(scheduled(60*60))
    executor.start_polling(dp, skip_updates=True)