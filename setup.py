import asyncio
from janusbot.bot.telegram_bot import telegram_bot

async def main():
    await telegram_bot()

if __name__ == "__main__":
    asyncio.run(main())