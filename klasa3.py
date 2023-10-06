class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Predkosc wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car1 = Car("BMW", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.licznik()

car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()


car1.licznik()

