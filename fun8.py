def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("d, d", c, d)
    print("args", args)
    print("kwargs",kwargs)


allparams(1, 2)
allparams(1, 2, 3)
allparams(1, 2, c=3)

allparams(1, 2, 3, 4, 4, 5, 6, 7, 8, 9)
allparams(1, 2, 34, 4, 5, 6, 7, 8, 100, 106, 10987)
allparams(1, 2, 34, 4, 5, 6, 7, 8, 9, d=129)
allparams(1, 2, 34, 4, 5, 6, 7, 8, 9, d=129, klucz='wart')
allparams(1, 2, 34, 4, 5, 6, 7, 8, 9, d=129, klucz='wart', a=8)
