# ----------------------------------------------------------------
# Lesson 15 – Train Your AI Doctor (Very Simple Counting Homework)
# Task: Count how many times common words appear in symptoms.
# Level: Grade 5–6  |  Use lists, loops, counters, and prints.
# ----------------------------------------------------------------

print("=== Lesson 15: Simple 'Training' by Counting Words ===")
print("Enter 6-8 symptom lines and their diseases. We count common words.")
print("-" * 60)

symptoms_list = []
disease_list = []

# 1) Collect 6 symptom->disease pairs
for i in range(1, 7):
    print("-" * 20, "Row", i, "-" * 20)
    s = input("Symptoms (e.g., 'fever cough'): ").strip().lower()
    d = input("Disease  (e.g., 'flu'): ").strip().lower()
    symptoms_list.append(s)
    disease_list.append(d)

# 2) Build a flat list of words
all_words = []
for line in symptoms_list:
    words = line.split()
    for w in words:
        all_words.append(w)

# 3) Count some common words using simple counters
fever_count = 0
cough_count = 0
headache_count = 0
rash_count = 0

for w in all_words:
    if w == "fever":
        fever_count += 1
    if w == "cough":
        cough_count += 1
    if w == "headache":
        headache_count += 1
    if w == "rash":
        rash_count += 1

# 4) Print "training report"
print("\n=== Training Report (Word Counts) ===")
print("fever    :", fever_count)
print("cough    :", cough_count)
print("headache :", headache_count)
print("rash     :", rash_count)

# 5) Small explanation
print("\n=== What is 'Training'? ===")
print("1) Training means learning from examples we typed.")
print("2) We counted words to spot simple patterns in symptoms.")
print("3) Later, we will use these patterns to make a guess!")
