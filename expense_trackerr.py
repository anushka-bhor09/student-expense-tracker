expenses = []

def add_expense():
    print("\n--- Add Expense ---")

    name = input("Enter expense name: ")
    category = input("Enter category (Food/Travel/College/Other): ")

    try:
        amount = float(input("Enter amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number for the amount.")


def view_expenses():
    print("\n--- Your Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: ₹{total:.2f}")


def main():
    while True:
        print("\n==============================")
        print("   STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("Thank you for using Student Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()