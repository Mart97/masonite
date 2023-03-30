from masonite.providers import Provider
from app.models.User import User


class UserModelProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.bind('User', User)

    def boot(self, user: User):
        providers_list = self.application.providers.__str__().split(', ')
        userinContainer = User.find(1)
        print(userinContainer.name)
        #for p in providers_list:
        #    print(p)
        #print("UsrModelProvider(Provider)@boot working on each Request", user)
