import csv
import os
from random import choice


SCORE_FILE = 'rps_scores.csv'

if not os.path.exists(SCORE_FILE):
    with open(SCORE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Player Score', 'Computer Score', 'Draws', 'Result'])

print('''
 ---------------------------------------------------
|      --------- WELCOME TO THE GAME ---------      |
|           === ROCK, PAPER, SCISSOR ===            |
|                                                   |
 ---------------------------------------------------
''')

player_name = input("ENTER YOUR NAME: ").strip().title()

Choices = ['ROCK', 'PAPER', 'SCISSOR']

player_score = 0
computer_score = 0
draws = 0

while True:
    print("\nROCK, PAPER OR SCISSOR?")
    user = input("YOUR CHOICE: ").strip().upper()
    Computer = choice(Choices)

    if user not in Choices:
        print(f"INVALID >> *{user}* CHECK YOUR CHOICE AGAIN")
    else:
        print(f'COMPUTER CHOICE IS: {Computer}')
        
        if user == Computer:
            print("IT'S A DRAW")
            draws += 1
        elif (user == "ROCK" and Computer == "SCISSOR") or \
             (user == "PAPER" and Computer == "ROCK") or \
             (user == "SCISSOR" and Computer == "PAPER"):
            print("YOU WIN THIS ROUND!")
            player_score += 1
        else:
            print("COMPUTER WINS THIS ROUND!")
            computer_score += 1

    # Display current scores
    print(f"\nSCOREBOARD: {player_name} {player_score} | COMPUTER {computer_score} | DRAWS {draws}")

    # Play again?
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("\nGAME OVER!")
        print(f"\nFINAL SCORE: {player_name}: {player_score} | Computer: {computer_score} | Draws: {draws}")
        
        if player_score > computer_score:
            print(f"CONGRATULATIONS {player_name}, YOU'RE A CHAMPION!")
            result = "Win"
        elif player_score < computer_score:
            print("BETTER LUCK NEXT TIME!")
            result = "Loss"
        else:
            print("IT'S A DRAW OVERALL!")
            result = "Draw"

        # Save to CSV
        with open(SCORE_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([player_name, player_score, computer_score, draws, result])
        
        break

# Show Wall of Fame from CSV
print("\n=== 🎉 WALL OF FAME (Past Winners) 🎉 ===")

with open(SCORE_FILE, mode='r') as file:
    reader = csv.DictReader(file)
    winners = [row['Name'] for row in reader if row['Result'] == 'Win']

if winners:
    for winner in set(winners):
        print(f"🏆 {winner}")
else:
    print("No winners recorded yet.")
