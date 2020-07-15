# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:


user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}
user2 = {
    'name' : 'notSorna',
    'valid': False
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[1]['valid']:
            result = fn(*args, **kwargs)
            return result
    return wrapper


@authenticated
def message_friends(*args, **kwargs):
    print('message has been sent')


message_friends(user1, user2)
