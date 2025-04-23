from aiogram import Router, types
from aiogram.types import Message
from keyboards import main_keyboard

router = Router()

@router.message(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.answer(
        "Привет! 👋 Я бот 'Не скучай'! Выбери, что тебе интересно:",
        reply_markup=main_keyboard
    )

@router.message(lambda msg: msg.text == "🃏 Шутка дня")
async def joke_handler(message: Message):
    await message.answer("Почему программисты любят осень? Потому что OCT 31 == DEC 25 😄")

@router.message(lambda msg: msg.text == "📚 Факт дня")
async def fact_handler(message: Message):
    await message.answer("Знаешь ли ты? Первый компьютерный баг был настоящей молью 🐛, найденной в реле.")

@router.message(lambda msg: msg.text == "🎮 Мини-игра")
async def game_handler(message: Message):
    await message.answer("🎲 Угадай число от 1 до 3!")

@router.message()
async def fallback_handler(message: Message):
    await message.answer("Не понял тебя 😅 Попробуй выбрать опцию из меню.")
