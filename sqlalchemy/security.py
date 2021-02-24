from models.user import UserModel as User

__all__ = [
    'authenticate',
    'identify'
]

## function to check the password 
def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = User.find_by_username(username)
    if user and user.password == password:
        return user

## function to identify the user 
def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
