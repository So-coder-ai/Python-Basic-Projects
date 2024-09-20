print("this is a exclusive calculator")
operator=input("enter what you want to do ")
d1=float(input("enter the first number "))
d2=float(input("enter the second number"))
if operator=='+':
    sum=d1+d2
    print(f"your sum is : {sum}")
elif operator=='-': 
    if d1>d2 :
        subt=d1-d2
        print(f"the subtraction of the numbers is : {subt}")
    else:
        subt=d2-d1
        print(f"the subtraction of the numbers is : {subt}")
elif operator=='*':
    mult=d1*d2
    print(f"the multiplication of numbers is: {mult}")
elif operator=='/':
    divi=d1/d2
    print(f"division is {divi}")
else:
    print("not a valid ")
