from werkzeug.security import safe_str_cmp #there maybe some difficulty in comparing strings in different python versions and different systems, to be on a safer side we use this for string comparison
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
