import abc
from typing import Any


class BaseMessageBuilder(abc.ABC):
    text: str = ""
    reply_markup: Any

    def build(self):
        content = {"text": self.text}

        if self.reply_markup:
            content["reply_markup"] = self.reply_markup

        return content
