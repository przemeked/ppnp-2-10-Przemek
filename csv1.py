import csv

row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']
fields2 = dict(zip(fields, row))
print(fields2)

dict_x = [
    {'name':'radek', 'branch':'coe', 'year':3, 'cgpa':'9.10'},
    {'name':'radek2', 'branch':'cos', 'year':2, 'cgpa':'9.0'},
    {'name':'rade1k', 'branch':'cod', 'year':1, 'cgpa':'9'}
]

filename = 'records.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(row)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=",")
    csvwriter.writeheader()
    csvwriter.writerows(dict_x)



