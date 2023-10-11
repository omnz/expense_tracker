# Keep track of monthly expenses and return your average expenses per year.
import os
import Expenses
import sqlite3

def calulateExpenses():
    dataDir = './data'

    db = sqlite3.connect(f'{dataDir}/Expenses.db')
    cursor = db.cursor()

    # Create expenses table if it doesn't exist
    query = """CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY NOT NULL,
        year INTEGER NOT NULL,
        month INTEGER NOT NULL,
        category VARCHAR(32) NOT NULL,
        cost REAL NOT NULL
    );"""
    cursor.execute(query)

    # TODO: Remove this later. Testing query output to console
    query = """SELECT * FROM expenses;"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    # Closing db
    cursor.close()
    db.close()
    
    # TODO: Calculate total monthly expenses and per category
    
    # TODO: Calculate total yearly expenses and per category

    # TODO: Calculate average monthly and yearly expenses

def main():
    # Create 'data' directory if it does not exist
    dataDir = './data'
    if os.path.exists(dataDir) == False:
        try:
            os.makedirs(dataDir)
            print(f"Created missing {dataDir} directory")
        except:
            print(f"ERROR: Failed to create the {dataDir} directory!")

    # Add expenses
    new_expense = Expenses.Expenses()
    new_expense.askForExpenses()

    # Print expenses
    calulateExpenses()

if __name__ == '__main__':
    main()