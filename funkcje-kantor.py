def kantor(waluta):
    print("uruchomienie kantoru")


    def usd(x_pln=0):
        x_pln = float(input("Wpisz kwote w PLN"))
        print(f"wymieniam dolarsy, {x_pln}USD po kursie 4.300, wymieniona kwota to: {x_pln * 4.3} USD"),

    def eur(x_pln=0):
        x_pln = float(input("Wpisz kwote w PLN"))
        print(f"Wymieniam dolarsy, {x_pln}EUR po kursie 4.300, wymieniona kwota to: {x_pln * 4.8} EUR"),

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')
print(kantor_usd)

kantor_usd()

kantor_eur = kantor('eur')
print(kantor_eur)

kantor_eur()

