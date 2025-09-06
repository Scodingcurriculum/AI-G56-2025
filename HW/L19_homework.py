# ------------------------------------------------------------------
# Lesson 19 – Improve AI Doctor with New Data (Homework)
# Task: Compare accuracy BEFORE and AFTER adding new pairs.
# Level: Grade 5–6 | Uses word matching + yes/no correctness tally.
# ------------------------------------------------------------------

print("=== Lesson 19: More Data, Better Results? ===")
print("We will first use 6 starter pairs, then add 6 more and compare.")
print("-" * 60)

# Starter dataset (6 rows)
base_symptoms = [
    "fever cough",
    "runny nose sneezing",
    "headache stress",
    "sore throat fever",
    "itchy eyes sneezing",
    "stomach pain"
]
base_diseases = [
    "flu",
    "cold",
    "stress",
    "tonsillitis",
    "allergy",
    "indigestion"
]

# Add more data (6 rows) entered by the student
new_symptoms = []
new_diseases = []
for i in range(1, 7):
    print("-" * 15, "Add Row", i, "-" * 15)
    s = input("Symptoms (e.g., 'fever cough'): ").strip().lower()
    d = input("Disease  (one word, e.g., 'flu'): ").strip().lower()
    new_symptoms.append(s)
    new_diseases.append(d)

def best_guess(sym_list, dis_list, user_line):
    words = user_line.split()
    best_score = -1
    best_dis = "Not sure"
    for i in range(len(sym_list)):
        row_words = sym_list[i].split()
        score = 0
        for w in words:
            if w in row_words:
                score += 1
        if score > best_score:
            best_score = score
            best_dis = dis_list[i]
    if best_score <= 0:
        best_dis = "Not sure"
    return best_dis

def round_test(sym_list, dis_list, label):
    print("\n---", label, "Round (3 tests) ---")
    correct = 0
    for t in range(1, 4):
        inp = input(f"Test {t}: Type symptoms: ").strip().lower()
        guess = best_guess(sym_list, dis_list, inp)
        print("Predicted:", guess)
        ok = input("Was this correct? (y/n): ").strip().lower()
        if ok == "y":
            correct += 1
    accuracy = int((correct / 3) * 100)
    print("Accuracy:", accuracy, "%")
    return accuracy

# Round A: only base data
accA = round_test(base_symptoms, base_diseases, "A (Base Only)")

# Round B: base + new data
all_symptoms = base_symptoms + new_symptoms
all_diseases = base_diseases + new_diseases
accB = round_test(all_symptoms, all_diseases, "B (Base + New)")

print("\n=== Summary ===")
print("Round A (Base only) :", accA, "%")
print("Round B (With new)  :", accB, "%")
print("Conclusion: Adding more examples can improve accuracy!")
