import random
import time

moods = {
    "1": {
        "name": "Happy 😊",
        "music": ["Pop", "Dance", "Party Mix"],
        "activity": ["Go for a walk", "Call a friend", "Try something new"],
        "food": ["Pizza", "Ice cream", "Burger"],
        "message": [
            "Keep that energy going!",
            "Today is your day!",
            "Spread the good vibes!"
        ]
    },

    "2": {
        "name": "Bored 😐",
        "music": ["Lo-fi", "Indie", "Chill beats"],
        "activity": ["Learn something new", "Go outside", "Try a new hobby"],
        "food": ["Fries", "Noodles", "Popcorn"],
        "message": [
            "Your brain needs an adventure.",
            "Do something you've never done.",
            "Boredom is just creativity waiting to happen."
        ]
    },

    "3": {
        "name": "Sad 😔",
        "music": ["Acoustic", "Soft piano", "Chill music"],
        "activity": ["Watch a comfort movie", "Talk to someone", "Take a relaxing walk"],
        "food": ["Hot chocolate", "Ice cream", "Comfort food"],
        "message": [
            "It's okay to have a bad day.",
            "Take things one step at a time.",
            "Tomorrow can be different."
        ]
    },

    "4": {
        "name": "Angry 😡",
        "music": ["Rock", "Workout music", "Heavy beats"],
        "activity": ["Go for a run", "Write down your thoughts", "Take some quiet time"],
        "food": ["Spicy noodles", "Fries", "Tacos"],
        "message": [
            "Take a breath before making decisions.",
            "Use that energy positively.",
            "Give yourself some space."
        ]
    },

    "5": {
        "name": "Tired 😴",
        "music": ["Rain sounds", "Slow piano", "Ambient"],
        "activity": ["Take a nap", "Read a book", "Take a warm shower"],
        "food": ["Soup", "Fruit", "Warm milk"],
        "message": [
            "Rest is productive too.",
            "Your body needs a break.",
            "Slow down today."
        ]
    },

    "6": {
        "name": "Stressed 🤯",
        "music": ["Meditation", "Nature sounds", "Lo-fi"],
        "activity": ["Meditate for 10 minutes", "Take a walk", "Disconnect from your phone"],
        "food": ["Fruit", "Smoothie", "Dark chocolate"],
        "message": [
            "You don't have to solve everything today.",
            "One thing at a time.",
            "Take a deep breath and reset."
        ]
    }
}


print("=" * 40)
print("       🌈 MOOD LIFE GENERATOR")
print("=" * 40)

print("""
1. 😊 Happy
2. 😐 Bored
3. 😔 Sad
4. 😡 Angry
5. 😴 Tired
6. 🤯 Stressed
""")

choice = input("How are you feeling? ")

if choice in moods:

    mood = moods[choice]

    print("\n🔮 Analyzing your mood...")

    for i in range(5):
        print("█", end="", flush=True)
        time.sleep(0.3)

    print(" 100%\n")

    print("=" * 40)
    print("           ✨ YOUR PLAN")
    print("=" * 40)

    print(f"\nMood: {mood['name']}")

    print(f"\n🎵 Music:")
    print(random.choice(mood["music"]))

    print(f"\n🏃 Activity:")
    print(random.choice(mood["activity"]))

    print(f"\n🍕 Food:")
    print(random.choice(mood["food"]))

    print(f"\n💬 Message:")
    print(random.choice(mood["message"]))

else:
    print("\n❌ Invalid choice.")