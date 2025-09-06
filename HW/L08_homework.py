# L08_homework.py
# Goal: Ask 3 questions (sport, subject, food) and print a neat one-line summary.
# Skills: inputs, .strip(), f-strings, headings and separators.

print("=== Survey Results ===\n")
sport = input("Favorite sport: ").strip()
subject = input("Favorite subject: ").strip()
food = input("Favorite food: ").strip()

print("\n" + "-" * 40)
print("Survey Results")
print("-" * 40)
print(f"You like {sport}, enjoy {subject}, and love eating {food}.")
print("-" * 40)

# Mini extension idea:
# Try adding one more question like "Favorite color" and include it in the summary!
