print('Radni sati: ')
radniSati = int(input())
print('eura/h: ')
euroPoSatu = float(input())

zarada = radniSati*euroPoSatu
print('Ukupno: ', zarada, ' eura')

def total_euro(radniSati, euroPoSatu):
    print('Ukupno: ',float(radniSati*euroPoSatu), ' eura')

total_euro(radniSati, euroPoSatu)