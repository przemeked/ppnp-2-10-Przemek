import chardet

file_path = 'test.log'
with open(file_path, 'rb') as file:
    raw_data = file.read()

print(raw_data)
result = chardet.detect(raw_data)
print(result)

kodowanie = result['encoding']
confidence = result['confidence']
print(kodowanie, confidence)
print(raw_data.decode(encoding=kodowanie))



