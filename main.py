# Keep track of monthly expenses and return your average expenses per year.
import os
import Expenses
import sqlite3
import locale

def calulateExpenses():
    """Calculate monthly expenses per category, total monthly expenses, and annual expenses. Then print results to console."""

    locale.setlocale(locale.LC_ALL, 'en_US')    # Set to currency to USD
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

    # SELECT DISTINCT years in which expenses occured
    query = """SELECT DISTINCT year FROM expenses;"""
    cursor.execute(query)
    query_result = cursor.fetchall()
    years = []
    for y in query_result:
        for year in y:
            years.append(year)
    
    # SELECT DISTINCT months per year where expenses occured
    for year in years:
        query = f"""SELECT DISTINCT month FROM expenses WHERE year={year}"""
        cursor.execute(query)
        query_result = cursor.fetchall()
        annual_cost = 0

        months = []
        for i in query_result:
            for month in i:
                months.append(month)
        
        print(f'\n=============== {year} Costs ===============')
        # SELECT DISTINCT categories per month
        for month in months:
            query = f"""SELECT DISTINCT category FROM expenses WHERE year={year} AND month={month}"""
            cursor.execute(query)
            query_result = cursor.fetchall()

            categories = []
            for i in query_result:
                for category in i:
                    categories.append(category)

            print(f'\n*** {getMonth(month)}\'s Cost Breakdown: ***')
            # SELECT all costs per category
            monthly_cost = 0
            for category in categories:
                query = f"""SELECT cost FROM expenses WHERE year={year} AND month={month} AND category='{category}'"""
                cursor.execute(query)
                query_result = cursor.fetchall()

                costs = []
                for i in query_result:
                    for cost in i:
                        costs.append(cost)

                # Calculate costs per category
                category_cost = 0
                for cost in costs:
                    category_cost += cost

                monthly_cost += category_cost 

                print(f'{category.title()}: {locale.currency(category_cost, grouping=True)}')

            print(f'\n* Total Monthly Costs: ${monthly_cost} *\n')
            annual_cost += monthly_cost

        # Print annual costs
        print('\n-----------------------------------')
        print(f'Total Annual Costs: {locale.currency(annual_cost, grouping=True)}')
        print('-----------------------------------')

    # Closing db
    cursor.close()
    db.close()

def getMonth(month):
    """Given month number return month name
        Parameters:
            month (int): numerical representation of month

        Return: Name of month corresponding to the passed numerical value
    """

    match month:
        case 1:
            return 'January'
        case 2:
            return 'February'
        case 3:
            return 'March'
        case 4:
            return 'April'
        case 5:
            return 'May'
        case 6:
            return 'June'
        case 7:
            return 'July'
        case 8:
            return 'August'
        case 9:
            return 'September'
        case 10:
            return 'October'
        case 11:
            return 'November'
        case 12:
            return 'December'

    

def main():
    """
    Returns the user's annual and monthly costs as well as the distribution of all of their expenses

    Steps to Complete:
    1) Create a 'data' directory if it doesn't exist to store the 'Expenses.db'
    2) Create the 'Expenses.db' if it doesn't exist
    3) Ask the user to enter expenses, if they wish to
    4) Calculate and print out the user's annual and monthly expenses as well as what they spent their money on each month
    """
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