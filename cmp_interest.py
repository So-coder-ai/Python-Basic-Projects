print("this is the best compound interst calculator")
principle=float(input("enter the principle amount "))
rate= float(input("enter the rate of interest "))
time = float(input("enter the time for loan "))
amount = principle*pow((1+rate/100),time)

print(f"amount ${amount:,.2f}")