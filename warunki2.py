lista = []
lang = input("Podaj znany Ci jezyk progrmaowania").replace(" ", "").lower()

match lang:
    case "python":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _:
        print(f"nie wiem co Ty tu wpisujesz, a wpisales {lang}")
print(lista)
