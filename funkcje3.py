a = 10
b = 10

def dodaj():
    a = 6
    b = 7
    print(a + b)


print("zmienna z gory", a)
dodaj()
print("zmienna z gory", a)

def dodaj2():
    print(a+b)
dodaj2()
print("zmienna z gory", a)

def dodaj3():
    global a
    a = 6
    b = 7
    print(a + b)
dodaj3()
print("zmienna z gory", a)