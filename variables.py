import random
from string import digits, ascii_letters


def drop_pass_give_list(s: dict):
    return [y for x, y in s.items() if x != 'password']


def rs(base, ln):  # random string from base characters, ln length
    return ''.join(random.choice(base) for i in range(ln))


def new_random_user():
    p = ascii_letters + digits
    return {'username': rs(p, random.randrange(4, 10)), 'password': rs(p, random.randrange(4, 10)),
            'firstname': rs(p, random.randrange(4, 10)), 'lastname': rs(p, random.randrange(4, 10)),
            'phone': rs(p, random.randrange(4, 10))}


user1 = {'username': 'User11', 'password': 'Pass11', 'firstname': 'Firsname11', 'lastname': 'Lastname11',
         'phone': 'Phone11'}
user2 = {'username': 'User2', 'password': 'Pass2', 'firstname': 'Firsname2', 'lastname': 'Lastname2',
         'phone': 'Phone2'}
user3 = {'username': 'User3', 'password': 'Pass3', 'firstname': 'Firsname3', 'lastname': 'Lastname3',
         'phone': 'Phone3'}
user1_np = drop_pass_give_list(user1)  # np == no password, used in UI test
user2_np = drop_pass_give_list(user2)
user3_np = drop_pass_give_list(user3)


apiuser1 = {'username': 'apiuser1', 'password': 'apipass1', 'firstname': 'apifirstname1', 'lastname': 'apilastname1',
            'phone': 'apihone1'}
apiuser2 = {'username': 'apiuser1', 'password': 'apipass1', 'firstname': 'apifirstname1', 'lastname': 'apilastname1',
            'phone': 'apihone1'}
apirand1 = new_random_user()
apirand2 = new_random_user()
techuser = {'username': 'root', 'password': 'root', 'firstname': 'root', 'lastname': 'root',
            'phone': 'root'}
techuser_token = ''

users = {'user1': user1, 'user2': user2, 'user3': user3, 'apirand1': apirand1, 'apirand2': apirand2,
         'techuser': techuser}

UI_tests_executed = False

server = 'localhost:8080'
browser = 'Chrome'
base_url = 'http://{}/'.format(server)
login_url = 'http://{}/login'.format(server)
register_url = 'http://{}/register'.format(server)
error_url = 'http://{}/error'.format(server)
user_url = 'http://{}/user'.format(server)
userfield = 'name:username'
passfield = 'name:password'
fnfield = 'name:firstname'
lnfield = 'name:lastname'
phfield = 'name:phone'
