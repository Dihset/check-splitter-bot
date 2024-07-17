from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class StartMessageBuilder(BaseMessageBuilder):
    _text = (
        "👋 Привет! Я помогу тебе легко и быстро разделить чек с друзьями после посещения бара или ресторана. \n\n"
        "Выбери, что ты хочешь сделать:"
    )
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1️⃣ Добавить друга", callback_data="friend")],
            [InlineKeyboardButton(text="2️⃣ Разбить чек", url="https://ya.ru")],
        ],
    )
