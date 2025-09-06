# L07_homework.py
# Goal: Ask about favorite weather and respond with different messages.
# Skills: multi-branch conditionals, tidy outputs.

print("=== Weather Chatbot ===\n")
weather = input("What's your favorite weather? ").strip().lower()

print("\n" + "-" * 40)
if weather == "sunny":
    print("Perfect for outdoor games! ☀️")
elif weather == "rainy":
    print("Time for books, music, and cozy vibes! 🌧️")
elif weather in ("winter", "cold"):
    print("Stay warm with cocoa and a blanket! ❄️")
elif weather in ("windy", "breezy"):
    print("Kites and paper planes can be extra fun! 🍃")
else:
    print("That’s interesting weather! Enjoy it your way!")
print("-" * 40)
