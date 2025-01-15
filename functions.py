#program for addding two numbers
#ApproachEx1.py

def sumop (a,b):
    c = a+b
    return c
#main program
x = float(input("Enter first value: "))
y = float(input("Enter second value: "))
res = sumop(x,y)
print(f"{x}+{y}= \t{res}")
print("-"*50)
a = float(input("enter first value: "))
b =  float(input("enter second value:"))
c = sumop(a,b)
print(f"{a}+{b}=\t{c}")       