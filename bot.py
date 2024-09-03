import requests
import asyncio
from telegram import Bot

# Налаштування Telegram
TELEGRAM_BOT_TOKEN = '7224705050:AAFkwraUqV77oSbK3FvAvCm1OPpTaFLyyNE'
TELEGRAM_CHAT_ID = '355542941'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# URL API для моніторингу
# Замініть на фактичний URL API
API_URL = 'https://www.soe.com.ua/includes/vidklyuchennya_srv_CURL.php?cmd=get_user_disconnections_image_api&cherga=1'
CHECK_INTERVAL = 60  # Інтервал перевірки в секундах

# Зберігаємо попередній стан даних
previous_data = None


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Помилка запиту до {url}: {e}")
        return None


async def send_telegram_message(chat_id, message):
    try:
        await bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Помилка відправки повідомлення в Telegram: {e}")


async def monitor_api():
    global previous_data

    while True:
        current_data = fetch_data(API_URL)

        if current_data:
            # Перевіряємо, чи є зміни
            if previous_data and previous_data['data']['modified_on'] != current_data['data']['modified_on']:
                message = (
                    f"Дата модифікації: {current_data['data']['modified_on']}"
                )
                print("Знайдено зміни на сайті!")
                await send_telegram_message(TELEGRAM_CHAT_ID, message)
            else:
                print("Змін не знайдено")

            # Оновлюємо попередні дані
            previous_data = current_data
        else:
            print("Не вдалося отримати дані з API")

        # Затримка між перевірками
        await asyncio.sleep(CHECK_INTERVAL)


# Запуск моніторингу
asyncio.run(monitor_api())
