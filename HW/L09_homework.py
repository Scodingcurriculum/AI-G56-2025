# Lesson 9 Homework: Mini Journal
# -------------------------------
# Homework Task:
#   - Ask the user for their favorite color, hobby, and time of day.
#   - Clean inputs (strip/title).
#   - Print a one-line summary using f-strings.
#   - Append the entry to "journal_log.txt" with timestamp.
#   - End with a friendly 2-line message.

from datetime import datetime

def main():
    print("=== Mini Journal Program ===\n")

    # --- Collect Inputs ---
    color = input("Enter your favorite color: ").strip().title()
    hobby = input("What is your favorite hobby? ").strip().title()
    time_of_day = input("What is your favorite time of day? ").strip().lower()

    # --- Format Summary ---
    summary = f"You love {color}, enjoy {hobby}, and prefer {time_of_day}."

    print("\n--- Your Journal Entry ---")
    print(summary)

    # --- Save to journal_log.txt ---
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {summary}\n")

    # --- Closing Friendly Message ---
    print("\nThanks for sharing!\nSee you next time!")

if __name__ == "__main__":
    main()
