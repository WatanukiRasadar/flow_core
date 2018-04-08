import pytest
from core.authentication import Authenticator, AuthenticationError, UserLoginBlockedError
from tests.user_provider import UserProvider
from quart import Quart


@pytest.fixture()
def app() -> Quart: return Quart(__name__)


@pytest.fixture
def authenticator() -> Authenticator: return Authenticator()


@pytest.mark.asyncio
async def test_authentication(authenticator: Authenticator, app: Quart):

    async with app.app_context():

        await authenticator.authenticate(user_id=1)
        with pytest.raises(UserLoginBlockedError):
            await authenticator.authenticate(user_id=2)
        with pytest.raises(AuthenticationError):
            await authenticator.authenticate(user_id=3)
        await authenticator.authenticate(user_name='foo')
