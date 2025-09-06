# ------------------------------------------------------------------
# Lesson 23 – Intro to GitHub & Troubleshooting (Homework)
# Task: Print a README preview and a tiny troubleshooting helper.
# Level: Grade 5–6 | Simple inputs, prints, and a small loop menu.
# ------------------------------------------------------------------

print("=== Lesson 23: README & Troubleshooting Preview ===")
print("-" * 60)

# 1) Collect README info
title = input("Project Title: ").strip()
desc1 = input("Short description (line 1): ").strip()
desc2 = input("Short description (line 2): ").strip()

print("\nEnter 3 file names you would upload (e.g., app.py, data.csv):")
file1 = input("File 1: ").strip()
file2 = input("File 2: ").strip()
file3 = input("File 3: ").strip()

# 2) Print a README-style preview
print("\n# " + title)
print("## Description")
print(desc1)
print(desc2)
print("\n## Files")
print("-", file1)
print("-", file2)
print("-", file3)
print("\n## How to Run")
print("1) Open the folder")
print("2) Run: python", file1 if file1 else "main.py")
print("3) Follow on-screen steps")

# 3) Tiny troubleshooting helper (choose two problems)
def tip_for(choice):
    if choice == "1":
        return "Check the file name and the folder path. Use correct spelling."
    if choice == "2":
        return "Type symptoms like: fever cough (two words separated by space)."
    if choice == "3":
        return "Read the last printed line. Fix the input or restart the program."
    return "Pick 1, 2, or 3."

print("\n## Troubleshooting")
for n in range(1, 3):
    print("\nChoose a problem to get a tip:")
    print("1) File not found")
    print("2) Wrong input format")
    print("3) Program exited early")
    ch = input("Your choice: ").strip()
    print("Tip:", tip_for(ch))

# 4) End with 3 things GitHub helps you do
print("\n## Why GitHub? (3 benefits)")
print("1) Share code with others easily.")
print("2) Track changes over time.")
print("3) Collaborate with friends and teammates.")
print("\nGreat job! This looks ready for a real README soon.")
