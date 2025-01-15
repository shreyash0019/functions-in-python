def incr():
    global a
    a = a + 1


def update_val():
    global a
    a = a * 2


a = 10
print("main program --> val of a before incr() = {}".format(a))
incr()
print("main program --> val of a after incr() = {}".format(a))
update_val()
print("main program --> val of a after update_val() = {}".format(a))
