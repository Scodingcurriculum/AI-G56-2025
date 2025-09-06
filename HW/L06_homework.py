# L06_homework.py — While Loop Homework
# ------------------------------------
# Task: Ask the user for a password. Keep asking until the correct password "python123" is entered.

def main():
    print("=== Password Checker with While Loop ===")
    password = ""
    while password != "python123":
        password = input("Enter the password: ")
        if password != "python123":
            print("Incorrect password, try again!")
    print("Access Granted!")

if __name__ == "__main__":
    main()
