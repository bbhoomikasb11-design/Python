import random
import time

# --------------------------------
# DESTINATIONS
# --------------------------------

destinations = [
    {
        "place": "Coorg, Karnataka",
        "food": "Pandi Curry + Kadambuttu",
        "activity": "Sunrise Trek",
        "experience": "Visit a coffee plantation"
    },

    {
        "place": "Munnar, Kerala",
        "food": "Kerala Parotta + Curry",
        "activity": "Tea Garden Walk",
        "experience": "Watch the sunrise over the hills"
    },

    {
        "place": "Gokarna, Karnataka",
        "food": "Seafood Thali",
        "activity": "Beach Trek",
        "experience": "Watch the sunset at the beach"
    },

    {
        "place": "Hampi, Karnataka",
        "food": "South Indian Thali",
        "activity": "Explore Ancient Ruins",
        "experience": "Watch sunset from Matanga Hill"
    },

    {
        "place": "Pondicherry, Tamil Nadu",
        "food": "French Bakery Food",
        "activity": "Cycling Tour",
        "experience": "Explore White Town"
    },

    {
        "place": "Manali, Himachal Pradesh",
        "food": "Momos + Thukpa",
        "activity": "Mountain Trek",
        "experience": "Explore a hidden waterfall"
    }
]

# --------------------------------
# OTHER DATA
# --------------------------------

stays = [
    "🏡 Cozy Homestay",
    "🏨 Boutique Hotel",
    "🏕️ Campsite",
    "🌲 Forest Cottage",
    "🏔️ Mountain View Resort"
]

transport = [
    "🚗 Road Trip",
    "🚌 Bus",
    "🚆 Train",
    "✈️ Flight",
    "🏍️ Bike Trip"
]

travel_styles = [
    "🔥 Adventure",
    "😌 Relaxation",
    "📸 Photography",
    "🍴 Food Exploration",
    "🏛️ Culture & History"
]

challenges = [
    "Wake up before sunrise.",
    "Try a food you've never eaten.",
    "Talk to a local and learn their story.",
    "Take 10 photos without using a filter.",
    "Spend one hour without your phone.",
    "Find a place that isn't on Google Maps."
]

# --------------------------------
# INTRO
# --------------------------------

print("=" * 45)
print("         ✈️ RANDOM TRAVEL AI")
print("=" * 45)

input("\nPress ENTER to generate your adventure...")

print("\n🌍 Planning your trip...\n")

for i in range(20):
    print("█", end="", flush=True)
    time.sleep(0.08)

print(" 100%")

# --------------------------------
# GENERATE TRIP
# --------------------------------

destination = random.choice(destinations)

days = random.randint(2, 7)

budget = random.randint(5000, 30000)

stay = random.choice(stays)

transport_choice = random.choice(transport)

style = random.choice(travel_styles)

challenge = random.choice(challenges)

score = random.randint(70, 99)

# --------------------------------
# DISPLAY
# --------------------------------

print("\n" + "=" * 45)
print("         🌍 YOUR ADVENTURE")
print("=" * 45)

print(f"\n📍 Destination:")
print(destination["place"])

print(f"\n📅 Trip Duration:")
print(f"{days} Days")

print(f"\n💰 Estimated Budget:")
print(f"₹{budget}")

print(f"\n🏨 Stay:")
print(stay)

print(f"\n🚗 Transport:")
print(transport_choice)

print(f"\n🎒 Travel Style:")
print(style)

print(f"\n🍴 Must Try:")
print(destination["food"])

print(f"\n🌄 Main Activity:")
print(destination["activity"])

print(f"\n☕ Experience:")
print(destination["experience"])

print(f"\n🎯 Secret Challenge:")
print(challenge)

print(f"\n🔥 Adventure Score:")
print(f"{score}/100")

print("\n" + "=" * 45)
print("        HAVE AN AMAZING TRIP! 🌎")
print("=" * 45)