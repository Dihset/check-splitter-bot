from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class AddFriendMessageBuilder(BaseMessageBuilder):
    text = (
        "🤝 Хорошо, давайте добавим нового друга. \n"
        "Выберите способ добавления:"
    )
    reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Добавить вручную", url="https://ya.ru"),
                    InlineKeyboardButton(text="Отправить приглашение", url="https://ya.ru"),
                ]
            ],
            #resize_keyboard=True,
        )
