# -------------------------------------------------------------
# Lesson 13 – Introduction to Supervised Learning (Homework)
# Task: Build a tiny "examples list" and make a simple prediction.
# Level: Grade 5–6  |  Keep it simple and neat.
# -------------------------------------------------------------

print("=== Lesson 13: Labeled Examples Explainer ===")
print("We will collect 5 examples like: animal -> sound OR fruit -> color")
print("-" * 55)

# Two lists to store inputs and labels (like X and y)
inputs_list = []
labels_list = []

# 1) Collect 5 pairs from the user
print("Enter 5 pairs. Example: 'cat' and 'meow'  OR  'apple' and 'red'")
for i in range(1, 6):
    print("-" * 25, "Pair", i, "-" * 25)
    x = input("Enter example input (e.g., animal/fruit): ").strip().lower()
    y = input("Enter its label (e.g., sound/color): ").strip().lower()
    inputs_list.append(x)
    labels_list.append(y)

print("\n=== Your Example Table ===")
print("No. | Input -> Label")
print("-" * 25)
for i in range(len(inputs_list)):
    print(str(i+1) + ". ", inputs_list[i], "->", labels_list[i])

# 2) Ask for a new input and try to predict by exact match
print("-" * 55)
new_item = input("Type a new input to predict its label: ").strip().lower()

predicted = "Not sure yet"
# Try exact match
for i in range(len(inputs_list)):
    if new_item == inputs_list[i]:
        predicted = labels_list[i]
        break

print("\n=== Prediction Result ===")
print("Input :", new_item)
print("Guess :", predicted)

# 3) Reflection lines – what did we learn?
print("\n=== What I Learned ===")
print("1) Supervised learning uses input and correct label examples.")
print("2) The computer looks at pairs like (cat -> meow).")
print("3) When it sees a new input, it tries to guess the label.")

# 4) Save a tiny report to a text file (optional but nice)
report_name = "my_examples_report.txt"
with open(report_name, "w", encoding="utf-8") as f:
    f.write("My Examples Report\n")
    f.write("-------------------\n")
    for i in range(len(inputs_list)):
        f.write(f"{i+1}. {inputs_list[i]} -> {labels_list[i]}\n")
    f.write("\nNew input: " + new_item + "\n")
    f.write("Prediction: " + predicted + "\n")

print("\nSaved report to:", report_name)
print("Done! Great work. :)")
