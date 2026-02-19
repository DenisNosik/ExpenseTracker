A simple CLI Expense Tracker for tracking your expenses.
Allows you to add, delete, list expenses, and get monthly summaries.

## Installation

Clone the repository:

```
git clone https://github.com/denisnosik/ExpenseTracker.git
cd ExpenseTracker
python3 main.py -h
```

## Usage

All commands are run via Python

1️⃣ Add an expense:
```
python main.py add --description "Lunch" --amount 99
```
--description — description of the expense
--amount — amount spent (number)
The date is automatically set to today.

2️⃣ List all expenses:
```
python main.py list
```
Displays a table with ID, Date, Description, and Amount

3️⃣ Delete an expense:
```
python main.py delete --id 2
```
--id — ID of the expense to delete
After deletion, a confirmation is printed: Expense 'Dinner' deleted successfully

4️⃣ Summary of expenses:
Total expenses:
```
python main.py summary
```
Total for a specific month:
```
python main.py summary --month 8
```
--month — number of the month (1-12)
Output example: Total expenses for August: $35

📝 Notes
All expenses are stored in expenses_data.json.
IDs are automatically incremented for new expenses.
Monthly summaries support filtering by month.
Tables are neatly aligned for easy terminal reading.
