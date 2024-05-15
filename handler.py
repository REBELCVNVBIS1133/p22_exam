from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.redis import RedisStorage2


bot = Bot(token="TOKEN", parse_mode=types.ParseMode.HTML)
storage = RedisStorage2()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['msg'])
async def send_message_to_group(message: types.Message):

    await storage.set(f"messages:{message.chat.id}:{message.from_user.username}", message.text)
    await message.reply("Xabar saqlandi!")


@dp.message_handler(commands=['count'])
async def count_messages_in_group(message: types.Message):

    count = await storage.count(f"messages:{message.chat.id}:{message.from_user.username}")
    await message.reply(f"{message.from_user.username} ga {count} ta xabar yozilgan")

if __name__ == '__main__':
    import asyncio
    from aiogram import executor

    loop = asyncio.get_event_loop()
    loop.create_task(storage.redis.flushdb())
    executor.start_polling(dp, skip_updates=True)
