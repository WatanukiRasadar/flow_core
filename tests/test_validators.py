from core.validators import TextValidator, ListValidator, NumberValidator, DictValidator
import pytest


@pytest.mark.asyncio
async def test_text_validations():

    validator = TextValidator(blank=False)
    with pytest.raises(ValueError):
        await validator.validate('')
    await validator.validate('test')

    validator = TextValidator(max_length=3)
    with pytest.raises(ValueError):
        await validator.validate('1234')
    await validator.validate('123')

    validator = TextValidator(min_length=2)
    with pytest.raises(ValueError):
        await validator.validate('1')
    await validator.validate('12')

    validator = TextValidator(valid_values=['1', '2'])
    with pytest.raises(ValueError):
        await validator.validate('3')
    await validator.validate('1')


@pytest.mark.asyncio
async def test_number_validations():

    validator = NumberValidator(min_value=2)
    with pytest.raises(ValueError):
        await validator.validate(1)
    await validator.validate(2)

    validator = NumberValidator(max_value=2)
    with pytest.raises(ValueError):
        await validator.validate(3)
    await validator.validate(2)

    validator = NumberValidator(allow_str=True, max_value=2)
    with pytest.raises(ValueError):
        await validator.validate('3')
    await validator.validate('2')

    validator = NumberValidator(decimal=False)
    with pytest.raises(ValueError):
        await validator.validate(2.2)
    await validator.validate(2)


@pytest.mark.asyncio
async def test_list_validation():

    validator = ListValidator(limit=2)
    with pytest.raises(ValueError):
        await validator.validate([1, 2, 3])
    await validator.validate([1, 2])

    validator = ListValidator(item_validator=TextValidator(blank=False))
    with pytest.raises(ValueError):
        await validator.validate([''])
    await validator.validate(['1'])


@pytest.mark.asyncio
async def test_dict_validation():

    validator = DictValidator({
        'name': TextValidator(blank=False)
    })
    with pytest.raises(ValueError):
        await validator.validate({'name': ''})
    await validator.validate({'name': 'Teste'})
