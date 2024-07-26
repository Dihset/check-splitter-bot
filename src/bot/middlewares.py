from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from src.core.containers import get_container
from src.domain.entities.user import User
from src.domain.services.user import IUserService


class GetOrCreateUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            chat = event.chat
        if isinstance(event, CallbackQuery):
            chat = event.message.chat

        user = User(
            telegram_id=str(chat.id),
            first_name=chat.first_name,
            last_name=chat.last_name,
            username=chat.username,
        )

        container = get_container()
        service = container.resolve(IUserService)
        user = await service.get_or_create(user)

        return await handler(event, data)
