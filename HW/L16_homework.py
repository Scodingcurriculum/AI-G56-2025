# -------------------------------------------------------------
# Lesson 16 – Predict with AI Doctor (Rule-of-Thumb Homework)
# Task: Use simple word matching to pick the best disease.
# Level: Grade 5–6  |  Lists, loops, basic scoring.
# -------------------------------------------------------------

print("=== Lesson 16: Simple Prediction by Word Matching ===")
print("Enter 6 lines of 'symptoms -> disease' to learn from.")
print("-" * 60)

symptoms_list = []
disease_list = []

# 1) Collect 6 pairs
for i in range(1, 7):
    print("-" * 20, "Row", i, "-" * 20)
    s = input("Symptoms (e.g., 'fever cough'): ").strip().lower()
    d = input("Disease  (e.g., 'flu'): ").strip().lower()
    symptoms_list.append(s)
    disease_list.append(d)

def best_guess(user_line):
    user_words = user_line.split()
    best_score = -1
    best_disease = "Not sure"
    # Check each row and count overlapping words
    for idx in range(len(symptoms_list)):
        row_words = symptoms_list[idx].split()
        score = 0
        for w in user_words:
            if w in row_words:
                score += 1
        if score > best_score:
            best_score = score
            best_disease = disease_list[idx]
    # If no overlap, say Not sure
    if best_score == 0:
        best_disease = "Not sure"
    return best_disease, best_score

# 2) Run two test predictions
print("\n=== Test 1 ===")
test1 = input("Type symptoms to predict (e.g., 'fever cough'): ").strip().lower()
guess1, score1 = best_guess(test1)
print("Prediction:", guess1, "| Score:", score1)

print("\n=== Test 2 ===")
test2 = input("Type symptoms to predict: ").strip().lower()
guess2, score2 = best_guess(test2)
print("Prediction:", guess2, "| Score:", score2)

print("\nDone! This is a tiny rule-based prediction, not a real doctor.")
