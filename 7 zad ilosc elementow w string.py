def count_chars():
    slowo=input('wpisz stringa: ')
    ilosc=len(slowo)
    print('ilość liter w podanym stringu to', ilosc)
    z=0
    for key in slowo:
        slownik={slowo[0+z]:1}
        z+=1
        #print(key,"'", slownik[key],"'", end="   ")
        print(slownik, end='')
count_chars()   
