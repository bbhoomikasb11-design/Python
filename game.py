import random
import time

# -----------------------------
# GAME DATA
# -----------------------------

locations = [
    "🏚️ Abandoned Mansion",
    "🏝️ Lost Island",
    "🏰 Haunted Castle",
    "🚀 Abandoned Space Station",
    "🌲 Dark Forest"
]

enemies = [
    "👻 Shadow Ghost",
    "🐉 Fire Dragon",
    "🤖 Rogue Robot",
    "🧟 Zombie King",
    "🧙 Dark Wizard"
]

weapons = [
    "🪄 Magic Pencil",
    "⚔️ Crystal Sword",
    "🏹 Golden Bow",
    "🔫 Plasma Blaster",
    "🛡️ Ancient Shield"
]

missions = [
    "🔑 Find the Golden Key",
    "💎 Steal the Ancient Diamond",
    "👑 Rescue the Lost Prince",
    "📜 Find the Secret Map",
    "🧪 Recover the Magic Potion"
]

# -----------------------------
# GENERATE GAME
# -----------------------------

location = random.choice(locations)
enemy = random.choice(enemies)
weapon = random.choice(weapons)
mission = random.choice(missions)

gold = random.randint(100, 1000)

difficulty = random.choice([
    "EASY 🟢",
    "MEDIUM 🟡",
    "HARD 🔴"
])

# -----------------------------
# INTRO
# -----------------------------

print("=" * 50)
print("          🎮 RANDOM ADVENTURE")
print("=" * 50)

print("\nGenerating your world...")

for i in range(10):
    print("█", end="", flush=True)
    time.sleep(0.15)

print(" 100%")

# -----------------------------
# SHOW WORLD
# -----------------------------

print("\n" + "=" * 50)

print(f"\n📍 Location: {location}")
print(f"👹 Enemy: {enemy}")
print(f"⚔️ Weapon: {weapon}")
print(f"🎯 Mission: {mission}")
print(f"💰 Reward: {gold} Gold")
print(f"🔥 Difficulty: {difficulty}")

print("\n" + "=" * 50)

input("\nPress ENTER to begin your adventure...")

# -----------------------------
# STORY
# -----------------------------

print("\nYou enter the location...")

time.sleep(1)

print("\nYou hear a strange sound behind you.")

print("""
1. 🏃 Run
2. 🔎 Investigate
3. 🫣 Hide
""")

choice = input("Choose: ")

if choice == "1":

    print("\n🏃 You run deeper into the area!")

elif choice == "2":

    print("\n🔎 You investigate the sound...")

    time.sleep(1)

    print(f"\n{enemy} appears!")

elif choice == "3":

    print("\n🫣 You hide behind a wall.")

    time.sleep(1)

    print(f"\n{enemy} walks past you...")

else:

    print("\n❌ You froze and did nothing!")

# -----------------------------
# ENEMY ENCOUNTER
# -----------------------------

print("\n" + "=" * 50)

print(f"{enemy} is blocking your path!")

print("""
1. ⚔️ Fight
2. 🏃 Run
3. 🗣️ Talk
""")

choice = input("Choose: ")

if choice == "1":

    print(f"\n⚔️ You use your {weapon}!")

    success = random.randint(1, 100)

    if success >= 50:

        print("\n🎉 YOU WON!")

        print(f"💰 You received {gold} gold!")

    else:

        print("\n💀 You lost the battle.")

elif choice == "2":

    print("\n🏃 You escaped!")

    print("\nBut the mission remains incomplete.")

elif choice == "3":

    print("\n🗣️ You try talking to the enemy...")

    chance = random.randint(1, 2)

    if chance == 1:

        print("\n🤝 Surprisingly, the enemy helps you!")

        print(f"\n🎯 You discover the location of the {mission}.")

    else:

        print("\n😡 The enemy attacks you!")

else:

    print("\n❌ Invalid choice.")

# -----------------------------
# END
# -----------------------------

print("\n" + "=" * 50)
print("           🏁 ADVENTURE COMPLETE")
print("=" * 50)

print("\nThanks for playing! 🎮")