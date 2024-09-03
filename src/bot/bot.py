import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart

from src.bot.handlers.add_friends_handlers import (
    add_friend_manually_handler,
    start_add_friend_handler,
)
from src.bot.handlers.start_handler import start_handler
from src.bot.middlewares import GetOrCreateUserMiddleware
from src.bot.view import TelegramWebhookView
from src.project.configs import settings

logger = logging.getLogger(__name__)


def add_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.message.middleware(GetOrCreateUserMiddleware())
    dispatcher.callback_query.middleware(GetOrCreateUserMiddleware())


def add_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.message.register(start_handler, CommandStart())
    dispatcher.callback_query.register(start_handler, F.data == "start")

    dispatcher.callback_query.register(start_add_friend_handler, F.data == "friend")
    dispatcher.message.register(start_add_friend_handler, Command("friend"))

    dispatcher.callback_query.register(
        add_friend_manually_handler,
        F.data == "add_friend_manually",
    )
    dispatcher.message.register(
        add_friend_manually_handler,
        Command("add_friend_manually"),
    )


async def telegram_view_factory() -> TelegramWebhookView:
    bot = Bot(token=settings.TELEGRAM_API_KEY)
    await bot.set_webhook(settings.TELEGRAM_WEB_HOOK)

    dispatcher = Dispatcher()
    add_middlewares(dispatcher)
    add_handlers(dispatcher)

    # dispatcher.callback_query.register(start_add_friend_handler, F.data == "friend")
    # dispatcher.message.register(start_add_friend_handler, Command("friend"))

    return TelegramWebhookView(dispatcher=dispatcher, bot=bot)
