# Keep track of monthly expenses and return your average expenses per year.
import os

import Expenses

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


if __name__ == '__main__':
    main()