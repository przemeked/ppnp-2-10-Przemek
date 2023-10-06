dictionary = {}
print(dictionary)

dictionary['imie'] = 'Radek'
print(dictionary)
dictionary['wiek'] = '39'
print(dictionary)

print(type(dictionary))

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())

dictionary.update({'date': '12-12-2023'})
print(dictionary)

dictionary1 = {'x': 2}
print(dictionary1)
dictionary1.update([('y', 3), ('z', 5)])
print(dictionary1)
print(dictionary1['x'])

slownikPLEN = {}
slownikPLEN = {'imie': 'name', 'cat': 'kot', 'dog': 'pies'}
print(slownikPLEN)
print('Mam w slowniku', slownikPLEN.keys())

#key = input("Podaj slowko do przetlumaczenia")
#print(slownikPLEN[key.replace(" ", "").lower()])
# apka kalkulator
key1 = float(input("Podaj liczbe A"))
key2 = float(input("Podaj liczbe B"))

print(key1 + key2)

