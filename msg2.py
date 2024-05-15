from aiofiles import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.redis import RedisStorage2
from dotenv import load_dotenv

from main import bot

load_dotenv('.env')
TOKEN = os.getenv("BOT_TOKEN")
storage = RedisStorage2()

dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['msg'])
async def count_messages_for_username(message: types.Message):
    chat_id = message.chat.id
    username = message.text.split(" ")[1]
    messages = await storage.redis.keys(f"messages:{chat_id}:{username}:*")
    count = len(messages)
    await message.answer(f"{username} ga tegishli jami {count} ta xabar yozilgan")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
