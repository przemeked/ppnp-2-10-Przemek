import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = re.get(url)

print(response)

table = response.json()
print(table)
print(type(table))

print(table.keys())
print(table.values())

print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates'])

print(len(table['rates']))
print(table['rates'][0]['no'])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])


urlthb = 'http://api.nbp.pl/api/exchangerates/rates/A/THB/'
response2 = re.get(urlthb)
print(response2)


table2 = response2.json()
print(table2)
print(type(table2))