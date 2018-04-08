class AuthenticationError(Exception): pass


class UserLoginBlockedError(AuthenticationError):
    def __init__(self):
        super().__init__('User are ben blocked to login action')