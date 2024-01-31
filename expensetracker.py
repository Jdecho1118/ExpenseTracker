import json
import getpass
import bcrypt  #Install in terminal ( "pip install bcrypt " ) 
import logging

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.income = 0
        self.username = None
        self._password_hash = None  # Encapsulate password hash

        # Logging configuration
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger("ExpenseTracker")
        self.logger.info("ExpenseTracker instance created.")

    def _hash_password(self, password):
        try:
            salt = bcrypt.gensalt()
            return bcrypt.hashpw(password.encode('utf-8'), salt)
        except Exception as e:
            self.logger.exception("Error during password hashing: %s", e)
            raise

    def set_credentials(self, username, password):
        self.username = username
        self._password_hash = self._hash_password(password)
        self.logger.info("Credentials set for user: %s", username)

    def check_credentials(self, username, password):
        return self.username == username and bcrypt.checkpw(password.encode('utf-8'), self._password_hash)

    def insert_income(self, income):
        try:
            income = float(income)
            if income >= 0:
                self.income = income
                self.logger.info("Income of ₹%s recorded successfully.", income)
            else:
                self.logger.warning("Attempted to set negative income.")
                print("Income must be a non-negative number.")
        except ValueError:
            self.logger.error("Invalid input for income.")
            print("Invalid input. Please enter a valid income.")

    def add_expense(self, category, amount):
        try:
            amount = float(amount)
            if not isinstance(category, str) or not category.strip():
                raise ValueError("Invalid category name.")

            if amount <= 0:
                print("Amount must be a positive number.")
                return

            if category in self.expenses:
                self.expenses[category] += amount
            else:
                self.expenses[category] = amount
            print("Expense added successfully!")
            self.logger.info("Expense added - Category: %s, Amount: ₹%s", category, amount)
        except ValueError:
            self.logger.error("Invalid input for expense.")
            print("Invalid input. Please enter a valid amount.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("\nExpense Tracker:")
            for category, amount in self.expenses.items():
                print(f"{category}: ₹{amount}")

            total_expenses = sum(self.expenses.values())
            remaining_income = self.income - total_expenses

            print(f"Total Expenses: ₹{total_expenses}")
            print(f"Remaining Income: ₹{remaining_income}")

            if total_expenses > self.income:
                print("Warning: You have exceeded your monthly income!")

    def save_data(self, filename="expense_tracker_data.json"):
        data = {
            "expenses": self.expenses,
            "income": self.income,
            "username": self.username,
            "_password_hash": self._password_hash,  # Save hashed password
        }

        with open(filename, 'w') as file:
            json.dump(data, file)
        print("Data saved successfully!")
        self.logger.info("Data saved successfully.")

    def load_data(self, filename="expense_tracker_data.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.expenses = data.get("expenses", {})
                self.income = data.get("income", 0)
                self.username = data.get("username", None)
                self._password_hash = data.get("_password_hash", None)
            print("Data loaded successfully!")
            self.logger.info("Data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found. Starting with a fresh Expense Tracker.")
            self.logger.warning("No previous data found.")

def main():
    tracker = ExpenseTracker()
    credentials_set = False

    # Load existing data if available
    tracker.load_data()

    while True:
        print("\n1. Set Username and Password")
        print("2. Login")
        print("3. Insert Income")
        print("4. Add Expense")
        print("5. View Expenses")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice ( 1, 2, 3, 4, 5, 6, 7 ): ")

        if choice == '1':
            if not credentials_set:
                username = input("Enter username: ")
                password = getpass.getpass("Enter password: ")
                tracker.set_credentials(username, password)
                credentials_set = True
            else:
                print("Credentials already set. Cannot set again.")
        elif choice == '2':
            if credentials_set:
                username_input = input("Enter username: ")
                password_input = getpass.getpass("Enter password: ")
                if tracker.check_credentials(username_input, password_input):
                    print("Login successful!")
                else:
                    print("Invalid credentials. Please try again.")
            else:
                print("Please set username and password first (Option 1).")
        elif credentials_set:
            try:
                if choice == '3':
                    income = input("Enter your monthly income: ")
                    tracker.insert_income(income)
                elif choice == '4':
                    category = input("Enter the expense category: ")
                    amount = input("Enter the expense amount: ")
                    tracker.add_expense(category, amount)
                elif choice == '5':
                    tracker.view_expenses()
                elif choice == '6':
                    tracker.save_data()
                elif choice == '7':
                    print("Exiting the Expense Tracker. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter 3, 4, 5, 6, or 7.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Please set username and password first (Option 1).")

if __name__ == "__main__":
    main()
