dict = {'imie': 'radek', 'nazwisko': 'kowalski'}
# for k in dict:
#     print(k)
#
# for k in dict.keys():
#     print(k)
#
# for v in dict.values():
#     print(v)
#
# for i in dict.items():
#     print(i)


for k, v in dict.items():
    print(k, 'to', v)

dict2 = {'name': 'imie', 'surname': 'nazwisko'}
print({value: key for key, value in dict2.items()})
print(dict2)
