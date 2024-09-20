pad=((1,2,3),
     (4,5,6),
     (7,8,9),
     ("*",0,"#"))


for x in pad:
    for j in x:
        print(j, end=" ")
    print()