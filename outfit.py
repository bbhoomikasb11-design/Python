import random
import time

outfits = {

    "1": {
        "name": "🎓 College",
        "tops": [
            "Oversized white T-shirt",
            "Black graphic T-shirt",
            "Pastel shirt",
            "Crop top",
            "Denim jacket"
        ],
        "bottoms": [
            "Blue straight-fit jeans",
            "Black cargo pants",
            "Wide-leg jeans",
            "Beige trousers"
        ],
        "shoes": [
            "White sneakers",
            "Black sneakers",
            "Canvas shoes"
        ]
    },

    "2": {
        "name": "💼 Interview",
        "tops": [
            "White formal shirt",
            "Light blue formal shirt",
            "Black formal blouse"
        ],
        "bottoms": [
            "Black trousers",
            "Navy trousers",
            "Beige formal pants"
        ],
        "shoes": [
            "Black formal shoes",
            "Brown loafers"
        ]
    },

    "3": {
        "name": "🎉 Party",
        "tops": [
            "Black stylish top",
            "Satin blouse",
            "Sequined top",
            "Statement shirt"
        ],
        "bottoms": [
            "Black jeans",
            "Leather pants",
            "Wide-leg trousers",
            "Mini skirt"
        ],
        "shoes": [
            "Heels",
            "Platform shoes",
            "Ankle boots"
        ]
    },

    "4": {
        "name": "☕ Casual",
        "tops": [
            "Oversized hoodie",
            "Basic T-shirt",
            "Striped shirt",
            "Casual crop top"
        ],
        "bottoms": [
            "Mom jeans",
            "Cargo pants",
            "Joggers",
            "Shorts"
        ],
        "shoes": [
            "Sneakers",
            "Canvas shoes",
            "Slides"
        ]
    },

    "5": {
        "name": "❤️ Date",
        "tops": [
            "Elegant black top",
            "Satin blouse",
            "Floral top",
            "Off-shoulder top"
        ],
        "bottoms": [
            "Black trousers",
            "Blue jeans",
            "Long skirt"
        ],
        "shoes": [
            "Heels",
            "Flats",
            "Ankle boots"
        ]
    },

    "6": {
        "name": "✈️ Travel",
        "tops": [
            "Oversized T-shirt",
            "Comfortable sweatshirt",
            "Loose shirt",
            "Basic tank top"
        ],
        "bottoms": [
            "Cargo pants",
            "Joggers",
            "Wide-leg jeans",
            "Comfortable shorts"
        ],
        "shoes": [
            "Running shoes",
            "Sneakers",
            "Comfortable sandals"
        ]
    }
}


accessories = [
    "Minimal silver jewellery",
    "Black shoulder bag",
    "Sunglasses",
    "Watch",
    "Crossbody bag",
    "Baseball cap"
]

colors = [
    "Black + White",
    "Blue + White",
    "Beige + Brown",
    "Black + Grey",
    "Pastel",
    "Monochrome"
]

comments = [
    "Simple but effortlessly stylish.",
    "This look has main-character energy.",
    "Clean, comfortable and confident.",
    "You are definitely going to stand out.",
    "The outfit speaks for itself.",
    "Minimal effort, maximum style."
]


print("=" * 45)
print("          👗 AI OUTFIT STYLIST")
print("=" * 45)

print("""
Choose your occasion:

1. 🎓 College
2. 💼 Interview
3. 🎉 Party
4. ☕ Casual
5. ❤️ Date
6. ✈️ Travel
""")

choice = input("Choose: ")

if choice in outfits:

    outfit = outfits[choice]

    print("\n✨ Creating your look...\n")

    for i in range(20):
        print("█", end="", flush=True)
        time.sleep(0.08)

    print(" 100%")

    top = random.choice(outfit["tops"])
    bottom = random.choice(outfit["bottoms"])
    shoes = random.choice(outfit["shoes"])
    accessory = random.choice(accessories)
    color = random.choice(colors)
    score = random.randint(70, 99)
    comment = random.choice(comments)

    print("\n" + "=" * 45)
    print("          💫 TODAY'S OUTFIT")
    print("=" * 45)

    print(f"\n📍 Occasion: {outfit['name']}")

    print(f"\n👕 Top:")
    print(top)

    print(f"\n👖 Bottom:")
    print(bottom)

    print(f"\n👟 Shoes:")
    print(shoes)

    print(f"\n👜 Accessory:")
    print(accessory)

    print(f"\n🎨 Color Theme:")
    print(color)

    print(f"\n🔥 Style Score:")
    print(f"{score}/100")

    print(f"\n💬 Stylist:")
    print(f'"{comment}"')

    print("\n" + "=" * 45)

else:
    print("\n❌ Invalid choice.")