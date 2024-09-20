print("enter a valid user name which does not : ")
print("contain any more than 12 characters :")
print("contain any spaces")
print("contain any numbers")

name = input(" Enter the valid name :")
if len(name) >12:
    print("not a valid name contains more than 12 characters :")
elif not name.find(" ")==-1:
    print("name contains spaces :")
elif not name.isalpha():
    print("contains number")

else:
    print(f"welcome {name} in the gang :")