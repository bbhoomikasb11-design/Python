import random
import time

# -----------------------------
# PERSONALITY DATA
# -----------------------------

personality_types = [
    {
        "name": "🔥 The Creative Chaotic",
        "description": "You have endless ideas and love creating new things.",
        "strength": "Creativity",
        "weakness": "Starting too many things"
    },

    {
        "name": "🧠 The Mastermind",
        "description": "You think deeply before making important decisions.",
        "strength": "Problem solving",
        "weakness": "Overthinking"
    },

    {
        "name": "😎 The Natural Leader",
        "description": "People naturally look to you when something needs to be done.",
        "strength": "Leadership",
        "weakness": "Being too controlling"
    },

    {
        "name": "🌙 The Dreamer",
        "description": "Your imagination is one of your biggest strengths.",
        "strength": "Imagination",
        "weakness": "Getting distracted"
    },

    {
        "name": "⚡ The Adventurer",
        "description": "You love trying new things and hate boring routines.",
        "strength": "Bravery",
        "weakness": "Impulsiveness"
    }
]

colors = [
    "Purple",
    "Blue",
    "Red",
    "Black",
    "Green",
    "Orange",
    "Pink"
]

missions = [
    "Build something nobody has seen before.",
    "Turn your biggest idea into reality.",
    "Learn something completely new.",
    "Take a risk you've been avoiding.",
    "Create something that helps other people."
]

# -----------------------------
# START
# -----------------------------

print("=" * 40)
print("       🧠 PERSONALITY GENERATOR")
print("=" * 40)

name = input("\nEnter your name: ")

print("\n🔮 Analyzing your personality...")

for i in range(10):
    print("█", end="", flush=True)
    time.sleep(0.2)

print(" 100%")

# -----------------------------
# RANDOM STATS
# -----------------------------

energy = random.randint(50, 100)
creativity = random.randint(50, 100)
intelligence = random.randint(50, 100)
confidence = random.randint(50, 100)
luck = random.randint(1, 100)
chaos = random.randint(1, 100)

personality = random.choice(personality_types)
color = random.choice(colors)
number = random.randint(1, 99)
mission = random.choice(missions)

# -----------------------------
# DISPLAY
# -----------------------------

print("\n" + "=" * 40)
print("          ✨ YOUR PROFILE")
print("=" * 40)

print(f"\n👤 Name: {name}")

print(f"\n⚡ Energy       : {energy}/100")
print(f"🎨 Creativity   : {creativity}/100")
print(f"🧠 Intelligence : {intelligence}/100")
print(f"😎 Confidence   : {confidence}/100")
print(f"🍀 Luck         : {luck}/100")
print(f"🌪️ Chaos        : {chaos}/100")

print("\n" + "=" * 40)
print("        🎭 PERSONALITY TYPE")
print("=" * 40)

print(f"\n{personality['name']}")

print(f'\n"{personality["description"]}"')

print(f"\n💪 Strength:")
print(personality["strength"])

print(f"\n⚠️ Weakness:")
print(personality["weakness"])

print(f"\n🎨 Lucky Color:")
print(color)

print(f"\n🔢 Lucky Number:")
print(number)

print(f"\n🎯 Life Mission:")
print(mission)

print("\n" + "=" * 40)