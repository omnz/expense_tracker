import datetime
import json
import os

class Expenses:
    def __init__(self):
        self.categories = []
        self.dataDir = './data'
        self.filename = 'expenses.json'
        self.filepath = None

    # Insert a new expense
    def insert_expense(self, year, month, category, cost):
        expense = {
            'year': year,
            'month': month,
            'category': category,
            'cost': cost
        }

        self.addToJson(expense)
        
    # Add new expense to json file for future use
    def addToJson(self, expense):
        # Set the filepath if it hasn't been set
        if self.filepath == None:
            self.setFilepath()
            print(f"filepath: {self.filepath}")

        # Check if json file does not exists or is empty
        if os.path.exists(self.filepath) == False or os.path.getsize(self.filepath) <= 0:
            with open(self.filepath, 'w') as outfile:
                outfile.write('[]')

        # Read json file
        data = ''
        try:
            with open(self.filepath, 'r+') as infile:
                data = json.load(infile)
        except:
            print(f"ERROR: Failed to load {self.filepath}\n")
            exit()

        # Send new expense to json file
        data.append(expense)
        with open(self.filepath, 'w') as outfile:
            outfile.write(json.dumps(data).replace('\\', ''))
        
        print(f"New expense was added to {self.filename}")

    # Set the filepath using dataDir and the json filename
    def setFilepath(self, filename=None):
        if filename == None:
            filename = self.filename
        
        self.filepath = f"{self.dataDir}/{filename}"

    # Ask user for expenses or quit
    def askForExpenses(self):
        user_input = ''

        while(True):
            year = ''
            month = ''
            category = ''
            cost = -1

            # Ask for date of expense
            current_date = input('Is expense from current year and month? ')
            if (current_date.lower() == 'n' or current_date.lower() == 'no'):
                # Ask for year
                while(True):
                    year = input('Enter the year of expense: ')
                    try:
                        year = int(year)
                        break
                    except:
                        print("ERROR: Please enter the year as a integer number")

                # Ask for month
                while(True):
                    month = input('Enter the month of expense: ')
                    try:
                        month = int(month)
                        break
                    except:
                        print("ERROR: Please enter the month as a integer number")
            elif (current_date.lower() == 'y' or current_date.lower() == 'yes'):
                pass
            else:
                continue

            # TODO: Ask user for expense category
            break
            # TODO: Ask user for expense cost
            break
        
            # Use entered data to create expenses
            if(year != ''):
                self.insert_expense(year, month, category, cost)
            else:
                current_date = datetime.datetime.now()
                self.insert_expense(current_date.year, current_date.month, category, cost)

            # TODO: Ask user if they want to quit or continue adding expenses
            break