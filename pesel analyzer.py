pesel = '04232706053'
pesel_lista = list(pesel)
if len(pesel)==11:
    print("Pesel poprawny!")
else:
    print("To nie jest pesel!")

dzienurodzenia = str(pesel_lista[4] + pesel_lista[5])

miesiacurodzenia = int(pesel_lista[2] + pesel_lista[3])

if miesiacurodzenia > 20:
    miesiacurodzenia -= 20

nr = miesiacurodzenia

if nr==1:
    miesiacurodzenia_tekst = "stycznia"
elif nr==2:
    miesiacurodzenia_tekst = "lutego"
elif nr==3:
    miesiacurodzenia_tekst = "marca"
elif nr==4:
    miesiacurodzenia_tekst = "kwietnia"
elif nr==5:
    miesiacurodzenia_tekst = "maja"
elif nr==6:
    miesiacurodzenia_tekst = "czerwca"
elif nr==7:
    miesiacurodzenia_tekst = "lipca"
elif nr==8:
    miesiacurodzenia_tekst = "sierpnia"
elif nr==9:
    miesiacurodzenia_tekst = "września"
elif nr==10:
    miesiacurodzenia_tekst = "października"
elif nr==11:
    miesiacurodzenia_tekst = "listopada"
elif nr==12:
    miesiacurodzenia_tekst = "grudnia"
else:
    print("Jest tylko 12 miesięcy!")

rokurodzenia = str('20'+(pesel_lista[0]+pesel_lista[1]))

plec = int(pesel_lista[-2])

if plec%2==0:
    plec_tekst = "Kobieta"
else: 
    plec_tekst = "Mężczyzna"
    
print(plec_tekst,"urodzony/a", dzienurodzenia+"-go",miesiacurodzenia_tekst,rokurodzenia,"roku")