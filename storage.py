import csv


FILE_NAME = "expenses.csv"


def load_expenses():

    expenses = []

    try:

        file = open(FILE_NAME, "r", newline="")

        reader = csv.DictReader(file)

        for row in reader:

            expense = {
                "amount": float(row["amount"]),
                "category": row["category"],
                "date": row["date"],
                "description": row["description"]
            }

            expenses.append(expense)

        file.close()

    except FileNotFoundError:

        file = open(FILE_NAME, "w", newline="")

        writer = csv.writer(file)

        writer.writerow([
            "amount",
            "category",
            "date",
            "description"
        ])

        file.close()

    return expenses


def save_expenses(expenses):

    file = open(FILE_NAME, "w", newline="")

    fieldnames = [
        "amount",
        "category",
        "date",
        "description"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for expense in expenses:
        writer.writerow(expense)

    file.close()