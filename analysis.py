def show_total(expenses):

    total = 0

    for expense in expenses:

        total = total + expense["amount"]

    print("\n========== TOTAL EXPENSE ==========")

    print("Total Expense =", total)


def category_analysis(expenses):

    if len(expenses) == 0:

        print("\nNo expenses available for analysis.")

        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:

            categories[category] = categories[category] + amount

        else:

            categories[category] = amount

    print("\n======= CATEGORY ANALYSIS =======")

    for category in categories:

        print(
            category,
            "=",
            categories[category]
        )