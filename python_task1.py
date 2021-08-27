import random
 
def cont():
    q=input('do u wanna play again?(yes/no):').lower()
    if q=='yes':
        main()
    elif q=='no':
        exit()
    else:
        print('Invalid input.Please try again')
        cont()
 
def main():
    print('''this is a man vs computer cricket game.There are some rules:-
1.you can only enter 1 and 2 for the toss
2.you can enter numbers from 1 to 10 while batting or balling
if u dont follow these the game will restart''')
    o=int(input("The number of overs are: "))
    def batp():  
        i=1
        print('The computer is bowling')
        total = 0
        while i<=o*6:
 
            match = random.randint(1, 6)
            computer = random.randint(1, 6)
            player = int(input("Play your shot: "))
            if player>6:
                print('u arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Computer plays: ", computer)
            total = total + player
 
            if (computer == player):
                print("Number Matched! ..out!!!")
                print("Your total runs =", total)
                i=i+1
                break
 
        print('the computer needs ', total+1, 'runs to win!')
 
        print('it is computers time to bat.')
        ctotal = 0
        while i<=o*6:
 
            cmatch = random.randint(1, 6)
            computer = random.randint(1, 6)
            player = int(input("put your ball: "))
            if player>6:
                print('u arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Computer plays: ", computer)
            ctotal = ctotal + computer
            
 
            if (computer == player):
                print("Number Matched! ..out!!!")
                print("computer's total runs =", ctotal)
                if ctotal>total:
                    print('you lose!')
                elif total>ctotal:
                    print('you win!')
                else:
                    print('tie!')
                    i=i+1
                break
            
    def bat2():
        j=1
        print('it is computers time to bat.')
        ctotal = 0
        while j<=0*6:
 
            cmatch = random.randint(1, 6)
            computer = random.randint(1, 6)
            player = int(input("put your ball: "))
            if player>6:
                print('u arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Computer plays: ", computer)
            ctotal = ctotal + computer
            
            if (computer == player):
                print("Number Matched! ..out!!!")
                print("computer's total runs =", ctotal)
                j=j+1
                break
 
        print('The computer is bowling')
        total = 0
        while j<=o*6:
 
            match = random.randint(1, 6)
            computer = random.randint(1, 6)
            player = int(input("Play your shot: "))
            if player>6:
                print('u arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Computer plays: ", computer)
            total = total + player
 
            if (computer == player):
                print("Number Matched! ..out!!!")
                print("Your total runs =", total)
                if ctotal>total:
                    print('you lose!')
                elif total>ctotal:
                    print('you win!')
                else:
                    print('tie!')
                    j=j+1
                break
 
    def toss():
        x=input('what do u want? (head/tail):').lower()
        y=int(input('play your number for the toss(1/2):'))
        if y>2:
            print('u are only allowed to use 1 and 2.')
            toss()
        z=random.randint(1,2)
        print('the computer has played',z,'for the toss')
        if x=='tail':
            if ((y+z)%2)==0:
                print('you have won the toss')
                a=input('what do u want?(bat/bowl)').lower()
                if a=='bat':
                    bat1()
                elif a=='bowl':
                    bat2()
                else:
                    print('invalid input.The game will restart')
                    toss()
            else:
                x=random.choice(['bat','bowl'])
                if x=='bat':
                    print('The computer chooses to bat!')
                    bat2()
                elif x=='bowl':
                    print('The computer chooses to bowl!')
                    bat1()
        elif x=='head':
            if ((y+z)%2)==0:
                y=random.choice(['bat','bowl'])
                if y=='bat':
                    print('The computer chooses to bat!')
                    bat2()
                elif y=='bowl':
                    print('The computer chooses to bowl!')
                    bat1()
                
            else:
                print('you have won the toss')
                a=input('what do u want?(bat/bowl)').lower()
                if a=='bat':
                    bat1()
                elif a=='bowl':
                    bat2()
                else:
                    print('invalid input.The game will restart')
                    toss()
        else:
             print('invalid input.The game will restart')
             toss()
 
 
 
 
 
    toss()
    cont()
 
main()
