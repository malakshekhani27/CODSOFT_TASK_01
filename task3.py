import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_scores(user_score, computer_score):
    print(f"\nCurrent Scores => You: {user_score} | Computer: {computer_score}\n")

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock\n")

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors or q to quit): ").lower()

        if user_choice == 'q':
            print("Thanks for playing!")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"\n🧍 You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 'tie':
            print("🤝 It's a tie!")
        elif result == 'user':
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😞 You lose this round.")
            computer_score += 1

        display_scores(user_score, computer_score)

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("Game Over. Final Scores:")
            display_scores(user_score, computer_score)
            break

# Run the game
play_game()
