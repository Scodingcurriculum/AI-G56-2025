# L11_homework.py — Rock–Paper–Scissors Auto Simulation (10 rounds)
# ---------------------------------------------------------------
# Task: Run 10 automatic rounds (simulate both user and computer moves),
# store results in a stats dictionary, and print a motivational 2-line message.

import random

VALID_MOVES = ("rock", "paper", "scissors")

def winner(user, comp):
    if user == comp: return "tie"
    if (user == "rock" and comp == "scissors") or        (user == "paper" and comp == "rock") or        (user == "scissors" and comp == "paper"):
        return "win"
    return "lose"

def main():
    print("=== RPS Auto Simulation — 10 Rounds ===")
    stats = {"wins": 0, "losses": 0, "ties": 0}
    for i in range(1, 11):
        user = random.choice(VALID_MOVES)
        comp = random.choice(VALID_MOVES)
        result = winner(user, comp)
        if result == "win": stats["wins"] += 1
        elif result == "lose": stats["losses"] += 1
        else: stats["ties"] += 1
        print(f"Round {i}: user={user}, comp={comp}, result={result}")
    total = sum(stats.values())
    print("\n--- Summary ---")
    print(f"Total rounds: {total}")
    print(f"Wins: {stats['wins']} | Losses: {stats['losses']} | Ties: {stats['ties']}")
    print("\nAI Learned from Data!\nNext time it will be smarter.")

if __name__ == "__main__":
    main()
