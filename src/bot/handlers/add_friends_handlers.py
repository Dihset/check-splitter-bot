import logging

from aiogram import types

from src.bot.messages.add_friend import (
    AddFriendMessageBuilder,
    AddFriendsManuallyMessageBuilder,
)
from src.bot.utils import callback_handler_wrapper

logger = logging.getLogger(__name__)


@callback_handler_wrapper
async def start_add_friend_handler(message: types.Message) -> None:
    content = AddFriendMessageBuilder().build()
    await message.reply(**content)


@callback_handler_wrapper
async def add_friend_manually_handler(message: types.Message) -> None:
    content = AddFriendsManuallyMessageBuilder().build()
    await message.reply(**content)


@callback_handler_wrapper
async def get_friend_request_handler(message: types.Message) -> None:
    pass
