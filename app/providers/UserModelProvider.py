from masonite.providers import Provider
from app.models.User import User


class UserModelProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.bind('User', User)

    def boot(self, user: User):
        print("Boot working on each Request", user)
