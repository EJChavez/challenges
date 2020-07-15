import requests
import hashlib
import sys


def request_api_data(hashed_password):
    # returns the api data if the password was properly trunkaded and hashed
    # checks the website for all passwords with the first 5 hash digits
    url = 'https://api.pwnedpasswords.com/range/' + hashed_password
    res = requests.get(url)
    # checks if its actually a valid 5 digit combination
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check API and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # gets how many times the specific hash exists in the API, and isolates the number
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if it exists in API response as well as encoding password
    # before it can check if its been pwned it needs to hash it
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # and then only take the first 5 characters of the password
    first5_char, tail = sha1password[:5], sha1password[5:]
    # sends the first 5 characters to the actual api data
    response = request_api_data(first5_char)
    # after it confirms that the password has been hashed and such, then it checks if its been pwned by the API
    return get_password_leaks_count(response, tail)


def main(*args):
    for password in args:
        # to do the count it needs to check the pwned api
        count = pwned_api_check(password)
        # we get the count from the get_password_leaks_count function
        if count:
            print(f'{len(password)*"*"} was found {count} times... change your password')
        else:
            print(f'{len(password)*"*"} was not found, keep using it')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main('password'))
