# L10_homework.py — Rock–Paper–Scissors Frequency Predictor (5 rounds)
# --------------------------------------------------------------------
# Task: Ask user for 5 moves. Store them, print the most frequent move,
# and the AI's counter move. Show a neat summary at the end.

VALID_MOVES = ("rock", "paper", "scissors")

def counter_move(m):
    if m == "rock":
        return "paper"
    if m == "paper":
        return "scissors"
    return "rock"

def main():
    print("=== RPS Frequency Predictor — Homework (5 rounds) ===")
    moves = []
    for i in range(1, 6):
        mv = input(f"Move {i} (rock/paper/scissors): ").strip().lower()
        if mv not in VALID_MOVES:
            print("Invalid. Try again."); return
        moves.append(mv)
    # count frequencies manually (grade-friendly)
    counts = {"rock": 0, "paper": 0, "scissors": 0}
    for m in moves:
        counts[m] += 1
    most = max(counts, key=counts.get)
    print("\n--- Summary ---")
    print("Your moves:", moves)
    print("Counts:", counts)
    print("Most frequent:", most)
    print("AI would counter with:", counter_move(most))
    print("----------------")

if __name__ == "__main__":
    main()
