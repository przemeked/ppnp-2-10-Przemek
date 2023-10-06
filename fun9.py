def odejmij2(a, b):
    return a - b


odejmij = lambda a, b: a - b

print(odejmij(1, 4))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 1000
print(oblicz_vat(1000))
print(oblicz_vat(100, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(12))
print(wiek(29))

lista = [1, 2, 3, 4, 8, 10, 23, 50]
l = []
for i in lista:
    l.append(i * 2)
print(l)

print([i *2 for i in lista])

def zmien(x):
    return x * 2

print(f"zastosowanie map(): {list(map(zmien, lista))}")

print(f"Zasrosowanie lambdy map(): {list(map(lambda x: x * 2, lista ))}")
print(f"zastosowanie filter(): {list(filter(lambda x: x >8, lista))}")
print(f"zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")
