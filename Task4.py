#                                                Task 4
# Rock-Paper-Scissors Game
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock beats scissors, scissors beat paper, and paper beats rock.")

    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print("\nRound", round_number)
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chooses:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print("Your score:", user_score)
        print("Computer's score:", computer_score)

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nFinal Scores:")
            print("Your score:", user_score)
            print("Computer's score:", computer_score)
            if user_score > computer_score:
                print("Congratulations! You won the game!")
            elif user_score < computer_score:
                print("Sorry, you lost the game. Better luck next time!")
            else:
                print("It's a tie game!")
            break

        round_number += 1

if __name__ == "__main__":
    main()
