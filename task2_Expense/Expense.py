import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "expenses.csv")


# -------------------------------------------------
# 1. Add Expense
# -------------------------------------------------

def add_expense():
    expense = input("Expense Name: ").strip()

    if not expense:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Amount in PKR: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense, amount])

    print("Expense added successfully!")


# -------------------------------------------------
# 2. View Expenses
# -------------------------------------------------

def view_expenses():
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if not rows:
                print("\nNo expenses found.")
                return

            print("\n====== All Expenses ======\n")

            for row in rows:
                if len(row) >= 2:
                    print(f"Expense: {row[0]}")
                    print(f"Amount: PKR {float(row[1]):.2f}")
                    print("-" * 30)

    except FileNotFoundError:
        print("\nNo expenses found.")

    except ValueError:
        print("\nInvalid data found in expenses.csv.")


# -------------------------------------------------
# 3. Delete Expense
# -------------------------------------------------

def delete_expense():
    search = input("Enter expense name to delete: ").strip()

    if not search:
        print("Expense name cannot be empty.")
        return

    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

    except FileNotFoundError:
        print("No expenses found.")
        return

    new_rows = []
    found = False

    for row in rows:

        if len(row) >= 2 and row[0].lower() == search.lower():
            found = True

        else:
            new_rows.append(row)

    if found:

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

        print("Expense deleted successfully!")

    else:
        print("Expense not found.")


# -------------------------------------------------
# 4. Show Total Expense
# -------------------------------------------------

def show_total_expense():
    total = 0

    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) >= 2:
                    total += float(row[1])

        print(f"\nTotal Expense: PKR {total:.2f}")

    except FileNotFoundError:
        print("\nNo expenses found.")

    except ValueError:
        print("\nInvalid data found in expenses.csv.")


# -------------------------------------------------
# Main Menu
# -------------------------------------------------

while True:

    print("\n========== Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total Expense")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        show_total_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice. Please select 1-5.")