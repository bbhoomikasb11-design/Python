import random
import time

reasons = [
    "Your gut already knew the answer.",
    "This feels like the right choice.",
    "The universe has spoken.",
    "You probably wanted this anyway.",
    "Don't overthink it. Just do it.",
    "Future you will thank you.",
    "This option has main-character energy."
]

print("=" * 40)
print("       🎯 RANDOM DECISION ENGINE")
print("=" * 40)

while True:

    decision = input("\nWhat are you deciding?\n> ")

    number = int(input("\nHow many options? "))

    options = []

    for i in range(number):
        option = input(f"Enter option {i + 1}: ")
        options.append(option)

    print("\n🤖 ANALYZING YOUR OPTIONS...")

    for i in range(5):
        print("█", end="", flush=True)
        time.sleep(0.3)

    print(" 100%")

    winner = random.choice(options)
    confidence = random.randint(60, 99)
    reason = random.choice(reasons)

    print("\n" + "=" * 40)
    print("           🎯 DECISION")
    print("=" * 40)

    print(f"\n👉 {winner}")
    print(f"\nConfidence: {confidence}%")
    print(f"\n💡 Reason:")
    print(f'"{reason}"')

    again = input("\n\nMake another decision? (yes/no): ")

    if again.lower() != "yes":
        print("\n👋 Decision Engine shutting down...")
        break