def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


fun1()
x = fun1()

print(x)
print(type(x))
x()