#!/usr/bin/python

user, pwd = 'alex', 'abc123'

def auth(func):
    def wrapper(*args, **kwargs):
        username = input('Username:').strip()
        password = input('Password:').strip()
        if user == username and pwd == password:
            print("User has passed authentication")
            return func(*args, **kwargs)
        else:
            exit('Invalid user or password')
    return wrapper

def index():
    print('Welcome to index page')

@auth
def home():
    print('Welcome to home page')
    return 'From home'

@auth
def bbs():
    print('Welcome to bbs page')

index()
print(home())
bbs()