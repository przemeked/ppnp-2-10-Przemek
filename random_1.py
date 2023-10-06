import random

print(random.randint(1, 6))
print(random.random())
print(random.random())
print(random.randrange(1, 6))


lista = [5, 7, 45, 34, 56]

print(random.choice(lista))
print(lista)

lista2 = list(range(1,50))
print(lista2)

# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)


print(random.choices(lista2, k=6))
print(random.sample(lista2, 6))