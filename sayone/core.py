from telethon import TelegramClient, events, Button
from core.loader import load_all_modules
import config
import asyncio
import json

async def main():
    client = TelegramClient("SayOne", config.API_ID, config.API_HASH)
    await client.start()
    print("Sayone Started!")
    
UserbotFolder = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(UserbotFolder, "sayone", "bcfg", "bot.json")

# Загрузка настроек
def load_config():
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "modules": {"enabled": True},
            "userbot": {"prefix": ".", "logs": True}
        }

# Сохранение настроек
def save_config(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

@client.on(events.NewMessage(pattern=r'\.settings'))
async def settings_handler(event):
    buttons = [
        [Button.inline("📦 Модули", b"modules_settings")],
        [Button.inline("🤖 Юзербот", b"userbot_settings")],
        [Button.inline("❌ Закрыть", b"close_settings")]
    ]
    await event.respond("**SayOne. Выбор категории настроек:**", buttons=buttons)

@client.on(events.CallbackQuery(data=b"modules_settings"))
async def modules_settings(event):
    config = load_config()
    buttons = [
        [Button.inline(f"📦 Модули: {'ON' if config['modules']['enabled'] else 'OFF'}", b"toggle_modules")],
        [Button.inline("🔙 Назад", b"back_to_main")]
    ]
    await event.edit("**⚙ Настройки модулей:**", buttons=buttons)

@client.on(events.CallbackQuery(data=b"toggle_modules"))
async def toggle_modules(event):
    config = load_config()
    config["modules"]["enabled"] = not config["modules"]["enabled"]
    save_config(config)
    await event.answer(f"Модули: {'ON' if config['modules']['enabled'] else 'OFF'}")
    await modules_settings(event)

# ====== НАСТРОЙКИ ЮЗЕРБОТА ====== #
@client.on(events.CallbackQuery(data=b"userbot_settings"))
async def userbot_settings(event):
    config = load_config()
    buttons = [
        [Button.inline(f"📝 Префикс: {config['userbot']['prefix']}", b"change_prefix")],
        [Button.inline(f"📊 Логи: {'ON' if config['userbot']['logs'] else 'OFF'}", b"toggle_logs")],
        [Button.inline("🔙 Назад", b"back_to_main")]
    ]
    await event.edit("**⚙ Настройки юзербота:**", buttons=buttons)

@client.on(events.CallbackQuery(data=b"toggle_logs"))
async def toggle_logs(event):
    config = load_config()
    config["userbot"]["logs"] = not config["userbot"]["logs"]
    save_config(config)
    await event.answer(f"Логи: {'ON' if config['userbot']['logs'] else 'OFF'}")
    await userbot_settings(event)

@client.on(events.CallbackQuery(data=b"change_prefix"))
async def change_prefix(event):
    await event.answer("ℹ Введите новый префикс (например, '!')")
    

# ====== ЗАКРЫТИЕ И ВОЗВРАТ ====== #
@client.on(events.CallbackQuery(data=b"close_settings"))
async def close_settings(event):
    await event.delete()

@client.on(events.CallbackQuery(data=b"back_to_main"))
async def back_to_main(event):
    await settings_handler(event)
    # Авто-загрузка модулей
    load_all_modules(client)
    
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
    
