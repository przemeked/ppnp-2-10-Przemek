import csv

lista = []

with open('dane.csv', 'r') as file:
    reader = csv.reader(file)

    for i in reader:
        lista.append(i)


print(lista)
print(lista[1][1])

lista[1][1] = 'kasia'


print(lista)

with open('dane2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lista)
