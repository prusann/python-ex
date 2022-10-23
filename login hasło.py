login  = 'Admin'
password = '1234'
x = False
while not x:
    userlogin = input('Podaj login: ')
    userpassword = input ('Podaj hasło: ')
    print('Błędne hasło')
    if userlogin == login and userpassword == password:
        user_is_authentificated = True
        print('Authentificated')
        break


