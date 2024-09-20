print("exclusive temperature program :>>>>*********")
unit=input("enter the unit you want to convert in F or C :")
temp=float(input("enter the temperature :>"))
if unit=="C":
    newtemp=round((temp*9)/5+32,1)
    print(f"the new temperature in celcius is : {newtemp}")
elif unit=="F":
    newtemp=round(((temp-32)*5)/9)
    print(f"the new temperature in farenheit is : {newtemp}")
else :
    print(f"the unit {unit} is not a unit :)")