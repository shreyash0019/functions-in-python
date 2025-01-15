def circumference(radius):
    pi = 3.14
    return 2 * pi * radius
radius = float(input("Enter the value of radius: "))
circumference_result = circumference(radius)
print("The circumference of the circle is = ", circumference_result)