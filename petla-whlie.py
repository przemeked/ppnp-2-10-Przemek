licznik = 0
while True:
    licznik += 1
    print("Komunikat!")
    if licznik > 10:
        break
print("dzialam dalej")


lista = []
lista2 = []

while True:
    wej = input("Podaj liczbe")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)
print(lista2)



