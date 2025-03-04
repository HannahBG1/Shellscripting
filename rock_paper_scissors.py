import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Please choose: rock, paper, or scissors: ").lower()

    if user_choice in choices:
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    play_game()
