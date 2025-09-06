# -------------------------------------------------------------
# Lesson 14 – Create AI Doctor Dataset (Homework, simple lists)
# Task: Collect 10 'symptoms -> disease' pairs and preview them.
# Level: Grade 5–6  |  No CSV module here; just lists and prints.
# -------------------------------------------------------------

print("=== Lesson 14: Build a Small Symptoms->Disease List ===")
print("Please enter 10 lines like: 'fever cough' -> 'flu'")
print("-" * 60)

symptoms_list = []
disease_list = []

# 1) Collect 10 pairs
for i in range(1, 11):
    print("-" * 20, "Row", i, "-" * 20)
    symptoms = input("Enter symptoms (1-5 words): ").strip().lower()
    disease = input("Enter disease (one word): ").strip().lower()
    symptoms_list.append(symptoms)
    disease_list.append(disease)

# 2) Preview table
print("\n=== Preview Table ===")
print("No. | Symptoms                | Disease")
print("-" * 45)
for i in range(len(symptoms_list)):
    s = symptoms_list[i]
    d = disease_list[i]
    print(f"{i+1:>2}. | {s:<22} | {d}")

# 3) Count totals and unique diseases (simple list check)
print("-" * 45)
total_rows = len(symptoms_list)
seen = []
for d in disease_list:
    if d not in seen:
        seen.append(d)
unique_count = len(seen)

print("Total rows:", total_rows)
print("Unique diseases:", unique_count)
print("Unique list:", ", ".join(seen))

# 4) Friendly summary
print("\nSummary: You created a small labeled dataset in memory.")
print("We will use it later to make simple predictions!")
