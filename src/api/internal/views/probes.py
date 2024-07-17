from aiohttp import web

from src.core.containers import get_container
from src.domain.services.healthcheck import IHealthCheckService


async def heathcheck_view(request: web.Request) -> web.Response:
    container = get_container()
    healthcheck_service = container.resolve(IHealthCheckService)
    response_data = await healthcheck_service.check()
    return web.json_response(response_data)
