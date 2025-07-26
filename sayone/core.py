from telethon import TelegramClient, events, Button
from core.loader import load_all_modules
import config
import asyncio
import json

async def main():
    client = TelegramClient("SayOne", config.API_ID, config.API_HASH)
    await client.start()
    print("Sayone Started!")

    # Загрузка/сохранение настроек
def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"auto_load": True, "security": False, "logs": True}

def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)
        
# Обработчик команды .settings
@client.on(events.NewMessage(pattern=r'\.settings'))
async def settings_handler(event):
    settings = load_settings()
    buttons = [
        [
            Button.inline(f"🔄 Автозагрузка: {'ON' if settings['auto_load'] else 'OFF'}", b"toggle_auto_load"),
            Button.inline(f"🔐 Безопасность: {'ON' if settings['security'] else 'OFF'}", b"toggle_security")
        ],
        [Button.inline("💾 Сохранить", b"save_settings")]
    ]
    await event.respond("⚙ **Настройки UserBot**", buttons=buttons)

# Обработчики кнопок
@client.on(events.CallbackQuery(data=b"toggle_auto_load"))
async def toggle_auto_load(event):
    settings = load_settings()
    settings["auto_load"] = not settings["auto_load"]
    save_settings(settings)
    await event.answer(f"Автозагрузка: {'ON' if settings['auto_load'] else 'OFF'}")
    await event.delete()

@client.on(events.CallbackQuery(data=b"toggle_security"))
async def toggle_security(event):
    settings = load_settings()
    settings["security"] = not settings["security"]
    save_settings(settings)
    await event.answer(f"Безопасность: {'ON' if settings['security'] else 'OFF'}")
    await event.delete()

@client.on(events.CallbackQuery(data=b"save_settings"))
async def save_settings_handler(event):
    await event.answer("✅ Настройки сохранены!")
    await event.delete()
    
    # Авто-загрузка модулей
    load_all_modules(client)
    
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
