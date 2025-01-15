def disp(obj):
    if (obj == None):
        print("obj not available")
    print("=" * 50)
    print("Type of obj =", type(obj))
    print("=" * 50)

    if type(obj) in [int, float, bool, complex]:
        print("Non-Iterable object = {}".format(obj))

    elif (type(obj) != dict) and type(obj) in [str, bytes, bytearray, range, tuple, set, frozenset, list]:
        for i in obj:
            print("\t{}".format(i))
    elif (type(obj) == dict):
        for k, v in obj.items():
            print("\t {} --> {}".format(k, v))
    else:
        print("value of obj =", obj)

        print("-_-" * 50)


lst = [10, 20, "Python", "c", True, 2 + 3j]
disp(lst)
tpl = (100, 'RS', 34.56, True, -34)
disp(tpl)
fs1 = frozenset({10, 20, -45, -56, 3 + 4.5j, "HYD"})
disp(fs1)
s = "MISSISSIPPI"
disp(s)
a = 10
disp(a)
b = []
disp(b)
