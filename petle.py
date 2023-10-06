# for i in range(10):
#     print(i)
from itertools import zip_longest

for _ in range(10):
    pass
import random

lista2 = list(range(1, 50))
for i in range(6):
    wynik = random.choice(lista2)
    lista2.remove(wynik)
    print(f"Twoja szczesliwa liczba to: {wynik}")

for i in range(10):
    print(i * 2)

for i in range(10):
    if i % 2 == 0:
        print(i, "Parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

for c in lista3:
    print(c)

for c in lista3:
    if c == 2:
        c += 1
    print(c)

a = 1
a += 1
print(f"'liczba a {a}")

b = 1
b -= 1
print(f"'liczba b {b}")

c = 4
c *= 5
print(f"'liczba c {c}")

d = 4
d %= 5
print(f"'liczba d {d}")

e = 4
e /= 5
print(f"'liczba e {e}")

imiona = ['Asia', 'Radek', 'Zbyszek', 'Karolina']

for p in range(len(imiona)):
    print(p, imiona[p])

for p in imiona:
    print(imiona.index(p), p)

for p in enumerate(imiona):
    print(p)

for p, w in enumerate(imiona):
    print(f"{p}:{w}")

for p, w in enumerate(imiona):
    print(p, w, sep=";")

for p, w in enumerate(imiona):
    print(p, w, sep=";", end='')

print()

for p, w in enumerate(imiona):
    print(f"Imie na pozycji {p} to: {w}")

print(enumerate(imiona))


ludzie = ['Asia', 'Radek', 'Zbyszek', 'Karolina', 'Kasia']
wiek = [47, 67, 43, 32]

# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])


for k in zip(ludzie, wiek):
    print(k)

for o, w in zip(ludzie, wiek):
    print(o, w)

for p in enumerate(zip(ludzie,wiek)):
    print(p)

a, b = (3, ('Karolina', 32))
print(a, b)
c, d = b
print(a, c, d)

for o, (w, p) in enumerate(zip(ludzie,wiek), start=1):
    print(f"Na pozycji startowej numer {o} znajduje sie {w} w wieku {p} lat.")


zipped = zip_longest
jezyk = ['PL', 'EN']

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='brak danych')
print(type(zipped))
print(zipped)
zipped_list= list(zipped)

for item in zipped_list:
    print(item)

for o, w, j in zipped_list:
    print(o, w, j)

zipped2 = zip_longest(ludzie, wiek)
zippedlist = list(zipped2)
for o, w in zippedlist:
    print(f"lista imie {o}, {w}")