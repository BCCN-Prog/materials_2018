import pickle
import getpass

def get_credentials():
    username = input('Please type your username: ')
    password = getpass.getpass('Please type your password:')
    return username, password

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        salt = pwdb[username]['salt']
        hashed_password = hash_password(password, salt)
        if pwdb[username]['password'] == hashed_password:
            status = True
    return status

def add_user(username, password, pwdb, admin = False):
    if username not in pwdb:
        salt = get_salt()
        pwdb[username] = {'password': hash_password(password, salt), 'salt': salt, 'admin': admin}
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

def get_salt():
    import uuid
    return uuid.uuid4().hex

def hash_password(password, salt):
    import hashlib
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    return hashlib.md5(password + salt).hexdigest()

pwdb = read_pwdb()
username, password = get_credentials()

if not pwdb:
    ans = input('Create database with this user? [y/n]')
    if ans == 'y':
        username = input('Please type new username: ')
        password = getpass.getpass('Please type new password:')
        add_user(username, password, pwdb, True)
        print(pwdb)
        status = True

if authenticate(username, password, pwdb):
    print('Login successful')
    if pwdb[username]['admin']:
        ans = input('Add another User? [y/n]')
        if ans == 'y':
            username = input('Please type new username: ')
            password = getpass.getpass('Please type new password:')
            admin = input('Give this user admin role? [y/n]')
            if admin == 'y':
                add_user(username, password, pwdb, admin = True)
            else:
                add_user(username, password, pwdb)
            print(pwdb)
            print('User added successfully')
else:
    print('Login failed')
