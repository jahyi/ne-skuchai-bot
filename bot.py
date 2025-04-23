import logging
import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import API_TOKEN

# Логгирование
logging.basicConfig(level=logging.INFO)

# Бот и диспетчер
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Постоянная клавиатура
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎲 Дай мне не заскучать")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери действие 👇"
)

# Список активностей
activities = [
    "😂 Шутка: Почему программисты любят темную тему? Потому что светлая — это баг, а темная — фича!",
    "🤓 Факт дня: У осьминога три сердца. Два из них перестают биться, когда он плывёт!",
    "🎮 Мини-игра: Загадай число от 1 до 10. Я угадаю его позже 😉",
    "🧠 Задачка: Что тяжелее — 1 кг стали или 1 кг пуха?"
]

# Команда /start
@dp.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer(
        "Привет! 👋 Я бот, который не даст тебе заскучать.\nНажми на кнопку ниже!",
        reply_markup=keyboard
    )

# Обработка кнопки
@dp.message(F.text == "🎲 Дай мне не заскучать")
async def handle_random_action(message: Message):
    action = random.choice(activities)
    await message.answer(action)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
