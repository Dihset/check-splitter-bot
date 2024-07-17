import abc


class IHealthCheckService(abc.ABC):
    @abc.abstractmethod
    async def check(self):
        pass
