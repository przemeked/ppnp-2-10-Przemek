import csv

filename = 'records.csv'

fileds = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    csv_f.seek(0)

    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(fields)
print(rows)

suma = 0
for i in rows:
    number = float(i[-1])
    suma += number

print(f"Srednia wynosi {suma / len(rows)}")

