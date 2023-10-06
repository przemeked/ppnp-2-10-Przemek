# odp = True
#
# if odp:
#     print ("Brawo")    # oboiwazkowo cztery spracjegfgff
# else:
#     print("mussisz sie dalej uczyc")
# print("działam dalej")
#
# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(podatek)
# print(f"Podatek wynosi {zarobki * podatek}")

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi {rabat}")

list_bledow = []
alert_system = '77'
error = 'jgfjgv'

error_message = 'stalo sie cos strasznego'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    list_bledow.append("email")
    if error == 'medium':
        list_bledow.append('ostrzenie')
    elif error == 'critical':
        list_bledow.append("krytyczny")
    else:
        list_bledow.append("other bug2")
else:
    print(f"nie znany blad {error}")

# print(list_bledow)

a = 14
b = 3
print(f"Wynik porowanania {a} > {b}, {a > b}")
print(f"Wynik porowanania {a} < {b}, {a < b}")
print(f"Wynik porowanania {a} >= {b}, {a >= b}")
print(f"Wynik porowanania {a} <= {b}, {a <= b}")
print(f"Wynik porowanania {a} == {b}, {a == b}")
print(f"Wynik porowanania {a} != {b}, {a > b}")


odp = input("Podaj rok przystapienia PL do UE")

if odp == '2004':
    print("Poprawna odpowiedz")
else:
    print("Odpowiedz bledna")