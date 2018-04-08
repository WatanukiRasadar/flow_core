from jwt import encode
from kylin import Service, Inject
from kylin.extras.provider import ProviderInject
from ._exceptions import AuthenticationError, UserLoginBlockedError
from ._user import User


@Service('authentication.authenticator')
class Authenticator:

    @ProviderInject('user', 'providers.repository.user')
    async def authenticate(self, user: User):
        if user is None: raise AuthenticationError('Invalid credentials')
        if not user.active: raise UserLoginBlockedError()
        return user
