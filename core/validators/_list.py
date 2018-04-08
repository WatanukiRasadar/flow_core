from kylin.extras.validator import Validator
from asyncio import wait, FIRST_EXCEPTION


class ListValidator(Validator):

    def __init__(self, limit = None,  item_validator: Validator = None):
        self.limit = limit
        self.item_validator = item_validator

    async def validate(self, value):
        if not isinstance(value, list):
            raise ValueError('Invalid value, list is expected')
        if self.limit is not None and self.limit < len(value):
            raise ValueError('Invalid value, limit overflow')
        if self.item_validator is not None:
            tasks = []
            for item in value:
                tasks.append(self.item_validator.validate(item))
            for task in await wait(tasks, return_when=FIRST_EXCEPTION):
                for i in task:
                    await i