# ------------------------------------------------------------------
# Lesson 18 – Explain AI Doctor Predictions (Homework)
# Task: Show WHY a guess was made by listing which words matched.
# Level: Grade 5–6 | Uses simple word matching (no real AI).
# ------------------------------------------------------------------

print("=== Lesson 18: Explain Why the AI Guessed ===")
print("We will store a few 'symptoms -> disease' lines and then explain matches.")
print("-" * 65)

# Example knowledge (students can add more if they want)
symptoms_list = [
    "fever cough",        # row 1
    "runny nose sneezing",# row 2
    "headache stress",    # row 3
    "rash fever"          # row 4
]
disease_list = [
    "flu",
    "cold",
    "stress",
    "chickenpox"
]

# Emoji legend (just for fun)
print("Legend: flu=😷  cold=🤧  stress=🤕  chickenpox=🌟")
print("-" * 65)

def best_row(user_line):
    """Return (index, score) of row with most word overlaps."""
    words = user_line.split()
    best_i = -1
    best_score = -1
    for i in range(len(symptoms_list)):
        row_words = symptoms_list[i].split()
        score = 0
        for w in words:
            if w in row_words:
                score += 1
        if score > best_score:
            best_score = score
            best_i = i
    return best_i, best_score

def emoji_for(disease):
    if disease == "flu":
        return "😷"
    if disease == "cold":
        return "🤧"
    if disease == "stress":
        return "🤕"
    if disease == "chickenpox":
        return "🌟"
    return ""

# Do two tests so we can see multiple explanations
for test in range(1, 3):
    print("\n--- Test", test, "---")
    text = input("Type symptoms (e.g., 'fever cough'): ").strip().lower()
    i, score = best_row(text)
    if i == -1 or score == 0:
        print("I could not match any words. Guess: Not sure.")
    else:
        top_disease = disease_list[i]
        row_words = symptoms_list[i].split()
        user_words = text.split()

        # Find matched and unmatched words
        matched = []
        missing = []
        for w in user_words:
            if w in row_words:
                matched.append(w)
            else:
                missing.append(w)

        print("Top disease :", top_disease, emoji_for(top_disease))
        print("Matched     :", ", ".join(matched) if matched else "(none)")
        print("Not found   :", ", ".join(missing) if missing else "(none)")
        print("Why guess?  : I saw", len(matched), "word(s) from your input in a known example.")

print("\nNote: This is a classroom demo, not medical advice.")
