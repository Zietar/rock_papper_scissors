import random
import tkinter as tk


def get_bot_choice():
    list = ["rock", "paper", "scissors"]
    return random.choice(list)


def set_player_choice(choice):
    global player_choice
    global bot_choice

    player_choice = choice
    bot_choice = get_bot_choice()

    player_choice_label.config(text=choice)
    bot_choice_label.config(text=bot_choice)

    determine_outcome()


def determine_outcome():
    global player_score_value, bot_score_value
    if player_choice == bot_choice:
        outcome_label.config(text="Draw!")
    elif (
        (player_choice == "rock" and bot_choice == "scissors")
        or (player_choice == "scissors" and bot_choice == "paper")
        or (player_choice == "paper" and bot_choice == "rock")
    ):
        outcome_label.config(text="You win!")
        player_score_value += 1
        player_score.config(text=str(player_score_value))
    else:
        outcome_label.config(text="You lose!")
        bot_score_value += 1
        bot_score.config(text=str(bot_score_value))

    if player_score_value == 2:
        outcome_label.config(text="The Final winner is The Player!")
        toggle_buttons(False)
    elif bot_score_value == 2:
        outcome_label.config(text="The Final winner is Bot!")
        toggle_buttons(False)


def play_again():
    global player_score_value, bot_score_value
    player_score_value, bot_score_value = 0, 0
    player_score.config(text=str(player_score_value))
    bot_score.config(text=str(bot_score_value))
    outcome_label.config(text="...")
    toggle_buttons(True)


def toggle_buttons(state):
    rock_button.config(state="normal" if state else "disabled")
    paper_button.config(state="normal" if state else "disabled")
    scissors_button.config(state="normal" if state else "disabled")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x170")

player_choice = ""
bot_choice = ""
player_score_value = 0
bot_score_value = 0

# 0 row
rock_button = tk.Button(root, text="Rock", command=lambda: set_player_choice("rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: set_player_choice("paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: set_player_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# 1 row

player_name_label = tk.Label(root, text="Player:")
player_name_label.grid(row=1, column=0, padx=5, pady=5)

player_choice_label = tk.Label(root, text="")
player_choice_label.grid(row=1, column=1, padx=5, pady=5)

player_score = tk.Label(root, text="0")
player_score.grid(row=1, column=2, padx=5, pady=5)


# 2 row
bot_name_label = tk.Label(root, text="Bot:")
bot_name_label.grid(row=2, column=0, padx=5, pady=5)

bot_choice_label = tk.Label(root, text="")
bot_choice_label.grid(row=2, column=1, padx=5, pady=5)

bot_score = tk.Label(root, text="0")
bot_score.grid(row=2, column=2, padx=5, pady=5)

# 3 row
outcome_label = tk.Label(root, text="...")
outcome_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 4 row
play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()