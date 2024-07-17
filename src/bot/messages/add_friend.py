from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class AddFriendMessageBuilder(BaseMessageBuilder):
    _text = "🤝 Хорошо, давай добавим нового друга. \n\nВыбери способ добавления:"
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1️⃣ Добавить вручную", callback_data="add_friend_manually"
                )
            ],
            [InlineKeyboardButton(text="2️⃣ Отправить приглашение", url="https://ya.ru")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="start")],
        ],
    )


class AddFriendsManuallyMessageBuilder(BaseMessageBuilder):
    _text = "👥 Ты выбрал добавить друга вручную. Пожалуйста, введи имя друга, которого хочешь добавить в список."
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="friend")],
        ],
    )


class GetFriendFequestMessageBuilder(BaseMessageBuilder):
    def __init__(self, user_ref_id: str) -> None:
        self.user_ref_id = user_ref_id

    @property
    def text(self) -> str:
        return ""
