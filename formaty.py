import sys

user = "Przemek"
wiek = 31
wersja = 3.110001
liczba = 13456774562
print(sys.int_info)
print(sys.float_info)

print("Witaj %s masz teraz %d lat" % (user, wiek))

print("Witaj %(user)s, masz teraz %(age)d lat." % {"user": user, "age": wiek})
print("Witaj {} masz teraz {} lat.".format(user, wiek))
print(f"Witaj {user}, masz teraz {wiek} lat.")

print("Uzywamy wersji %i" % 3)
print("Uzywamy wersji %f" % 3.11)
print("Uzywamy wersji %.1f" % 3.11)
print("Uzywamy wersji %.2f" % 3.11)
print("Uzywamy wersji %.0f" % 3.11)
print("Uzywamy wersji %.f" % 3.9)

x = 3.15
print("Zero miejsc po przecinku %.f" % x)
print("orygianly x =", x)

print(f"uzwamy wersji Pythona {wersja}")
print(f"uzwamy wersji Pythona {wersja:.1f}")
print(f"uzwamy wersji Pythona {wersja:.0f}")

print(f"{user:>10}")
print(f"{user:>20}")
print(f"{user:<30}")
print(f"{user:^24}")

print(liczba)
print("nasza duza liczba {:,}".format(liczba))
print("nasza duza liczba {:,}".format(liczba).replace(",", "."))
print(f"nasza duza liczba {liczba:,}")
print(f"1nasza duza liczba {liczba:,}".replace(",", "."))
