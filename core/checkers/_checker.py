from abc import ABC, abstractmethod


class Checker(ABC):

    @abstractmethod
    async def check(self, *args, **kwargs): pass
