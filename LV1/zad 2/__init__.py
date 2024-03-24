try:
    print('Unesi ocjenu izmedu 0.0 i 1.0: ')
    broj = float(input())

    # ocjena = {1:'F', 2:'D', 3:'C', 4:'B', 5:'A'}
    # for i in range(6):
    #     if(broj*10 == i):
    #         print(ocjena[i])

    if 0.0 <= broj <= 1.0:
        if broj >= 0.9:
            print('A')
        elif broj >= 0.8:
            print('B')
        elif broj >= 0.7:
            print('C')
        elif broj >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print('Greska! Unesena ocjena izvan intervala.')
except ValueError:
    print('Unos nije broj!')