🪨 Rock, Paper, Scissors Game (Python)

A simple Rock, Paper, Scissors game built using Python.
The user plays against the computer in the terminal.

📌 How the Game Works

The computer randomly selects:

Rock

Paper

Scissor

The user enters:

r → Rock

p → Paper

s → Scissor

The program compares both choices and prints:

✅ You Win!

❌ You Lose!

🤝 It's a draw!

🎮 Game Rules
Player	Computer	Result
Rock	Scissor	You Win
Rock	Paper	You Lose
Paper	Rock	You Win
Paper	Scissor	You Lose
Scissor	Paper	You Win
Scissor	Rock	You Lose
🧠 Logic Used

The program:

Uses random.choice() for computer selection

Maps choices using a dictionary:

{"r": 1, "p": 0, "s": -1}


Uses conditional logic to determine the winner

Optimized version uses mathematical difference:

computer - you

🛠️ Technologies Used

Python 3

Random Module

🚀 How to Run

Make sure Python is installed

Open terminal in project folder

Run:

python main.py


Enter your choice:

r / p / s

📂 Project Structure
rock-paper-scissor/
│── main.py
│── README.md

🎯 Example Output
Enter your choice: r
You choose Rock and Computer choose Paper
You Lose!

📌 Future Improvements

Add score tracking

Add replay option

Add GUI version (Tkinter / Pygame)

Handle invalid input safely

Convert into web version
