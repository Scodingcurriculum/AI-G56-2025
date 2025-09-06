# L03_homework.py
# Goal: Ask for favorite subject and hobby; print a friendly two-line summary.
# Skills: input(), .strip(), f-strings, tidy headings.

print("=== Quick Interests ===\n")
subject = input("Enter your favorite subject: ").strip()
hobby = input("Enter your favorite hobby: ").strip()

print("\n" + "-" * 40)
print("Summary:")
print(f"You enjoy {subject} and love {hobby}.")
print("Learning is fun!")
print("-" * 40)

# Extra guided prompt (helps kids think and extend)
print("\nTry this:")
print("• Change the subject and hobby above and run the program again.")
print("• Add one more print line that explains WHEN you enjoy your hobby.")
