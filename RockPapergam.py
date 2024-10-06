import random
print("Welcome to Rock Paper Scissors Game ENJOY !!")
print("---------------------------------------------")
print("YOU CAN CHOOSE ANY rock🪨 , paper📃 , scissors✂️ ")

options={1:"rock🪨", 
         2:"paper📃", 
         3:"scissors✂️"}
player = -1
computer = options.get(random.randint(1,3))
while not player > 0 or not player <= 3:
    player = int(input("Enter Your Choice : "))

player = options.get(player)
print(f"your choice was {player}")
print(f"computer choice was {computer}")
if player == computer:
     print("ITS A TIE!!")
elif player == "rock🪨" and computer == "scissors✂️":
    print("YOU WIN !!")
elif player == "scissors✂️" and computer == "paper📃":
    print("YOU WIN !!")    
elif player == "paper📃" and computer == "rock🪨":
     print("YOU WIN !!")
else:
    print("COMPUTER WINS!!")