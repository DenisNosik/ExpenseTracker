import argparse
import json
from datetime import datetime
from pathlib import Path


filename = Path("expenses_data.json")

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add a New Expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="expense description")
    add_parser.add_argument("--amount", type=float, required=True, help="expense amount")
    add_parser.set_defaults(func=add_expense)

    # Delete an existing expense
    delete_parser = subparsers.add_parser("delete", help="Remove an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="expense id")
    delete_parser.set_defaults(func=delete_expense)

    # List of expenses
    list_parser = subparsers.add_parser("list", help="List of all your expenses")
    list_parser.set_defaults(func=expenses_list)

    # Summary
    summary_parser = subparsers.add_parser("summary", help="Show summary of all your expenses")
    summary_parser.add_argument("--month", type=int, choices=range(1, 13), help="Filter by month (1-12)")
    summary_parser.set_defaults(func=summary)

    args = parser.parse_args()
    args.func(args)


def load_data():
    if not filename.exists() or filename.stat().st_size == 0:
        return []
    with open(filename, "r") as f:
        return json.load(f)


def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def add_expense(args):
    if args.amount > 0:
        data = load_data()

        new_id = max((item["id"] for item in data), default=0) + 1

        new_item = {
            "id": new_id,
            "date": datetime.now().strftime("%d-%m-%Y"),
            "description": args.description,
            "amount": args.amount
        }

        data.append(new_item)
        save_data(data)
        print(f"Expense {args.description} added successfully ID: {new_id}")
    else:
        print(f"Amount should be greater than 0")


def expenses_list(args):
    data = load_data()
    print(f'{"ID":<5} {"Date":<15} {"Description":<15} {"Amount":<10}')
    for item in data:
        print(f'{item["id"]:<5} {item["date"]:<15} {item["description"]:<15} ${item["amount"]:<10}')

def delete_expense(args):
    data = load_data()

    id_found = False

    for item in data:
        if item["id"] == args.id:
            id_found = True

    if not id_found:
        print(f"No expense with ID {args.id} found. Please try again.")
        return

    data = [item for item in data if item["id"] != args.id]
    save_data(data)
    print(f"Expense deleted successfully")

def summary(args):
    data = load_data()
    total = 0
    months = [
        "",
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if args.month:
        for item in data:
            item_month = datetime.strptime(item["date"], "%d-%m-%Y").month
            if item_month == args.month:
                total += item["amount"]
        month_name = months[args.month]
        print(f"Total expenses for {month_name}: ${total}")
    else:
        for item in data:
            total += item["amount"]
        print(f"Total expenses: ${total}")



if __name__ == '__main__':
    main()

