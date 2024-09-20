foods=[]
price=[]
total=0.0
while True:
    food=input("enter the foods here(and press q to quit )")
    
    if food.lower()== "q" :
        break
    else:
        cost=float(input("enter the price $"))
        foods.append(food)
        price.append(cost)

print("--------YOUR CART WAS------------")
for x in foods:
    print(x,end=" ")

    for y in price:
        total+=y

        print()
   
print(f"your total is ${total}")