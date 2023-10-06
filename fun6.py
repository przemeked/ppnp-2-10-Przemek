def liczby(i=10, *cyfry):
    print(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        count = len(cyfry)
        avg = suma / count
    except Exception as e:
        print('Bład', e)
    else:
        print(f'Srednia wynosi {avg}')


liczby()
liczby(1, 2, 3)
liczby(10, 2, 3, 4, 5, 6)
