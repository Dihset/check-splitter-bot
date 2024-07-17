import asyncio
from typing import Any, Coroutine


async def gather_and_wait(tasks: list[Coroutine[Any, Any, None]]) -> tuple[Any]:
    result_list = await asyncio.gather(*tasks, return_exceptions=True)

    for result in result_list:
        if isinstance(result, Exception):
            raise result

    return result_list
