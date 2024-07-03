import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart

from src.bot.handlers.add_friends_handlers import start_add_friend_handler
from src.bot.handlers.start_handler import start_handler
from src.bot.view import TelegramWebhookView
from src.core.configs import settings

logger = logging.getLogger(__name__)


async def telegram_view_factory() -> TelegramWebhookView:
    bot = Bot(token=settings.TELEGRAM_API_KEY)
    await bot.set_webhook(settings.TELEGRAM_WEB_HOOK)

    dispatcher = Dispatcher()
    dispatcher.message.register(start_handler, CommandStart())
    dispatcher.callback_query.register(start_add_friend_handler, F.data == 'friend')
    dispatcher.message.register(start_add_friend_handler, Command("friend"))


    return TelegramWebhookView(dispatcher=dispatcher, bot=bot)
