import logging

from aiogram import types

from src.bot.messages.add_friend import AddFriendMessageBuilder

logger = logging.getLogger(__name__)


async def start_add_friend_handler(message: types.Message | types.CallbackQuery) -> None:
    if isinstance(message, types.CallbackQuery):
        message = message.message

    content = AddFriendMessageBuilder().build()
    await message.reply(**content)
