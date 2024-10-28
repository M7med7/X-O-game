import tkinter as tk
from tkinter import messagebox
import random

Screen = tk.Tk()
Screen.title("X O Game")
Screen.geometry("1920x1080")
Screen.resizable(False, False)

player_symbol = None
computer_symbol = None
table = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
choice_frame = None
game_frame = None
control_frame = None

def reset_game():
    global table, player_symbol, computer_symbol
    for i in range(3):
        for j in range(3):
            table[i][j] = ""
            buttons[i][j].config(text="")
    player_symbol = None
    computer_symbol = None
    game_frame.destroy()
    control_frame.destroy()
    create_choice_screen()

def exit_game():
    Screen.destroy()

def check_winner():
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != "":
            Screen.after(100, lambda: messagebox.showinfo("Game Over", f"{table[i][0]} WON!"))
            return True
    
    for j in range(3):
        if table[0][j] == table[1][j] == table[2][j] != "":
            Screen.after(100, lambda: messagebox.showinfo("Game Over", f"{table[0][j]} WON!"))
            return True
    
    if table[0][0] == table[1][1] == table[2][2] != "":
            Screen.after(100, lambda: messagebox.showinfo("Game Over", f"{table[1][1]} WON!"))
            return True
    if table[0][2] == table[1][1] == table[2][0] != "":
            Screen.after(100, lambda: messagebox.showinfo("Game Over", f"{table[1][1]} WON!"))
            return True
    
    if all(table[i][j] != "" for i in range(3) for j in range(3)):
        Screen.after(100, lambda: messagebox.showinfo("Game Over", "It's a draw!"))
        return True
        
    return False

def get_winning_move(board, symbol):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = symbol
                if (any(all(board[i][k] == symbol for k in range(3)) for i in range(3)) or
                    any(all(board[k][j] == symbol for k in range(3)) for j in range(3)) or
                    all(board[i][i] == symbol for i in range(3)) or
                    all(board[i][2-i] == symbol for i in range(3))):
                    board[i][j] = ""
                    return (i, j)
                board[i][j] = ""
    return None

def computer_move():
    winning_move = get_winning_move(table, computer_symbol)
    if winning_move:
        i, j = winning_move
    else:
        blocking_move = get_winning_move(table, player_symbol)
        if blocking_move:
            i, j = blocking_move
        else:
            empty_cells = [(i,j) for i in range(3) for j in range(3) if table[i][j] == ""]
            if empty_cells:
                i, j = random.choice(empty_cells)
            else:
                return

    table[i][j] = computer_symbol
    buttons[i][j].config(text=computer_symbol)
    Screen.after(100, check_winner)

def button_click(i, j):
    if table[i][j] == "" and not check_winner():
        table[i][j] = player_symbol
        buttons[i][j].config(text=player_symbol)
        
        if not check_winner():
            Screen.after(100, computer_move)

def create_board():
    global game_frame, control_frame
    game_frame = tk.Frame(Screen)
    game_frame.place(relx=0.5, rely=0.45, anchor="center")
    
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(game_frame, text="", font=('Arial', 40), width=5, height=2,
                                    command=lambda row=i, col=j: button_click(row, col))
            buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

    control_frame = tk.Frame(Screen)
    control_frame.place(relx=0.5, rely=0.8, anchor="center")
    
    restart_button = tk.Button(control_frame, text="Restart", font=('Arial', 20), width=10,
                             command=reset_game)
    restart_button.pack(side=tk.LEFT, padx=10)
    
    exit_button = tk.Button(control_frame, text="Exit", font=('Arial', 20), width=10,
                           command=exit_game)
    exit_button.pack(side=tk.LEFT, padx=10)

def choose_symbol(symbol):
    global player_symbol, computer_symbol, choice_frame
    player_symbol = symbol
    computer_symbol = "O" if symbol == "X" else "X"
    choice_frame.destroy()
    create_board()
    if computer_symbol == "X":
        Screen.after(100, computer_move)

def create_choice_screen():
    global choice_frame
    choice_frame = tk.Frame(Screen)
    choice_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    label = tk.Label(choice_frame, text="Choose your symbol:", font=('Arial', 20))
    label.pack(pady=20)
    
    x_button = tk.Button(choice_frame, text="X", font=('Arial', 30), width=5, height=2,
                        command=lambda: choose_symbol("X"))
    x_button.pack(side=tk.LEFT, padx=10)
    
    o_button = tk.Button(choice_frame, text="O", font=('Arial', 30), width=5, height=2,
                        command=lambda: choose_symbol("O"))
    o_button.pack(side=tk.LEFT, padx=10)

create_choice_screen()
Screen.mainloop()
