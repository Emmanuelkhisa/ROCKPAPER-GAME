from random import random, choice

print('''
 ---------------------------------------------------
|      --------- WELCOME TO THE GAME ---------      |
|           === ROCK, PAPER, SCISSOR ===            |
|                                                   |
 ---------------------------------------------------
''')

Choices = ['ROCK', 'PAPER', 'SCISSOR']
print(" ROCK,  PAPER OR  SCISSOR  ?")
print("\n")
user = input("YOUR CHOICE: ")
Computer = choice(Choices)

if user.upper() =="ROCK":
    if Computer =="PAPER":
        print("I FOLD YOU !! LOOOOOOOSSEEERRR")
    elif Computer == "SCISSOR":
        print("DANG !! YOU WIN")
    else:
        print("IT'S A DRAW")

elif user.upper() == "PAPER":
    if Computer == "ROCK":
        print("EASY ON ME !!, YOU WIN")
    elif Computer == "SCISSOR":
        print("NICE TO CUT YOU, LOOOOOOSSEEERR")
    else:
        print("I THINK IT'S A DRAW")

elif user.upper() == "SCISSOR":
    if Computer == "ROCK":
        print("HARD ON YOU, LOOOOOOSSEEERR !")
    elif Computer == "PAPER":
        print("CUTS, * YOU WIN *")
    else:
        print("DRAW, LET'S ROLL AGAIN")

else:
    print(f"INVALID >> *{user}* CHECK YOUR CHOICE AGAIN")

print(f'COMPUTER CHOICE IS: {Computer}')
