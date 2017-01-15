#!/usr/bin/python
# encoding:utf-8

user, pwd = 'alex', 'abc123'


def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input('Password:').strip()
                if user == username and pwd == password:
                    print("User has passed authentication")
                    return func(*args, **kwargs)
                else:
                    exit('Invalid user or password')
            elif auth_type == 'ldap':
                print('Via ldap authentication')
        return wrapper
    return outer_wrapper


def index():
    print('Welcome to index page')


@auth(auth_type='local')
# auth = auth(auth_type='local') return outer_wrapper
# home = auth(home) return wrapper
# home <==> wrapper
# home() <==> wrapper()
def home():
    print('Welcome to home page')
    return 'From home'


@auth(auth_type='ldap')
def bbs():
    print('Welcome to bbs page')

index()
print(home())  # home = wrapper
bbs()
