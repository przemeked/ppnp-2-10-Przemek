lista = []  # definicja pustej listy

print(lista)
print(type(list))

print(bool(lista))

lista.append("Radek")
lista.append("Maciek")
lista.append("Ela")
lista.append("Odi")
lista.append("Jasiu")
print(lista)

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print(len(lista))

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])

print(lista[0:3])
print(lista[2:])
print(lista[:3])

print(lista[7:9])
print(lista[1:3])

lista[2] = "Mikolaj"
print(lista)

lista.insert(1, "Marcin11")
print(lista)

ind = lista.index("Marcin11")

element = lista.pop(ind)
print(ind)
print(lista)
print(element)

element = lista.remove("Maciek")

print(bool(None))
lista.remove("Jasiu")
print('Radek' in lista)
lista.append('Radek')
print(lista)
lista.remove('Radek')
print(lista)

a = 1
b = 3
a = b
print(a)
print(b)
a = 7

lista2 = lista
print(lista2)

print(lista)
lista3 = lista.copy()
print(lista3)

print(id(lista))
print(id(lista3))
print(id(lista2))

liczby = [54, 999, 34, 22, 13.34, 687]

print(liczby)
print(type(liczby))

liczby.sort()
print(liczby)

liczby2 = [54, 999, 34, 22, 13.34, 687, "A"]

lista_osoby = ['ala', 'baba', "zgmunet", "tata"]
lista_osoby.sort(reverse=True)
print(lista_osoby)
liczby[3]=6666
print(liczby)
lista_osoby.sort()
print(lista_osoby)
print(liczby[0:3])
print(liczby[-2])
print(liczby[0:-2])
print(liczby[-3:0])
liczby.remove(34)
print(liczby.pop(3))

teksty = "Python"
lista_1 = list(teksty)
print(lista_1)

lista2 = [teksty]
print(lista2)

print(lista_1 + lista2)

krotka = tuple(liczby)
print(krotka)
print(liczby)

