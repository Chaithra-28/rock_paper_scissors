import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:\n").casefold()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Invalid input. Please type Rock, Paper, or Scissors.")
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissor: 2
    computer_picks = options[random_number]
    print("Computer picked", computer_picks + ".")

    # Check for a tie first
    if user_input == computer_picks:
        print("It's a tie!")

    elif (user_input == "rock" and computer_picks == "scissors") or \
         (user_input == "paper" and computer_picks == "rock") or \
         (user_input == "scissors" and computer_picks == "paper"):
        print("You win!")
        user_wins += 1

    else:
        print("Computer Win!")
        computer_wins += 1

print(f"You: {user_wins} Computer: {computer_wins}")

print("Goodbye!")