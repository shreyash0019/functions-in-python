#p*r*t/100
def simple_intrest():
    p = float(input("Enter Principle Amount: "))
    r = float(input("Enter Intrest Rate: "))
    t = float(input("Enter Time to pay: "))
    val = (p*r*t/100)
    amount_pay = val+p
    print(f"{val}")
    print(f"{amount_pay}")
simple_intrest()
    