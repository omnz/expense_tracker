import datetime
import sqlite3

class Expenses:
    '''A class representing an expense'''
    
    def __init__(self):
        '''Initializes an Expenses object'''

        self.dataDir = './data'
        self.filename = 'expenses.json'
        self.filepath = None

    # TODO: Delete a specific expense or all expenses
    def delete_expenses(self, deleteAll=False, yearsToDelete=[], expensesToDelete=[]):
        """
        Handles functionality of deleteing specific expenses, all expenses in a given year, or all expenses in the table

        Parameters:
            deleteAll (boolean): Used to determine whether to delete all expenses in the table
            yearsToDelete: (list): Contains the year(s) which should be deleted from the table
            expensesToDelete: (list): Contains the specific expense(s) which should be deleted from the table
        """

        db = sqlite3.connect(f'{self.dataDir}/Expenses.db')
        cursor = db.cursor()

        # DELETE all expenses from table
        if(deleteAll):
            pass
    
        # DELETE all expenses in the given year(s)
        elif len(yearsToDelete) > 0:
            for year in yearsToDelete:
                pass

        # DELETE expenses in expensesToDelete
        else:
            pass

        # Closing db
        cursor.close()
        db.close()
    
    def create_expense(self, year, month, category, cost):
        '''
            Create a new expense with the passed parameters and insert it into the 'expenses' table

            Parameters:
                year (int): The year the expense took place
                month (int): The month the expense took place
                category (String): Category used to categorize expenses
                cost (float): The cost of the expense
        '''

        db = sqlite3.connect(f'{self.dataDir}/Expenses.db')
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

        # Insert expense into table
        query = """INSERT INTO expenses (year, month, category, cost) VALUES(?, ?, ?, ?);"""
        params = (year, month, category, cost)
        cursor.execute(query, params)
        db.commit()
        print('\nExpense was entered into table')

        # Closing db
        cursor.close()
        db.close()

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
                    if(ask == 'year'):
                        if (user_input <= 0):
                            print('ERROR: The year must be greater than 0')
                            continue
                    elif(ask == 'month'):
                        if (user_input < 1 or user_input > 12):
                            print('ERROR: The month must be a value from 1 to 12')
                            continue
                    
                elif data_type == 'float':
                    error_type = 'number'
                    user_input = float(user_input)
                return user_input
            except:
                print(f"ERROR: Please enter the {ask} as a {error_type}")


    def askForExpenses(self):
        '''Ask user to enter expenses, delete a specific expense, delete all expenses, or continue'''

        # TODO: Ask user whether to delete a specific expense or whether to delete all expenses

        entering_expenses = True
        while(entering_expenses):
            year = ''
            month = ''
            category = ''
            cost = -1

            # Ask user if they want to quit or continue adding expenses
            while(True):
                continue_input = input('\nDo you want to enter an expense? ')
                if continue_input.lower() == 'y' or continue_input.lower() == 'yes':
                    break
                elif continue_input.lower() == 'n' or continue_input.lower() == 'no':
                    entering_expenses = False
                    break

            if entering_expenses == False:
                continue

            # Ask for date of expense
            current_date = input('Is the expense from current year and month? ')
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