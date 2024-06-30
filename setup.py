from aiohttp import web

from src.web import init_app

if __name__ == "__main__":
    web.run_app(init_app())
