tekst ="Witaj swiecie"
print(tekst)
print(type(tekst))
tekst.upper()

tekst2=tekst.upper()

print(tekst)
print(tekst2)
print(tekst.lower())
print(tekst.upper())
print(tekst.removeprefix("witaj"))
print(tekst.removeprefix("Witaj").upper())

encoded_s = tekst.encode('utf-8')
print(encoded_s)
print(type(encoded_s))

print(tekst[0])
print(tekst.count("i"))
print(tekst.count("i", 0, 4))
print(tekst.count("j", 0, 4))


print(len(tekst))

imie = "Przemo"
tekst_format = f"Mam na imie {imie} i lubie jesc"
print(tekst_format)
tekst_format = f"\tMam na imie {imie}\n i lubie jesc\b"
print(tekst_format)

starszy = "Witaj %s"
print(starszy % imie)
print("Witajjjj {}".format(imie))

print ("""
    Teskt wiel
linijkowyyyfddfdf""")