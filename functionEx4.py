#Approach4,py

def sumop():
    a = float(input("enter first value: "))
    b = float(input("enter second value: "))
    c = a+b
    return a,b,c

k,v,r = sumop()
print(f"{k}+{v}={r}")
print("-"*50)
res = sumop()
print(f"{res[0]}+{res[1]}={res[2]}")
print("---------------OR---------------")
print(f"{res[-3]}+{res[-2]}={res[-1]}")
