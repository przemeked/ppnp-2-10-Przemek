tupla = "Przemo",
print(type(tupla))
print(tupla)

temp = 37,5
print(type(temp))
print(temp)


tupla2= "Tomek", "radek", "Ala", "Marek"
tupla3= ("Tomek", "radek", "Ala", "Marek")
print(tupla2)
print(tupla3)
print(type(tupla2))

print(tupla3.index("Marek"))

a, b = 1, 2
print(a)
print(b)
print(type((1,2)))

a, *b = 1, 2, 3
print(a)
print(b)
print(tupla2)
imie1, *imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)

lista = list(tupla3)
print(lista)
print(type(lista))

