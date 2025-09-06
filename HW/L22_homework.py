# ------------------------------------------------------------------
# Lesson 22 – Add Reset + Improve UI (Text UI Homework)
# Task: Options: ADD DATA, PREDICT, RESET, SHOW DATA, EXIT
# Level: Grade 5–6 | Confidence tags and a disclaimer.
# ------------------------------------------------------------------

print("=== AI Doctor Text UI (with RESET) ===")
print("Disclaimer: This is an AI-style demo. Consult a doctor for real advice.")
print("-" * 65)

symptoms_list = []
disease_list = []

def tag_for(score):
    if score >= 3:
        return "[HIGH]"
    if score == 2:
        return "[MEDIUM]"
    return "[LOW]"

def predict(user_line):
    user_words = user_line.split()
    best_score = -1
    best_dis = "Not sure"
    for i in range(len(symptoms_list)):
        row_words = symptoms_list[i].split()
        score = 0
        for w in user_words:
            if w in row_words:
                score += 1
        if score > best_score:
            best_score = score
            best_dis = disease_list[i]
    if best_score <= 0:
        best_dis = "Not sure"
    return best_dis, best_score

def show_table():
    print("No. | Symptoms                | Disease")
    print("-" * 40)
    for i in range(len(symptoms_list)):
        print(f"{i+1:>2}. | {symptoms_list[i]:<22} | {disease_list[i]}")

while True:
    print("\n[1] ADD DATA  [2] PREDICT  [3] RESET  [4] SHOW DATA  [5] EXIT")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        for i in range(1, 4):
            s = input(f"Row {i} symptoms: ").strip().lower()
            d = input(f"Row {i} disease : ").strip().lower()
            symptoms_list.append(s)
            disease_list.append(d)
        print("Data added.")

    elif choice == "2":
        line = input("Enter symptoms: ").strip().lower()
        result, score = predict(line)
        print("Prediction:", result, tag_for(score))

    elif choice == "3":
        symptoms_list = []
        disease_list = []
        print("All data cleared.")

    elif choice == "4":
        if len(symptoms_list) == 0:
            print("No data yet.")
        else:
            show_table()

    elif choice == "5":
        print("Exiting. Stay healthy!")
        break

    else:
        print("Please choose 1, 2, 3, 4, or 5.")

    # Always show disclaimer at bottom
    print("Disclaimer: This is an AI-based prediction demo. Consult a doctor for real advice.")
