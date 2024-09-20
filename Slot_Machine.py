import random

def spin_row(): 
    symbols=['🍒', '🍎', '🍌', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def payout(row,bet):
    if row[0]==row[1]==row[2]:
       if row[0]=='🍒':
          return bet*2
       elif row[0]=='🍎':
           return bet*3
       elif row[0]=='🍌':
           return bet*4
       elif row[0]=='⭐':
           return bet*5
    else:
        return 0



def main():
    balance=100
    print("*********************************************")
    print("----------This is A Slot Machine-------------")
    print("Symbols : 🍒 🍎 🍌 ⭐")
    print("*********************************************")
    while balance>0:
        bet=input("Enter the amount of the bet :")
        if not bet.isdigit():
            print("Enter a valid input :")
            continue

        bet=int(bet)

        if bet>balance:
            print("insuffiecient balance")
            continue

        if bet <= 0:
            print("Bet must me greater than zero")
            continue

        balance-=bet
        print(f"Current Balance :${balance}")

        row=spin_row()
        print("Spinning.......")
        print_row(row)

        payout1=payout(row,bet)
        if payout1>0:
            balance+=bet
            print(f"congrats you won ${payout1} !!")
        else:
            
            print(f"you lost the round !!")
        print(f"{balance}")
        

if __name__ == '__main__':
    main()