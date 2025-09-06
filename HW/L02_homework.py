# L02_homework.py
# Goal: Ask the user to choose a favorite AI app from a predefined list,
# then print how that app helps. Use f-strings for clean output.
# Skills: lists, dicts, input(), .strip(), .lower(), f-strings, neat menu.

print("=== Choose Your Favorite AI App ===\n")
apps = ["Alexa", "Siri", "Google Maps", "Netflix", "YouTube", "Spotify"]

features = {
    "alexa": "answers questions and controls smart home devices",
    "siri": "helps send messages and set reminders using voice",
    "google maps": "finds fast routes using live traffic data",
    "netflix": "recommends shows and movies",
    "youtube": "suggests videos based on your interests",
    "spotify": "creates playlists by learning your music taste",
}

# Show menu
print("Available apps:")
for a in apps:
    print(f" - {a}")

choice_raw = input("\nType your favorite app exactly as shown: ")
choice = choice_raw.strip()
key = choice.lower()

print("\n" + "-" * 40)
if key in features:
    print(f"You chose {choice}.")
    print(f"{choice} helps in this way: {features[key]}.")
else:
    print("That app is not in our list yet.")
    print("Tip: Pick one from the menu next time so I can tell you more about it!")
print("-" * 40)

# Extra: friendly outro
print("\nThanks for trying the AI apps menu!\n"
      "Notice how the program matched your text by converting it to lowercase.")
