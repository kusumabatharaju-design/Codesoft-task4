import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")
print("Instructions:")
print("Type rock, paper, or scissors to play\n")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    computer_choice = random.choice(choices)

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: You lose!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break

    print()
