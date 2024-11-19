import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция для получения случайного изображения кошки
def get_random_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        return None

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который отправляет случайные изображения кошек. Используйте команду /cat чтобы получить изображение.')

# Обработчик команды /cat
def cat(update: Update, context: CallbackContext) -> None:
    cat_image_url = get_random_cat_image()
    if cat_image_url:
        update.message.reply_photo(cat_image_url)
    else:
        update.message.reply_text('Не удалось получить изображение кошки. Попробуйте позже.')

def main():
    # Вставьте сюда ваш токен бота
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("cat", cat))

    # Запуск бота
    updater.start_polling()

    # Ожидание завершения программы
    updater.idle()

if __name__ == '__main__':
    main()
```

### Шаг 4: Запуск бота

Запустите скрипт:

```bash
python cat_bot.py