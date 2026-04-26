import csv
import os

FILE = 'data/expenses.csv'

# créer fichier si inexistant
if not os.path.exists(FILE):
    with open(FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'category', 'amount', 'description'])

def add_expense(date, category, amount, description):
    with open(FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

def show_total():
    total = 0
    with open(FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[2])
    print(f"Total expenses: {total}")

def show_by_category():
    categories = {}
    with open(FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cat = row[1]
            amount = float(row[2])
            categories[cat] = categories.get(cat, 0) + amount

    print("Expenses by category:")
    for k, v in categories.items():
        print(k, ":", v)

# TEST SIMPLE
add_expense("2026-04-26", "Food", 2500, "Lunch")
add_expense("2026-04-26", "Transport", 1000, "Bus")

show_total()
show_by_category()
