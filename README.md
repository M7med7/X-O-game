Tic-Tac-Toe Game (X-O Game) 🎮

This is a classic Tic-Tac-Toe game implemented in Python with the Tkinter library, allowing players to play against a computer opponent. The game features a modern and responsive GUI, making it engaging and easy to play.
Game Description

The game is played on a 3x3 grid. Players take turns marking an empty cell with their symbol, either "X" or "O". The goal is to align three of your symbols in a row, column, or diagonal before your opponent does. In this version, the player can choose to play as "X" or "O", with the computer taking the other symbol.

The AI opponent is designed to be challenging by implementing basic strategies:

    Winning Move: The computer checks if it can win in the current turn.
    Blocking Move: If the player is close to winning, the computer blocks the move.
    Random Move: When no immediate winning or blocking move is required, the computer makes a random move.

Features

    Choice of Symbol: Players can choose to play as "X" or "O" at the start.
    Intuitive Interface: Simple and clean 3x3 grid with large buttons for easy play.
    Reset and Exit Options: Players can restart the game or exit anytime.
    Responsive AI: The computer opponent responds with strategic moves to ensure a challenging experience.
    End-of-Game Alerts: Pop-up messages announce the winner or a draw.

How to Play

    Run the program, and you'll be prompted to select your symbol ("X" or "O").
    Click on any empty cell to place your symbol.
    The computer will make its move, and the game continues in turns.
    The first to align three symbols in a row, column, or diagonal wins.
    Use the "Restart" button to reset the game or "Exit" to close the application.

Technologies Used

    Python: Core programming language used.
    Tkinter: GUI library for creating the interface.
    Random: Used for AI’s random move selection when needed.

Code Overview

The code is structured as follows:

    Choice Screen: The player selects their symbol, and the game board is created.
    Game Logic: Handles player moves, computer moves, win conditions, and draws.
    AI Strategy: Simple AI that prioritizes winning and blocking moves, with fallback to random moves.
    Game Controls: Buttons for restarting or exiting the game.
