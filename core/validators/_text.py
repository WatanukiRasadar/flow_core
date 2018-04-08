from kylin.extras.validator import Validator


class TextValidator(Validator):

    def __init__(self, blank = True, max_length = float('inf'), min_length=0, valid_values=None):
        self.blank = blank
        self.max_length = max_length
        self.min_length = min_length
        self.valid_values = valid_values

    async def validate(self, value: str):
        if not isinstance(value, str):
            raise ValueError('Invalid value type, required str got %s' % str(type(value)))
        if len(value) > self.max_length:
            raise ValueError('Invalid value length, max length is %d got %d' % (self.max_length, len(value)))
        if len(value) < self.min_length:
            raise ValueError('Invalid value length, min length is %d got %d' % (self.min_length, len(value)))
        if (not self.blank) and (not value.replace(' ', '')):
            raise ValueError('Invalid value, blank value not allowed')
        if self.valid_values is not None and value not in self.valid_values:
            raise ValueError('Value not allowed, valid values: %s' % ','.join(self.valid_values))
