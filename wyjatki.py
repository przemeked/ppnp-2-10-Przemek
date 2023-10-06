while True:
    print(f"""
1. dodawanie
2. odejmowanie
3. dzielenie
4. mnozenie
5. koniec programu
""")
    odp = input("Podaj operacje")
    if odp == '5':
        break
    try:
        a = float(input("Podaj pierwsza liczbe"))
        b = float(input("Podaj druga liczbe"))

        if odp == '1':
            print("Wynik", a + b)
        elif odp == '2':
            print("Wynik", a - b)
        elif odp == '3':
            print("Wynik", a / b)
        elif odp == '4':
            print("Wynik", a * b)
        else:
            print("Nie wiem o co chodzi")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Blad wartosci")
    except Exception as e:
        print("blad", e)
    else:
        print("gdy nie ma bledu")
    finally:
        print("wykona sie zawsze")

# lista = []
# lang = input("Podaj znany Ci jezyk progrmaowania").replace(" ", "").lower()
#
# match lang:
#     case "python":
#         lista.append(lang)
#     case "c++":
#         lista.append(lang)
#     case "java":
#         lista.append(lang)
#     case _:
#         print(f"nie wiem co Ty tu wpisujesz, a wpisales {lang}")

while True:
    try:
        a = float(input("Podaj pierwsza liczbe dzialania"))
        print(f"""
            1. Dodawanie +
            2. Odejmowanie - 
            3. Dzielenie / 
            4. Mnozenie * 
            5. Wyjscsie
            """)
        dz = input("Podaj jakie dzialnie chcesz wykonac")
        b = float(input("Podaj druga liczbe"))
        match dz:
            case '5':
                break
            case '1':
                print(f"Wynik dodawania {a} + {b} = {a + b}")
            case '2':
                print(f"Wynik odejmowania {a} - {b} = {a - b}")
            case '3':
                print(f"Wynik dzielenia {a} / {b} = {a / b}")
            case '4':
                print(f"Wynik mnozenia {a} * {b} = {a * b}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Blad wartosci")
    except Exception as e:
        print("blad", e)
    else:
        print("wynik gotowy powyzej")
    finally:
        print("zakonczylem liczenie")
