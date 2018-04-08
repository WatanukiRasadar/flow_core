from kylin.extras.provider import Provider
from kylin import Service
from core.authentication import User
from overload import overload

class User(User):

    def __init__(self, id: int, name: str, active=True):
        self.id = id
        self.active = active
        self.name = name

@Service('providers.repository.user')
class UserProvider(Provider[User]):

    users = [
        User(1, 'foo', True),
        User(2, 'bar', False)
    ]

    @overload
    async def provide(self, id: int):
        try:
            return next(user for user in self.users if user.id == id)
        except: pass

    @provide.add
    async def provide(self, name: str):
        try:
            return next(user for user in self.users if user.name == name)
        except: pass
