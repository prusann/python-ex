kapital_poczatkowy=int(input("podaj kapitał początkowy: "))
wplywy=int(input("podaj miesięczne wpływy: "))
wydatki=int(input("podaj miesięczne wydatki: "))

oszczednosci=kapital_poczatkowy+12*(wplywy-wydatki)
print("twoje oszczędności wynoszą: ",oszczednosci)
