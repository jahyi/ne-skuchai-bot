from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🃏 Шутка дня")],
        [KeyboardButton(text="📚 Факт дня")],
        [KeyboardButton(text="🎮 Мини-игра")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери категорию"
)
