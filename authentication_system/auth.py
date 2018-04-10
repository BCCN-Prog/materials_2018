import getpass
import pathlib
import pickle
import random
import string
import tempfile

PWDB_FLNAME = pathlib.Path('pwdb.pkl')
CHARS = string.ascii_letters + string.digits + string.punctuation

def get_credentials():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    return (username, password)

def authenticate(username, pass_text, pwdb):
    if username in pwdb:
        salt = pwdb[username][1]
        if pwhash(pass_text, salt) == pwdb[username][0]:
            return True
    return False

def add_user(username, password, salt, paswdb, pwdb_file):
    if username in pwdb:
        raise Exception('Username already exists [%s]' %username)
    else:
        pwdb[username] = (pwhash(password,salt), salt)
        write_pwdb(pwdb, pwdb_file)

def read_pwdb(pwdb_file):
    try:
        pwdb = pickle.load(pwdb_file)
        pwdb_file.seek(0)
    except EOFError:
        pwdb = {}
    return pwdb

def write_pwdb(pwdb, pwdb_file):
    pickle.dump(pwdb, pwdb_file)

def pwhash(pass_text, salt):
    hash_ = 0
    full_pass_text = pass_text + salt
    for idx, char in enumerate(full_pass_text):
        # use idx as a multiplier, so that shuffling the characters returns a
        # different hash
        hash_ += (idx+1)*ord(char)
    return hash_

def get_salt():
    salt_chars = random.choices(CHARS, k=10)
    return ''.join(salt_chars)

if __name__ == '__main__':
    pwdb_path = tempfile.gettempdir() / PWDB_FLNAME
    try:
        pwdb_file = open(pwdb_path, 'rb+')
    except FileNotFoundError:
        pwdb_file = open(pwdb_path, 'wb+')

    username, password = get_credentials()
    pwdb = read_pwdb(pwdb_file)

    if authenticate(username, password, pwdb):
        print('Authentication succeeded!')
        print(pwdb)
    else:
        print('Wrong username or password')
        ans = input('Create new user [y/n]? ')
        if ans == 'y':
            salt = get_salt()
            add_user(username, password, salt, pwdb, pwdb_file)
        else:
            print('Exit!')
