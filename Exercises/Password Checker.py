def password_checker(): #blocks the password and and tells you how long the password is.
    username = input('please enter your username: ')
    password = input('please enter your password: ')
    print(f'Hello {username}, your password {password.replace(password, ("*" * len(password)))} is {len(password)} letters long')
password_checker()

def password_checker_clean():
    username = input('please enter your username: ')
    password = input('please enter your password: ')
    password_length = len(password)
    hidden_password = '*' * password_length
    print(f'Hello {username}, your password {hidden_password} is {password_length} letters long')
#password_checker_clean()