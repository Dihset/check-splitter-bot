from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class StartMessageBuilder(BaseMessageBuilder):
    text = (
        "👋 Добро пожаловать в нашего бота для разбиения чеков между друзьями!"
        "Этот бот поможет вам и вашим друзьям без проблем разделить счета в ресторанах, кафе и барах, "
        "чтобы каждый знал, сколько и за что платит. \n\n"
        "Выберите, что вы хотите сделать"
    )
    reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Добавить друга", callback_data="friend"),
                    InlineKeyboardButton(text="Добавить чек", url="https://ya.ru"),
                ]
            ],
            #resize_keyboard=True,
        )
