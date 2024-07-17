import logging

from aiogram import types

from src.bot.messages.start import StartMessageBuilder
from src.bot.utils import callback_handler_wrapper

logger = logging.getLogger(__name__)


@callback_handler_wrapper
async def start_handler(message: types.Message) -> None:
    logger.debug("Command handler running")
    content = StartMessageBuilder().build()
    await message.answer(**content)
