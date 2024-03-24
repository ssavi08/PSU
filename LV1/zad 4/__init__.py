ime_datoteke = input("Ime datoteke: ")

try:
    datoteka = open(ime_datoteke)
except:
    print("Ne mogu otvoriti datoteku:", ime_datoteke)
    quit()

suma = 0
brojac = 0

for linija in datoteka:
    if linija.startswith("X-DSPAM-Confidence:"):
        pocetak = linija.find(":")
        broj = float(linija[pocetak+1:])
        suma += broj
        brojac += 1

if brojac > 0:
    prosjek = suma / brojac
    print("Average X-DSPAM-Confidence:", prosjek)
else:
    print("Nema linija oblika 'X-DSPAM-Confidence:' u datoteci.")