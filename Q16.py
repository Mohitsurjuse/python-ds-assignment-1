#Rock-Paper-Scissors: Use dict for choices, loop 5 rounds with random (import random), track wins with set
import random
choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}  # Dict for choices
userWins = set()  # Set to track user wins
print('Welcome to Rock-Paper-Scissors Lets play 5 rounds.')
for round in range(1, 6):
    userChoice = int(input(f'Round {round} - Enter your choice (1: Rock, 2: Paper, 3: Scissors): '))
    while userChoice not in choices:
        userChoice = int(input('Only 1, 2, or 3 are allowed. Please select 1, 2, or 3: '))
    
    computerChoice = random.int(1, 3)  # Random choice for computer
    print(f'You chose {choices[userChoice]}, Computer chose {choices[computerChoice]}.')

    # Determine winner
    if userChoice == computerChoice:
        print('It is a tie')
    elif (userChoice == 1 and computerChoice == 3) or (userChoice == 2 and computerChoice == 1) or (userChoice == 3 and computerChoice == 2):
        print('You win this round')
        userWins.add(round)  # Add round number to wins set
    else:
        print('Computer wins this round')
print(f'You won {len(userWins)} out of 5 rounds')