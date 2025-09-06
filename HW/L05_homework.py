# L05_homework.py — For Loop Homework
# ----------------------------------
# Task: Print the first 10 even numbers using a for loop, then print their total sum.

def main():
    print("=== First 10 Even Numbers ===")
    total = 0
    for i in range(2, 21, 2):  # step by 2 to get even numbers
        print(i)
        total += i
    print(f"\nSum of these even numbers = {total}")

if __name__ == "__main__":
    main()
