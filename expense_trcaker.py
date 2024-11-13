import json
import os

# Define categories for expenses
CATEGORIES = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]

# File path for saving and loading data
FILE_PATH = "expenses.json"


# Function to load expenses from the file
def load_expenses():
    """Loads expenses from a JSON file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return []  # Return an empty list if the file does not exist


# Function to save expenses to the file
def save_expenses(expenses):
    """Saves the list of expenses to a JSON file."""
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)


# Function to add a new expense
def add_expense():
    """Prompts the user to enter an expense and adds it to the expenses list."""
    try:
        # Get expense details from the user
        amount = float(input("Enter the amount spent: "))
        if amount <= 0:
            print("Amount should be greater than zero.")
            return None

        description = input("Enter a brief description of the expense: ")
        print("Available categories:")
        for i, category in enumerate(CATEGORIES, 1):
            print(f"{i}. {category}")

        choice = int(input("Choose a category (1-5): "))
        if choice < 1 or choice > len(CATEGORIES):
            print("Invalid category choice.")
            return None

        category = CATEGORIES[choice - 1]

        # Return a dictionary representing the expense
        return {"amount": amount, "description": description, "category": category}
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")
        return None


# Function to analyze and summarize expenses
def analyze_expenses(expenses):
    """Displays an analysis of the user's expenses."""
    total_expense = sum(exp['amount'] for exp in expenses)
    print(f"Total Expenses: ${total_expense:.2f}")

    categories_expenses = {}
    for expense in expenses:
        category = expense['category']
        categories_expenses[category] = categories_expenses.get(category, 0) + expense['amount']

    print("Expenses by Category:")
    for category, total in categories_expenses.items():
        print(f"{category}: ${total:.2f}")


# Function to display all expenses
def view_expenses(expenses):
    """Displays all the stored expenses."""
    if not expenses:
        print("No expenses to display.")
        return
    print("\nAll Expenses:")
    for expense in expenses:
        print(f"${expense['amount']:.2f} - {expense['description']} (Category: {expense['category']})")


# Function for the main menu interface
def main_menu():
    """Displays the main menu and handles user choices."""
    expenses = load_expenses()  # Load expenses from the file at the start

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))

            if choice == 1:
                expense = add_expense()
                if expense:
                    expenses.append(expense)
                    save_expenses(expenses)  # Save the updated list of expenses
                    print("Expense added successfully.")

            elif choice == 2:
                view_expenses(expenses)

            elif choice == 3:
                analyze_expenses(expenses)

            elif choice == 4:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")


# Main function to start the application
if __name__ == "__main__":
    main_menu()
