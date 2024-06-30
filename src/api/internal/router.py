from aiohttp import web

from src.api.internal.views.probes import heathcheck_view

router = (
    web.get('/api/internal/healthcheck', heathcheck_view),
)