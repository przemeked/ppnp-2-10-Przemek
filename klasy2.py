class Human:
    """
    Klas opisujaca czlowieka w pajtonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def moj_wzrost(self):
        print(f"Moj wzrost to {self.wzrost}")

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszylam w droge")
        else:
            print("Ruszyłem w drogę")

    def wypisz_plec(self):
        print(f"plec: {self.plec}")


czl1 = Human("Przemo", "30", "178", plec='m')
print(czl1.wiek)
print(czl1.wzrost)
print(czl1.wiek)
print(czl1.plec)
czl1.moj_wzrost()
czl2 = Human("Ewa", "22","168")
print(czl2.wiek)
print(czl2.wzrost)
print(czl2.wiek)
print(czl2.plec)
czl2.moj_wzrost()

czl2.ruszaj()
czl1.ruszaj()
czl1.wypisz_plec()