class CalculateError(Exception): pass


class UnknownCalculateToStrategyError(CalculateError):

    def __init__(self, strategy: str):
        super().__init__('The calculator service to strategy "{strategy}" are not registered'.format(strategy=strategy))
