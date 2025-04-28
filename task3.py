import tkinter as tk
import random

# Game logic
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Reset game scores
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Choose Rock, Paper, or Scissors to start playing!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Create window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x300")
window.config(bg="#f0f0f0")

title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

result_label = tk.Label(window, text="Choose Rock, Paper, or Scissors to start playing!", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Reset Button
reset_btn = tk.Button(window, text="Play Again", command=reset_game)
reset_btn.pack(pady=20)

window.mainloop()
