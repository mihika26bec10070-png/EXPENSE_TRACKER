from storage import save_expenses
from validation import valid_amount


def add_expense(expenses):

    print("\n----- ADD EXPENSE -----")

    amount = input("Enter amount: ")

    if not valid_amount(amount):
        print("Invalid amount! Enter a positive number.")
        return

    category = input("Enter category: ")
    date = input("Enter date: ")
    description = input("Enter description: ")

    expense = {
        "amount": float(amount),
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully!")


def update_expense(expenses):

    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n----- UPDATE EXPENSE -----")

    for i in range(len(expenses)):
        print(
            i + 1,
            expenses[i]["category"],
            expenses[i]["amount"],
            expenses[i]["date"]
        )

    try:
        number = int(input("Enter expense number to update: "))
        index = number - 1

        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return

    except:
        print("Please enter a valid number.")
        return

    amount = input("Enter new amount: ")

    if not valid_amount(amount):
        print("Invalid amount!")
        return

    category = input("Enter new category: ")
    date = input("Enter new date: ")
    description = input("Enter new description: ")

    expenses[index]["amount"] = float(amount)
    expenses[index]["category"] = category
    expenses[index]["date"] = date
    expenses[index]["description"] = description

    save_expenses(expenses)

    print("Expense updated successfully!")


def delete_expense(expenses):

    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n----- DELETE EXPENSE -----")

    for i in range(len(expenses)):
        print(
            i + 1,
            expenses[i]["category"],
            expenses[i]["amount"],
            expenses[i]["date"]
        )

    try:
        number = int(input("Enter expense number to delete: "))
        index = number - 1

        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return

    except:
        print("Please enter a valid number.")
        return

    expenses.pop(index)

    save_expenses(expenses)

    print("Expense deleted successfully!")