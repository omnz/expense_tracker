# Keep track of monthly expenses and return your average expenses per year.
import os
import json
import Expenses

def calulateExpenses():
    dataDir = './data'
    filename = 'expenses.json'
    filepath = f'{dataDir}/{filename}'
    data = ''
    years = []
    dataByYear = []

    with open(filepath, 'r+') as infile:
        data = json.load(infile)

    print(data)
    # Count number of years of data
    for d in data:
        if d['year'] not in years:
            years.append(d['year'])

    print(f'years: {years}')


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