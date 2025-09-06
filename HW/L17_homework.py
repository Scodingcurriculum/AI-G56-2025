# -----------------------------------------------------------------
# Lesson 17 – Add Confidence to Prediction (Friendly Math Homework)
# Task: Show a simple confidence based on scores.
# Level: Grade 5–6  |  Lists, loops, bars, and tags.
# -----------------------------------------------------------------

print("=== Lesson 17: Prediction with Confidence ===")
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

def predict_with_conf(user_line):
    user_words = user_line.split()
    scores = []
    # Score each row
    for idx in range(len(symptoms_list)):
        row_words = symptoms_list[idx].split()
        score = 0
        for w in user_words:
            if w in row_words:
                score += 1
        scores.append(score)
    # Find best
    best_score = max(scores) if scores else 0
    best_index = scores.index(best_score) if scores else 0
    best_disease = disease_list[best_index] if scores else "Not sure"

    total = sum(scores)
    if total == 0 or best_score == 0:
        conf = 0
        best_disease = "Not sure"
    else:
        conf = int((best_score / total) * 100)

    # Make a simple confidence bar (0–10 #)
    hashes = "#" * max(0, min(10, conf // 10))
    dashes = "-" * (10 - len(hashes))
    bar = "[" + hashes + dashes + "]"

    # Tag
    if conf >= 70:
        tag = "[HIGH]"
    elif conf >= 40:
        tag = "[MEDIUM]"
    else:
        tag = "[LOW]"

    return best_disease, conf, bar, tag, scores

# 2) Two test runs
for run in range(1, 3):
    print("\n=== Test", run, "===")
    line = input("Type symptoms to predict: ").strip().lower()
    disease, conf, bar, tag, scores = predict_with_conf(line)
    print("Scores per row:", scores)
    print("Best disease  :", disease)
    print("Confidence    :", str(conf) + "%", bar, tag)

print("\nRemember: This is a simple classroom demo, not medical advice.")
