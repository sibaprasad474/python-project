import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=2)

    def display_summary(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total_expenses:.2f}")

    def add_expense(self, amount, category, description):
        new_expense = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'category': category,
            'description': description
        }

        self.expenses.append(new_expense)
        self.save_expenses()
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return

        print("\nExpense Details:")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. Date: {expense['date']} | Amount: ${expense['amount']:.2f} | Category: {expense['category']} | Description: {expense['description']}")

    def delete_selected_expenses(self):
        if not self.expenses:
            print("No expenses to delete.")
            return

        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. Date: {expense['date']} | Amount: ${expense['amount']:.2f} | Category: {expense['category']} | Description: {expense['description']}")

        try:
            index_to_delete = int(input("Enter the number of the expense to delete: ")) - 1
            del self.expenses[index_to_delete]
            self.save_expenses()
            print("Expense deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")

    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Delete Expense")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                amount = float(input("Enter the expense amount: "))
                category = input("Enter the expense category: ")
                description = input("Enter the expense description: ")
                self.add_expense(amount, category, description)
            elif choice == '2':
                self.view_expenses()
                self.display_summary()
            elif choice == '3':
                self.delete_selected_expenses()
            elif choice == '4':
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.run()
