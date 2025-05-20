from random import choice

print('''
 ---------------------------------------------------
|      --------- WELCOME TO THE GAME ---------      |
|           === ROCK, PAPER, SCISSOR ===            |
|                                                   |
 ---------------------------------------------------
''')

Choices = ['ROCK', 'PAPER', 'SCISSOR']

while True:
    print("\nROCK, PAPER OR SCISSOR?")
    user = input("YOUR CHOICE: ").upper()
    Computer = choice(Choices)

    if user == "ROCK":
        if Computer == "PAPER":
            print("I FOLD YOU !! LOOOOOOOSSEEERRR")
        elif Computer == "SCISSOR":
            print("DANG !! YOU WIN")
        else:
            print("IT'S A DRAW")

    elif user == "PAPER":
        if Computer == "ROCK":
            print("EASY ON ME !!, YOU WIN")
        elif Computer == "SCISSOR":
            print("NICE TO CUT YOU, LOOOOOOSSEEERR")
        else:
            print("I THINK IT'S A DRAW")

    elif user == "SCISSOR":
        if Computer == "ROCK":
            print("HARD ON YOU, LOOOOOOSSEEERR !")
        elif Computer == "PAPER":
            print("CUTS, * YOU WIN *")
        else:
            print("DRAW, LET'S ROLL AGAIN")

    else:
        print(f"INVALID >> *{user}* CHECK YOUR CHOICE AGAIN")

    print(f'COMPUTER CHOICE IS: {Computer}')

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("\nThanks for playing. Goodbye!")
        break
