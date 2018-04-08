from kylin.extras.validator import Validator
from asyncio import wait, FIRST_EXCEPTION
from typing import Dict, AnyStr


class DictValidator(Validator):

    def __init__(self, schema: Dict[AnyStr, Validator]):
        self.schema = schema

    async def validate(self, value):
        if not isinstance(value, dict):
            raise ValueError('Invalid value, expected dict')
        tasks = []
        for field_name, field_validator in self.schema.items():
            field_value = value.get(field_name, object)
            if field_name is not object:
                tasks.append(field_validator.validate(field_value))
        for task_list in await wait(tasks, return_when=FIRST_EXCEPTION):
            for task in task_list:
                await task
