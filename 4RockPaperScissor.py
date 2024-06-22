import random

choices = ['rock', 'paper', 'scissors']

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
            (user == 'scissors' and computer == 'paper') or \
            (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'


def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("Choose one: rock, paper, or scissors")

        user_ch = input("Your choice: ").lower()

        if user_ch not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_ch = random.choice(choices)

        print("You chose:", user_ch)
        print("Computer chose: ",computer_ch)

        winner = determine_winner(user_ch, computer_ch)

        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print("Scores - You:", user_score, "Computer:", computer_score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
