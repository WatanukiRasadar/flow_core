from kylin.extras.validator import Validator
from typing import Union, AnyStr


class NumberValidator(Validator):

    def __init__(self, valid_values = None, min_value = None, max_value = None, decimal=True, allow_str = False):
        self.valid_values = valid_values
        self.min_value = min_value
        self.max_value = max_value
        self.decimal = decimal
        self.allow_str = allow_str

    async def validate(self, value: Union[AnyStr, float, int]):
        if self.allow_str is True and isinstance(value, str) and value.isnumeric():
                value = float(value)
        elif isinstance(value, str):
            raise ValueError('Invalid value, numeric value is expected')
        if isinstance(value, float) and self.decimal is not True:
            if value.is_integer():
                value = int(value)
            else:
                raise ValueError('Invalid value, expected a integer value')
        if self.valid_values is not None and value not in self.valid_values:
            raise ValueError('Invalid values, allowed values: %s' % ', '.join(self.valid_values))
        if self.min_value is not None and value < self.min_value:
            raise ValueError('Invalid value, min value is %d' % self.min_value)
        if self.max_value is not None and value > self.max_value:
            raise ValueError('Invalid value, max value is %d' % self.max_value)
