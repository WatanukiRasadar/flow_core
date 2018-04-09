from abc import ABC, abstractmethod


class Calculator(ABC):

    @abstractmethod
    async def calculate(self, *args, **kwargs): pass