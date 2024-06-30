from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.view import TelegramWebhookView
from src.core.configs import settings


async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")


class CustomDispatcher(Dispatcher):
    async def process_update(
        self,
        update: types.Update,
    ):
        print(dict(update))
        # await metrics_sender_service.send_metrics(dict(update))
        return await super().process_update(update)


async def telegram_view_factory() -> TelegramWebhookView:
    bot = Bot(token=settings.TELEGRAM_API_KEY)
    await bot.set_webhook(settings.TELEGRAM_WEB_HOOK)

    dispatcher = Dispatcher()
    dispatcher.message.register(command_start_handler, CommandStart())

    return TelegramWebhookView(dispatcher=dispatcher, bot=bot)
