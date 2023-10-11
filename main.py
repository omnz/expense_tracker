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


    # Seperate expenses by year
    for y in years:            
        yearly_expenses = []
        for d in data:
            if y == d['year']:
                yearly_expenses.append(d)

        # Create a YYYY_Annual_Expenses.json file
        with open(f'./data/{y}_Annual_Expenses.json', 'w') as outfile:
                outfile.write(json.dumps(yearly_expenses))

    
    # TODO: Calculate total monthly expenses and per category
    
    # TODO: Calculate total yearly expenses and per category
    annual_expenses = 0

    for i in os.listdir(dataDir):
        if 'Annual_Expenses.json' in i:
            with open(f'{dataDir}/{i}') as infile:
                data = json.load(infile)
            
            print(f'\n{i}')
            print(data)

            # Count number of months of data per year
            months = []
            for d in data:
                if d['month'] not in months:
                    months.append(d['month'])

            for m in months:
                monthly_expenses = 0
                for d in data:
                    if m == d['month']:
                        monthly_expenses += d['cost']


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