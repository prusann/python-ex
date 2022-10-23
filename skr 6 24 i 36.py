a = 24
b = 36
c = 1
d = False
while not d:
    c+=1
    if c%a==0 and c%b==0:
        d = True
        print('Najmniejszą wspólną welokrotność liczb {} i {} jest {} '. format (a,b,c))
