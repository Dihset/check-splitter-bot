from typing import Any


class BaseMessageBuilder:
    _text: str = ""
    _reply_markup: Any = None

    @property
    def text(self) -> str:
        return self._text

    @property
    def reply_markup(self) -> Any | None:
        return self._reply_markup

    def build(self):
        content = {"text": self.text}

        if self.reply_markup:
            content["reply_markup"] = self.reply_markup

        return content
