# klasa

class Human:
    """
    Klasa opisujaca czlowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(self)
        print(f"Nazywam sie {self.imie}")

    def wiosny(self):
        print(self)
        print(f"Mam {self.wiek} lat.")


print(Human.__doc__)

# print(print.__doc__)


cz1 = Human()

print(cz1)

# print(cz1.)

print(cz1.plec)
cz1.imie = "Kasia"
cz1.wiek = 29

print(cz1.imie)
print(cz1.wiek)

cz2 = Human()
cz2.imie = "Przemo"
cz2.plec = "m"
cz2.wiek = 30
print(cz2.imie)
print(cz2.wiek)
print(cz1.powitanie())

print(cz1.wiosny())
cz1.wiosny()