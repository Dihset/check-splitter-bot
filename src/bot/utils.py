from typing import Callable

from aiogram import types

HandlerFuncType = Callable[[types.Message | types.CallbackQuery], None]
MessageHandlerFuncType = Callable[[types.Message], None]


def callback_handler_wrapper(handler: HandlerFuncType) -> MessageHandlerFuncType:
    async def wrapped(event: types.Message | types.CallbackQuery):
        if isinstance(event, types.CallbackQuery):
            message = event.message

        if isinstance(event, types.Message):
            message = event

        await handler(message)

        if isinstance(event, types.CallbackQuery):
            await message.delete()

    return wrapped
