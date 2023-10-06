lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(lista)
print(zbior)

zbior2= set()
print(zbior2)

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)

zbior.remove(55)
print(zbior)
print(zbior.pop())
print(zbior)
print(len(zbior))

print(zbior.pop())
print(zbior)
print(zbior.pop())
print(zbior)
print(zbior.pop())
print(zbior)
print(type(zbior))

lista2= list(zbior)
print(lista2)

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)
print(type(zbior2))

print(zbior | zbior2)
print(zbior & zbior2)
print(zbior - zbior2)
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))

