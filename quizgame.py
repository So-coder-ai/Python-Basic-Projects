print("WELCOME TO THIS QUIZ !!")
print("****************************")
print()
questions=("where did i born ?",
            "where did i go to school ?",
            "who is the prime minister of india ?",
            "whho is sigma in the world ?")
options=("A. kanpur, B. varanasi, C. california, D. london",
        "A. harvard, B. upkssv, C. chinetels , D. navodaya",
         "A. modi, B. rahul gandhi , C. lalau prasad, D. manmohan singh",
         "A. gopi bhahu, B. yogi ji , C. u?, D. shiv")

answers=("A","B","C","D")
his_answers=[]

for x in questions:
    for y in options:
        print(x)
        print()
        print(y)        
        inputs=input("enter the stuff")
        his_answers.append(inputs)