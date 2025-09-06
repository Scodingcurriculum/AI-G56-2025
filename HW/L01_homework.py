# L01_homework.py
# Goal: Print a simple profile card using print(), strings, and escape sequences.
# Skills: print(), \n new lines, simple separators, neat formatting.
# Note: No input required—keep it simple and focused on formatting.

print("=== PROFILE CARD ===\n")  # Title + blank line for readability

# Three required lines (customize these strings in class to practice editing code)
print("Name: Your Name")
print("Grade: 5 or 6")
print("Statement: AI is the future of technology.")

# Extra: Show how a blank line is created before the separator
print("\n" + "-" * 20)  # 20 dashes

# Extra practice lines (optional—teachers can comment/uncomment during class)
print("\nFormatting Tips:")
print("\t• Use \\n for new lines.")
print("\t• Keep labels (Name/Grade) aligned for easy reading.")
print("\t• Try changing the text above to your real details!")

# Tiny recap block using one multi-line string
recap = (
    "\nRecap:\n"
    "• We used print() to display text.\n"
    "• We used \\n to add blank lines and make the output pretty.\n"
    "• We added a decorative separator made of dashes.\n"
)
print(recap)
