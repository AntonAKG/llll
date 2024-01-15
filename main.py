import asyncio
from aiogram import Bot, Dispatcher

from logging import basicConfig, INFO

from bot import router


async def on_startup():
    print('Bot online')


async def main():
    basicConfig(level=INFO)

    bot = Bot("6809484776:AAHdS7vQXrAvYipYgYQnI_3Y73Tcy7_9ZN0", parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(
        router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=await on_startup())


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
