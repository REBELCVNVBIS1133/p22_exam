

@dp.message_handler(commands=['msg'])
async def count_messages_in_chat(message: types.Message):
    chat_id = message.chat.id
    messages = await storage.redis.keys(f"messages:{chat_id}:*")
    count = len(messages)
    await message.answer(f"Jami {count} ta xabar yozilgan")


