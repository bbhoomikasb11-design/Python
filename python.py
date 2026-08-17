expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: ₹"))
        expenses.append([name, amount])
        print("Expense added!")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            for name, amount in expenses:
                print(f"{name}: ₹{amount}")

    elif choice == "3":
        total = sum(amount for name, amount in expenses)
        print(f"Total expense: ₹{total}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")