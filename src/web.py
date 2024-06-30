from aiohttp import web

from src.api.internal.router import router as internal_router
from src.bot.bot import telegram_view_factory
from src.core.configs import settings


async def init_app() -> web.Application:
    app = web.Application()
    settings.config_logger()

    app.router.add_route(
        "*",
        settings.TELEGRAM_WEBHOOK_PATH,
        await telegram_view_factory(),
        name="tg_webhook_handler",
    )

    app.router.add_routes(internal_router)

    return app
