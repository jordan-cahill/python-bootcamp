from user import User

users = [
    User(1, 'jordan', 'asdf')
]

username_mapping = {u.username: u for u in users}
# {'jordan': User(1, 'jordan', 'asdf')}

user_id_mapping = {u.id: u for u in users}
# {1: User(1, 'jordan', 'asdf')}

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):  # payload
    user_id = payload['identity']
    return User.find_by_id(user_id)