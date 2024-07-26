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
        telegram_user = data["event_from_user"]

        user = User(
            telegram_id=str(telegram_user.id),
            first_name=telegram_user.first_name,
            last_name=telegram_user.last_name,
            username=telegram_user.username,
            language_code=telegram_user.language_code,
        )

        container = get_container()
        service = container.resolve(IUserService)
        user = await service.get_or_create(user)

        return await handler(event, data)
