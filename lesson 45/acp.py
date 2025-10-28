import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Button click functions
def choose_rock():
    determine_winner('rock')

def choose_paper():
    determine_winner('paper')

def choose_scissors():
    determine_winner('scissors')

def play_again():
    result_label.config(text="Make your move!")



# Heading
heading = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
heading.pack(pady=10)

# Buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=choose_rock)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=choose_paper)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=choose_scissors)
scissors_button.grid(row=0, column=2, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Score
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

again_button = tk.Button(root, text="Play Again", command=play_again)
again_button.pack(pady=10)

# Exit button at bottom-right
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

# Run the application
root.mainloop()
