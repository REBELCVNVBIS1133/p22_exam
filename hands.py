from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.redis import RedisStorage2


bot = Bot(token="BOT_TOKEN", parse_mode=types.ParseMode.HTML)
storage = RedisStorage2()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(content_types=types.ContentType.ANY)
async def save_message_to_redis(message: types.Message):
    await storage.set(f"messages:{message.chat.id}:{message.message_id}", message.text)

if __name__ == '__main__':
    import asyncio
    from aiogram import executor

    loop = asyncio.get_event_loop()
    loop.create_task(storage.redis.flushdb())
    executor.start_polling(dp, skip_updates=True)

