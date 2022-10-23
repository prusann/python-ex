dane_logowania = {'Admin': '1234'}
git = False
while not git:
    login = input('Podaj login: ')
    password = input('Podaj hasło: ')
    if dane_logowania.get(login):
        if dane_logowania[login] == password:
            git = True
            print('Logowanie poprawne')
        else:
            print('Zle hasło')
    else:
        print('Uwierzytelnienie nie powiodło się. Spróbuj jeszcze raz')