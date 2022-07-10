def is_authenticated():
    return True


def is_active():
    return True


def is_anonymous():
    return False


class UserLogin:
    def __init__(self):
        self.__user = None

    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user

    def get_id(self):
        return str(self.__user['id'])
