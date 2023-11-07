import calendar
import datetime

class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"Expense: {self.name}, Category: {self.category}, Amount: ${self.amount:.2f}"

class ExpenseList:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

class ExpenseTracker:
    def __init__(self, budget, expense_list):
        self.budget = budget
        self.expense_list = expense_list

    def get_user_expense(self):
        print("🎯 Getting User Expense")
        expense_name = input("Enter item to purchase: ")
        expense_amount = float(input("Enter expense amount:  "))
        expense_categories = [
            "Food",
            "Home",
            "Work",
            "Fun",
            "Misc",
        ]

        while True:
            print("Select a category: ")
            for i, category_name in enumerate(expense_categories):
                print(f"  {i + 1}. {category_name}")

            value_range = f"[1 - {len(expense_categories)}]"
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
                self.expense_list.add_expense(new_expense)
                return

            else:
                print("Invalid category. Please try again!")

    def save_expenses_to_file(self, expense_file_path):
        print(f"🎯 Saving User Expenses to {expense_file_path}")
        with open(expense_file_path, "a") as f:
            for expense in self.expense_list.expenses:
                f.write(f"{expense.name},{expense.amount},{expense.category}\n")

    def summarize_expenses(self):
        print(f"🎯 Summarizing User Expenses")
        amount_by_category = {}
        total_spent = 0

        for expense in self.expense_list.expenses:
            key = expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key] = expense.amount
            total_spent += expense.amount

        print("Expenses By Category 📈:")
        for key, amount in amount_by_category.items():
            print(f"  {key}: ${amount:.2f}")

        print(f"💵 Total Spent: ${total_spent:.2f}")

        remaining_budget = self.budget - total_spent
        print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

        now = datetime.datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        remaining_days = days_in_month - now.day

        if remaining_days > 0:
            daily_budget = remaining_budget / remaining_days
            print(f"👉 Budget Per Day: ${daily_budget:.2f}")
        else:
            print("Cannot calculate daily budget as the month is almost over.")

if __name__ == "__main__":
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = float(input("Enter your budget: "))

    expense_list = ExpenseList()
    tracker = ExpenseTracker(budget, expense_list)

    while True:
        tracker.get_user_expense()
        more_expenses = input("Do you want to add more expenses (Y/N)? ").strip().lower()
        if more_expenses != 'y':
            break

    tracker.save_expenses_to_file(expense_file_path)
    tracker.summarize_expenses()

