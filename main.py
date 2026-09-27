from expense import add_expense, update_expense, delete_expense
from storage import load_expenses
from display import show_expenses
from analysis import show_total, category_analysis


def main():

    expenses = load_expenses()

    while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Total Expense")
        print("6. Category Analysis")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            update_expense(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            show_total(expenses)

        elif choice == "6":
            category_analysis(expenses)

        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1 to 7.")


if __name__ == "__main__":
    main()