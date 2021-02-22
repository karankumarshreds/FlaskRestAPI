from user import User

users = [
    User(1, 'bob', 'passwd')
]

username_mapping = { u.username: u for u in users }

userid_mapping = { u.id: u for u in users }

def authenticate(username, password):
    user = username_mapping.get(username, None, None)
    if user and user.password == password:
        return user

def identify(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
