import random
import time

# --------------------------------
# DATA
# --------------------------------

predictions = {
    "1": {
        "category": "💼 Career",
        "future": [
            "An unexpected opportunity will appear.",
            "Your next big idea could become something real.",
            "Someone will recognize your potential.",
            "A new project will open an interesting door."
        ]
    },

    "2": {
        "category": "❤️ Relationships",
        "future": [
            "Someone will surprise you.",
            "An unexpected conversation will change your mood.",
            "A relationship will become stronger.",
            "Someone from your past may contact you."
        ]
    },

    "3": {
        "category": "💰 Money",
        "future": [
            "A small opportunity could become something bigger.",
            "You may discover a new way to earn money.",
            "An unexpected reward is coming.",
            "Your next financial decision will be important."
        ]
    },

    "4": {
        "category": "🎓 Studies",
        "future": [
            "A difficult topic will suddenly become easier.",
            "Your hard work will start showing results.",
            "You will discover a better way to learn.",
            "An important opportunity will test your skills."
        ]
    },

    "5": {
        "category": "🌱 Personal Growth",
        "future": [
            "You are about to leave an old habit behind.",
            "A new routine will change your life.",
            "You will become more confident.",
            "Something outside your comfort zone will help you grow."
        ]
    }
}

colors = [
    "Purple",
    "Blue",
    "Red",
    "Green",
    "Orange",
    "Pink",
    "Black"
]

events = [
    "You will start a new project.",
    "Someone will give you an unexpected opportunity.",
    "You will discover a new skill.",
    "You will travel somewhere unexpected.",
    "You will meet someone interesting.",
    "You will finally finish something you started."
]

messages = [
    "The future is uncertain, but your choices shape it.",
    "Trust yourself more than you think you should.",
    "Something interesting is closer than you realize.",
    "Your next chapter is going to be different.",
    "Don't ignore the small opportunities."
]

# --------------------------------
# INTRO
# --------------------------------

print("=" * 45)
print("          🔮 FUTUREVISION AI")
print("=" * 45)

name = input("\nEnter your name: ")

print("""
What are you focusing on right now?

1. 💼 Career
2. ❤️ Relationships
3. 💰 Money
4. 🎓 Studies
5. 🌱 Personal Growth
""")

choice = input("Choose: ")

# --------------------------------
# ANALYSIS
# --------------------------------

if choice in predictions:

    print("\n🔮 SCANNING YOUR FUTURE...\n")

    for i in range(20):
        print("█", end="", flush=True)
        time.sleep(0.1)

    print(" 100%")

    data = predictions[choice]

    future = random.choice(data["future"])

    luck = random.randint(1, 100)

    lucky_number = random.randint(1, 99)

    lucky_color = random.choice(colors)

    next_event = random.choice(events)

    message = random.choice(messages)

    # --------------------------------
    # RESULT
    # --------------------------------

    print("\n" + "=" * 45)
    print("            ✨ FUTURE DETECTED ✨")
    print("=" * 45)

    print(f"\n👤 {name}")

    print(f"\n{data['category']}")

    print(f"\n🔮 Prediction:")
    print(f'"{future}"')

    print(f"\n🍀 Luck:")
    print(f"{luck}%")

    print(f"\n🎯 Next Big Event:")
    print(next_event)

    print(f"\n🔢 Lucky Number:")
    print(lucky_number)

    print(f"\n🎨 Lucky Color:")
    print(lucky_color)

    print(f"\n💬 AI Message:")
    print(f'"{message}"')

    print("\n" + "=" * 45)

else:

    print("\n❌ Invalid choice.")