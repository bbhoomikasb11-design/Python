import random
import time

# -----------------------------
# DATA
# -----------------------------

locations = [
    "Abandoned Mansion",
    "Luxury Hotel",
    "Old Library",
    "Private Yacht",
    "Remote Cabin"
]

weapons = [
    "Broken glass",
    "Poison",
    "Rope",
    "Heavy statue",
    "Unknown object"
]

suspects = [
    "The Butler",
    "The Brother",
    "The Neighbor",
    "The Business Partner"
]

clues = [
    "A wet footprint was found near the crime scene.",
    "A strange note was found on the table.",
    "The victim's watch stopped at 11:47 PM.",
    "A window was left open.",
    "Someone had recently entered the room.",
    "A photograph was missing.",
    "A glass was found with fingerprints on it.",
    "A suspicious phone call was recorded."
]

# -----------------------------
# INTRO
# -----------------------------

print("=" * 50)
print("          🕵️ MYSTERY DETECTIVE")
print("=" * 50)

input("\nPress ENTER to start the investigation...")

print("\n🔍 Generating your case...")

time.sleep(1)

# Random case

location = random.choice(locations)
weapon = random.choice(weapons)
killer = random.choice(suspects)

# Choose clues
case_clues = random.sample(clues, 4)

# -----------------------------
# CASE
# -----------------------------

print("\n" + "=" * 50)
print("                 CASE")
print("=" * 50)

print(f"\n📍 Location: {location}")
print(f"🔪 Weapon: {weapon}")
print("⏰ Time of crime: 11:47 PM")

print("\n👥 SUSPECTS")

for i, suspect in enumerate(suspects, 1):
    print(f"{i}. {suspect}")

# -----------------------------
# CLUES
# -----------------------------

print("\n🔎 CLUES")

for i, clue in enumerate(case_clues, 1):
    print(f"{i}. {clue}")

# -----------------------------
# ACCUSATION
# -----------------------------

print("\n" + "=" * 50)
print("              MAKE YOUR ACCUSATION")
print("=" * 50)

for i, suspect in enumerate(suspects, 1):
    print(f"{i}. {suspect}")

choice = int(input("\nWho is the killer? Enter number: "))

guess = suspects[choice - 1]

# -----------------------------
# RESULT
# -----------------------------

print("\n🔍 Comparing evidence...")

time.sleep(2)

if guess == killer:

    print("\n" + "=" * 50)
    print("              🎉 CASE SOLVED!")
    print("=" * 50)

    print(f"\nYou correctly identified: {killer}")
    print(f"The murder weapon was: {weapon}")
    print(f"The crime happened at: {location}")

    print("\n🏆 Detective Rating: ⭐⭐⭐⭐⭐")

else:

    print("\n" + "=" * 50)
    print("              ❌ WRONG SUSPECT")
    print("=" * 50)

    print(f"\nYou accused: {guess}")
    print(f"The actual killer was: {killer}")

    print("\n💀 The case remains unsolved.")

print("\nThanks for playing, Detective. 🕵️")