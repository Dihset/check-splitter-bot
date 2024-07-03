import logging

from aiogram import types

from src.bot.messages.start import StartMessageBuilder

logger = logging.getLogger(__name__)


async def start_handler(message: types.Message) -> None:
    logger.debug("Command handler running")
    content = StartMessageBuilder().build()
    await message.answer(**content)
