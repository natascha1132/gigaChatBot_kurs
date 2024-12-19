import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from functools import partial
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from database import database
from globals import database, MainStates
from handlers.handler import rewrite_text_handler, analyze_text_handler, summarize_text_handler
from handlers.main_menu import handle_main_menu
from keyboards.key_words import main_menu
from handlers import user_hand
from keyboards.set_menu import set_main_menu
# from aiogram.client.session.aiohttp import AiohttpSession
from config_data.config import Config, load_config


# session = AiohttpSession(proxy="http://89.145.162.81:1080")


# Основная функция запуска
async def main():
    # Логирование
    logging.basicConfig(level=logging.INFO)

    # Загружаем конфиг в переменную config
    config: Config = load_config()


    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Регистрация команд
    dp.message.register(partial(user_hand.start_command, main_menu=main_menu, database=database),
                        Command(commands=["start"]))
    dp.message.register(user_hand.help_command, Command(commands=["help"]))
    dp.message.register(user_hand.admin_command, Command(commands=["admin"]))

    # Регистрация обработчиков состояний
    dp.message.register(handle_main_menu, StateFilter(None))# Обработка главного меню

    dp.message.register(rewrite_text_handler, StateFilter(MainStates.waiting_for_text_rewrite))
    dp.message.register(analyze_text_handler, StateFilter(MainStates.waiting_for_text_analysis))
    dp.message.register(summarize_text_handler, StateFilter(MainStates.waiting_for_text_summary))

    #Запуск опроса обновлений
    await set_main_menu(bot)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
