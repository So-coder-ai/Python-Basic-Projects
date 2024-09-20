import random
print("Welcome to Rock Paper Scissors Game ENJOY !!")
print("---------------------------------------------")
print("YOU CAN CHOOSE ANY (rock ,paper,scissors)")
options=("rock","paper","scissors")
player=None
computer=random.choice(options)
while player not in options:
    player=input("enter a choice: ")

print(f"your choice was {player}")
print(f"computer choice was {computer}")
if player==computer:
    print("ITS A TIE!!")
elif player=="rock" and computer=="scissors":
    print("YOU WIN !!")
elif player=="scissors"and computer=="paper":
    print("YOU WIN !!")    
elif player=="paper" and computer == "rock":
    print("YOU WIN !!")
else:
    print("COMPUTER WINS!!")