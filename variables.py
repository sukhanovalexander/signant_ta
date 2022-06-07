def drop_pass_give_list(s: dict):
    return [y for x, y in s.items() if x != 'password']


user1 = {'username': 'User11', 'password': 'Pass11', 'firstname': 'Firsname11', 'lastname': 'Lastname11',
         'phone': 'Phone11'}
user1_np = drop_pass_give_list(user1)  # np == no password

user2 = {'username': 'User2', 'password': 'Pass2', 'firstname': 'Firsname2', 'lastname': 'Lastname2',
         'phone': 'Phone2'}
user2_np = drop_pass_give_list(user2)

user3 = {'username': 'User3', 'password': 'Pass3', 'firstname': 'Firsname3', 'lastname': 'Lastname3',
         'phone': 'Phone3'}
user3_np = drop_pass_give_list(user3)

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
