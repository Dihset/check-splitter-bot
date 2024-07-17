from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class AddFriendMessageBuilder(BaseMessageBuilder):
    _text = "🤝 Хорошо, давай добавим нового друга. \n\nВыбери способ добавления:"
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1️⃣ Добавить вручную", url="https://ya.ru")],
            [InlineKeyboardButton(text="2️⃣ Отправить приглашение", url="https://ya.ru")],
            [InlineKeyboardButton(text="🔙 Назад", url="https://ya.ru")],
        ],
    )
