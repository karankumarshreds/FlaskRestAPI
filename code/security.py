from user import User

__all__ = [
    'authenticate',
    'identify'
]

users = [
    User(1, 'bob', 'passwd'),
    User(2, 'mark', 'passwd'),
]

username_mapping = { u.username: u for u in users }

userid_mapping = { u.id: u for u in users }

## function to check the password 
def authenticate(username, password):
    user = username_mapping.get(username, None, None)
    if user and user.password == password:
        return user

## function to identify the user 
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
