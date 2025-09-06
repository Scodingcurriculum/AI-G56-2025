# L04_homework.py
# Goal: Use a dictionary of animal -> sound. Ask for an animal and print its sound.
# Skills: dict, membership check, safe fallback for unknown animals, formatting.

print("=== Animal Sounds ===\n")
sounds = {
    "dog": "Woof",
    "cat": "Meow",
    "cow": "Moo"
}

print("We know these animals:", ", ".join(sounds.keys()))
animal = input("Type an animal name: ").strip().lower()

print("\n" + "-" * 40)
if animal in sounds:
    print(f"{animal.capitalize()} says: {sounds[animal]}!")
else:
    print("I don’t know that sound yet.")
    print("Tip: Try dog, cat, or cow.")
print("-" * 40)

# Extension idea (teacher demo during class):
# sounds[\"duck\"] = \"Quack\"
# print(\"Added duck to the dictionary! Now try typing 'duck'.\")
