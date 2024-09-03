from abc import ABC, abstractmethod
from typing import Generic, TypeVar

C = TypeVar("C")
R = TypeVar("R")

class BaseUseCase(ABC, Generic[C, R]):
    @abstractmethod
    async def execute(self, command: C) -> R:
        pass
