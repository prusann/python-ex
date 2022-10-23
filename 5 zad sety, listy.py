lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2,2,3,3,4,5]
set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)
#wspólne elementy:
if set1 == set2 == set3:
    print ('Wszystkie listy zawierają te same elementy')
elif set1 != set2 == set3:
    print ('set1 != set2 == set3')
elif set1 == set2 != set3:
    print ('set1 == set2 != set3')
else:
    print ('Wszystkie listy nie zawierają tych samych elementów')
#duplikaty:
if len(lista1) == len(set1) and len(lista2) == len(set2) and len(lista3) == len(set3):
    print("+++")
elif len(lista1) == len(set1) and len(lista2) == len(set2) and len(lista3) != len(set3):
    print("lista3 zawiera duplikaty")
elif len(lista1) == len(set1) and len(lista2) != len(set2) and len(lista3) != len(set3):
    print("+--")   
elif len(lista1) != len(set1) and len(lista2) == len(set2) and len(lista3) != len(set3):
    print("-+-")
elif len(lista1) != len(set1) and len(lista2) != len(set2) and len(lista3) == len(set3):
    print("--+")   
elif len(lista1) != len(set1) and len(lista2) == len(set2) and len(lista3) == len(set3):
    print("-++")
elif len(lista1) == len(set1) and len(lista2) != len(set2) and len(lista3) == len(set3):
    print("+-+")
else:
    print("---")