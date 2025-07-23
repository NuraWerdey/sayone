from telethon import TelegramClient
from core.loader import load_all_modules
import config
import asyncio

async def main():
    client = TelegramClient("SayOne", config.API_ID, config.API_HASH)
    await client.start()
    print("Sayone Started!")
    
    # Авто-загрузка модулей
    load_all_modules(client)
    
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
