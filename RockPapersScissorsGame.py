# Rock Papers Sciessors game

import random
choices = ["Rock", "Paper", "Scissors"]
result = [[0, "Draw"], [1, "Computer win"], [2, "Player win"]]

def Matchmaking(computer_choice, user_choice):
    # Comments are given in order of: {computer} vs {player}
    # Rock vs Rock, Paper vs Paper and Scissors vs Scissors
    if computer_choice == user_choice:
        round_result = result[0]

    # Rock vs Paper
    elif computer_choice == 0 and user_choice == 1:
        round_result = result[2]
    # Rock vs Scissors
    elif computer_choice == 0 and user_choice == 2:
        round_result = result[1]


    # Paper vs Rock
    elif computer_choice == 1 and user_choice == 0:
        round_result = result[1]
    # Paper vs Scissors
    elif computer_choice == 1 and user_choice == 2:
        round_result = result[2]


    # Scissors vs Rock
    elif computer_choice == 2 and user_choice == 0:
        round_result = result[2]
    # Scissors vs Paper
    elif computer_choice == 2 and user_choice == 1:
        round_result = result[1]

    # Fallback to a draw, in case matchmaking fails
    else:
        round_result = result[0]


    return round_result


user_health = 3
wins = 0

print("This is a Rock, Papers, Scissors game. Enter your choice below. You have 3 lives. Win three games to claim VICTORY")

while user_health > 0 and wins < 3:
    computer_choice = random.randint(0,2)
    
    print (computer_choice)

    user = int(input("\n Rock(1), Papers(2) or Scissors(3): "))
    user_choice = (user - 1)

    Result = Matchmaking(computer_choice, user_choice)

    if Result[0] == 0:
        print (result[0][1])
    
    elif Result [0] == 1:
        print (result[1][1])
        user_health -= 1

    elif Result [0] == 2:
        print (result[2][1])
        wins += 1

if user_health == 0:
    print("\nDEFEAT. This is disappointing")

if user_health > 0 and wins == 3:
    print("\n\nVICTORY")
    print(f'lives remaining: {user_health}/3')