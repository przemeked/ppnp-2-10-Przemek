from abc import ABC, abstractmethod

class Ptak(ABC):
# class Ptak:
    """
    klasa opisujaca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lece z szybkoscia", self.szybkosc)

    @abstractmethod #oznaczenie metody jako abstrakcyjna
    def wydaj_odglos(self):
        pass



class Kura(Ptak):
    """
    Kura
    """
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print(f"Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokoko")



class Orzel(Ptak):
    """
    Orzel
    """
    def wydaj_oglos(self):
        print(f"pii")

# orz1= Ptak("sokol", 20)
# orz1.latam()
# kur1 = Ptak("kura", 0)
#
# kur1.latam()
# kur1.wydaj_odglos()
#
# # kur2 = Kura("Kura", 0)
kur2 = Kura("Kura")
print(kur2.gatunek)
# kur2.latam()
##pt4 = Orzel("Orzel", 20)
#
# pt4.latam()
#
# pt4.wydaj_odglos()
