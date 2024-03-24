brojevi = []

while True:
    unos = input('Unesi broj ("Done" oznacuje kraj unosa)\n')
    if(unos == 'Done'):
        break
    try:
        broj = float(unos)
        brojevi.append(broj)
    except ValueError:
        print('Greska! Unos nije broj.')

if brojevi: #ako polje brojeva nije prazno
    print('Uneseno brojeva: ', len(brojevi))
    print('Srednja vrijednost: ', sum(brojevi)/len(brojevi))
    print('Minimalna vrijednost: ', min(brojevi))
    print('Maksimalna vrijednost: ', max(brojevi))

    brojevi.sort()
    print(brojevi)
else:
    print('Greska! Nije unesen broj')