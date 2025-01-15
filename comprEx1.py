print("Enter list of values separated by space: ")
dictobj = {float(val): float(val)**2 for val in input ().split() }
for num,sqval in dictobj.items():
    print("\t{}-->{}".format(num,sqval))