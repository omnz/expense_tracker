import datetime
import json
import os

class Expenses:
    '''A class representing an expense'''
    
    def __init__(self):
        '''Initializes an Expenses object'''

        self.dataDir = './data'
        self.filename = 'expenses.json'
        self.filepath = None

    def create_expense(self, year, month, category, cost):
        '''
            Create a new expense with the passed parameters

            Parameters:
                year (int): The year the expense took place
                month (int): The month the expense took place
                category (String): Category used to categorize expenses
                cost (float): The cost of the expense
        '''

        expense = {
            'year': year,
            'month': month,
            'category': category,
            'cost': cost
        }

        print('\nExpense was created')
        self.addToJson(expense)
        
    def addToJson(self, expense):
        '''
            Add new expense to json file for future use

            Parameters:
                expense (dict): A dictionary containing the data of a newly created expense
        '''

        # Set the filepath if it hasn't been set
        if self.filepath == None:
            self.setFilepath()

        print(f'Saving expense in {self.filepath}')

        # Check if json file exists and is empty or doesn't exist
        if os.path.exists(self.filepath) and os.path.getsize(self.filepath) <= 0:
            with open(self.filepath, 'w') as outfile:
                outfile.write('[]')     # Create or initialize file with []
        elif os.path.exists(self.filepath) == False:
            with open(self.filepath, 'w') as outfile:
                outfile.write('[]')     # Create or initialize file with []
        
        print(f"Initalized {self.filepath}")

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

    def setFilepath(self, filename=None):
        '''
            Set the filepath using dataDir and the json filename

            Parameters:
                filename (None or String): The name of the currently used json file
        '''

        if filename == None:
            filename = self.filename
        
        self.filepath = f"{self.dataDir}/{filename}"

    def askUser(self, ask, data_type):
        '''
            Ask user for input

            Parameters:
                ask (String): String containing key of what will be asked
                data_type (String): The data type of the input. Used for data type validation.
            Return:
                user_input (int, float, or String): A validated user input
        '''
        error_type = ''

        while(True):
            user_input = input(f'Enter the {ask} of expense: ')

            try:
                if data_type == 'int':
                    error_type = 'integer number'
                    user_input = int(user_input)
                elif data_type == 'float':
                    error_type = 'number'
                    user_input = float(user_input)
                return user_input
            except:
                print(f"ERROR: Please enter the {ask} as a {error_type}")


    def askForExpenses(self):
        '''Ask user for expenses or quit'''

        while(True):
            year = ''
            month = ''
            category = ''
            cost = -1

            # Ask for date of expense
            current_date = input('\nIs the expense from current year and month? ')
            if (current_date.lower() == 'n' or current_date.lower() == 'no'):
                # Ask for year and month
                year = self.askUser('year', 'int')
                month = self.askUser('month', 'int')
            elif (current_date.lower() == 'y' or current_date.lower() == 'yes'):
                pass
            else:
                continue

            # Ask user for expense category and cost
            category = self.askUser('category', 'String')
            cost = round(self.askUser('cost', 'float'), 2)
        
            # Use entered data to create expenses
            if(year != ''):
                self.create_expense(year, month, category, cost)
            else:
                current_date = datetime.datetime.now()
                self.create_expense(current_date.year, current_date.month, category, cost)

            # Ask user if they want to quit or continue adding expenses
            while(True):
                continue_input = input('Do you want to enter another expense? ')
                if continue_input.lower() == 'y' or continue_input.lower() == 'yes':
                    break
                elif continue_input.lower() == 'n' or continue_input.lower() == 'no':
                    exit()