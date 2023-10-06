class Dom:
    """
    klasa opisujaca dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Moj kolor domu to: {self.__kolor}")

    def mam_metraz(self):
        print(f"Metraz mojego domu to: {self.__metraz}")

    def mam_okna(self):
        print(f"Liczba okien w moim domu to: {self.__liczba_okien}")

    def zmien_kolor(self):
        wybor_koloru = input("Podaj kolor")
        self.__kolor = wybor_koloru
        self.mam_kolor()
        self.__farba()

    def zmien_okna(self):
        nowa_liczba_okien = int(input("Podaj liczbe okien"))
        self.__liczba_okien = nowa_liczba_okien
        self.mam_okna()

    def zmien_metraz(self):
        nowy_metraz = int(input("Podaj nowy metraz"))
        self.__metraz = nowy_metraz
        self.mam_metraz()

    def __farba(sel):
        print("Skonczyla sie farba")


dom1 = Dom(123, 'bialy', 3)

dom1.mam_kolor()
dom1.mam_metraz()
dom1.mam_okna()

dom1.mam_okna()

dom1.zmien_metraz()

dom1.zmien_kolor()
