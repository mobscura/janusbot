from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from conf import config
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def command_start(message: types.Message) -> None:
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Hello, world!", parse_mode="html")

@dp.message()
async def text_receiver(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, message.text, parse_mode="html")
    
@dp.callback_query()
async def inlines(c: types.CallbackQuery):
    chat_id = c.message.chat.id
    message_id = c.message.message_id
    data = c.data or ""
    parts = data.split()
    cmd = parts[0]
    args = parts[1:]
    if cmd in {"config"}:
        await bot.send_message(chat_id, "Hello, world!", parse_mode="html")
    
async def telegram_bot() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)