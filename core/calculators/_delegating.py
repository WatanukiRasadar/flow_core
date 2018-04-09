from ._calculator import Calculator
from ._exceptions import UnknownCalculateToStrategyError
from kylin import Scope, ServiceNotFoundException


class DelegatingCalculator(Calculator):

    def __init__(self, calculators_prefix: str):
        self.calculators_prefix = calculators_prefix

    @property
    def scope(self): return Scope()

    async def calculate(self, strategy: str, *args, **kwargs):
        try:
            return await self.scope['{prefix}.{strategy}'.format(
                strategy=strategy,
                prefix=self.calculators_prefix
            )].calculate(*args, **kwargs)
        except ServiceNotFoundException as error:
            raise UnknownCalculateToStrategyError(strategy)
