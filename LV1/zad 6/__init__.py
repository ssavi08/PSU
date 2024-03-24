with open('SMSSpamCollection.txt', 'r') as f:
    linije = f.readlines()

hamRijeci = 0
hamPoruka = 0
spamRijeci = 0
spamPoruka = 0
spamUsklicnik = 0

for linija in linije:
    parts = linija.split('\t')
    prviDio = parts[0]
    drugiDio = parts[1]
    rijec = drugiDio.split()

    if prviDio == 'ham':
        hamRijeci += len(rijec)
        hamPoruka += 1
    elif prviDio == 'spam':
        spamRijeci += len(rijec)
        spamPoruka += 1
    elif drugiDio.endswith('!'):
        print(drugiDio)
        spamUsklicnik += 1


srednjaHamVrijednost = hamRijeci / hamPoruka
srednjaSpamVrijednost = spamRijeci / spamPoruka

print(f"Prosječan broj riječi u ham porukama: {srednjaHamVrijednost:.2f}")
print(f"Prosječan broj riječi u spam porukama: {srednjaSpamVrijednost:.2f}")
print(f"Broj spam poruka koje završavaju uskličnikom: {spamUsklicnik}")