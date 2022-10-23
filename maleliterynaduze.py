
def zad1(a):
    b = ''
    v = ['a','e','o','i','u','y']
    c = ['B','C','D','F','G','H','J','K','L','M','N','P','R','S','T','W','X','Z']
    for i in a:
        if i in v:
            b = b + i.upper()
        elif i in c:
            b = b + i.lower()
        else:
            b = b + i
    print(b)
zad1('Hello world')