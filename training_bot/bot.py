import asyncio
from aiogram import Bot

from config import TOKEN
from hand import dp

bot = Bot(token=TOKEN)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
