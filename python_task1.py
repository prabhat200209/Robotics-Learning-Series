import random

def conti():
    p=input('do u wanna play again?(yes/no):').lower()
    if p=='yes':
     main()
    elif p=='no':
        exit()
    else:
        print('Invalid input.Please try again')
    conti()




def batp():  
        print("It's time for the player to Bat")
        total = 0
        while (True):

            match = random.randint(1, 6)
            computer = random.randint(1, 6)
            player = int(input("Play your shot: "))
            if player>6:
                print('u arent allowed to play any number more than 6.The game will restart now')
                batp()

            print("Computer plays: ", computer)
            total = total + player
            if (computer == player):
                print("Number Matched! ..out!!!")
                print("Your total runs =", total)
                break
           

        print('The computer needs ', total+1, 'runs to win!')

        print('The computer is batting.')
        ctotal = 0
        while (True):

            cmatch = random.randint(1, 6)
            computer = random.randint(1, 6)
            player = int(input("put your ball: "))
            print("Computer plays: ", computer)
            ctotal = ctotal + computer


            if (computer == player):
                    print("Number Matched! ..out!!!")
                    print("computer's total runs =", ctotal)
            break
        if ctotal>total:
                    print('Oops! you lose!')
        elif total>ctotal:
                    print('Hurray! you win!')
        else:
                    print('tie!')





def batc():
    print("It's time for the computer to Bat.")
    ctotal = 0
    while (True):

        cmatch = random.randint(1, 6)
        computer = random.randint(1, 6)
        player = int(input("Bowl: "))
        if player>6:
                print('u arent allowed to play any number more than 6.The game will restart now')
                batc()
        print("Computer plays: ", computer)
        ctotal = ctotal + computer

        if (computer == player):
                print("Number Matched! ..out!!!")
                print("computer's total runs =", ctotal)
        break

    print('The computer is bowling')
    total = 0
    while (True):

                match = random.randint(1, 6)
                computer = random.randint(1, 6)
                player = int(input("Play your shot: "))
                print("Computer plays: ", computer)
                total = total + player

                if (computer == player):
                    print("Number Matched! ..out!!!")
                print("Your total runs =", total)
                break
    if ctotal>total:
        print('you lose!')
    elif total>ctotal:
        print('you win!')
    else:
        print('tie!')




def main():
    print('''this is a man vs computer cricket game.There are some rules:-
1.you can only enter 1 and 2 for the toss
2.you can enter numbers from 1 to 6 while batting or balling
if u dont follow these the game will restart''')


print("Here,Time for toss\nEnter 0 for Heads and 1 for Tails")
y=int(input())
z=random.randint(0,1)
if(y==z):
    print("Hurray! You have won the toss.")
    print("Choose Batting or Bowling (1 for batting and 0 for bowling)")
x=int(input())
if(x==0):
    print("you choose to bowl")
    batc()

elif(x!=0):
    print("you choose to bat")
    batp()
else:
    print("Oops! You have lost the toss.")
rn=random.randint(0,1)
if(rn==0):
    print("computer choose to bowl")
    batp()
elif(rn==1):
        print("computer choose to bat")
        batc()
        conti()
          
