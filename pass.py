import pickle
import getpass

def get_credentials():
    username = input('Please type your username: ')
    password = getpass.getpass('Please type your password:')
    return username, password

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if pwdb[username] == password:
            status = True
    return status

def add_user(username, password, pwdb):
    if username not in pwdb:
        pwdb[username] = password
        write_pwdb(pwdb)
    else:
        print('User already known!')

def read_pwdb():
    pwdb_path = get_path()
    try:
        with open(pwdb_path, 'rb') as pwdb_file:
            pwdb = pickle.load(pwdb_file)
    except FileNotFoundError:
        pwdb = {}
    return pwdb

def write_pwdb(pwdb):
    pwdb_path = get_path()
    with open(pwdb_path, 'wb') as pwdb_file:
        pickle.dump(pwdb, pwdb_file)

def get_path():
    return '/tmp/pwdb.pkl'

pwdb = read_pwdb()
username, password = get_credentials()
if authenticate(username, password, pwdb):
    print('Login successful')
    ans = input('Add another User? [y/n]')
    if ans == 'y':
        username = input('Please type new username: ')
        password = input('Please type new password: ')
        add_user(username, password, pwdb)
        status = True

else:
    print('Login failed')
