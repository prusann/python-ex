kapital_poczatkowy = int(input('Podaj kapitał początkowy: '))
mies_wplywy = int(input('Podaj miesięczne wpływy: '))
okres_inwestowania = int(input('Podaj okres inwestowania w miesiącach: '))
pozadana_wartosc = int(input('Podaj pożądaną końcową wartość inwestycji:'))
kapital_koncowy = (kapital_poczatkowy + mies_wplywy*okres_inwestowania) * 1.02
if pozadana_wartosc < kapital_koncowy:
    print('Kwota jest mniejsza niż pożądana końcowa wartość inwestycji ')
elif pozadana_wartosc == kapital_koncowy:
     print('Kwota jest taka sama jak pożądana końcowa wartość inwestycji ')
else:
    print('Kwota jest większa niż pożądana końcowa wartość inwestycji ')
