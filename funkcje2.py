def dodaj(a, b):
    return a + b


print(dodaj(5, 7))
wyn = dodaj(5, 6)
print(f" wyn wynosi {wyn}")
print(f"wynik funkcji wynosi {dodaj(7, 8) + dodaj(8, 88)}")


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(f"zwraca vat z 1000 {oblicz_vat(1000)}")
print(f"zwraca vat z 1000 dla 7 procent {oblicz_vat(1000, 7)}")
print(f"zwraca vat z 5000 dla 15 procent {oblicz_vat(vat=15, cena=5000)}")

zm = oblicz_vat(1000)
if zm == 1230:
    print("dziala")
