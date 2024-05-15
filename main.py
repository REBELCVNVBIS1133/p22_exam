import asyncio
import logging
import sys
from email import message
from os import getenv
from typing import Iterable

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery, message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder
import os

# from redisdict import RedisDict

load_dotenv('.env')
TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()
bot = Bot(token=TOKEN)
router = Router()



@dp.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def group(message: Message):
    await message.answer('👋SALOM! GURUHIMIZGA XUSH KELIBSIZ🔯✅')





async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())