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
        NORMAL = '\033[0m'
        RED = '\033[91m'

        while(True):
            user_input = input(f'Enter the {ask}: ')

            try:
                if data_type == 'int':
                    error_type = 'integer number'
                    user_input = int(user_input)
                    if(ask == 'year'):
                        if (user_input <= 0):
                            print(f'{RED}ERROR: The year must be greater than 0{NORMAL}')
                            continue
                    elif(ask == 'month'):
                        if (user_input < 1 or user_input > 12):
                            print(f'{RED}ERROR: The month must be a value from 1 to 12{NORMAL}')
                            continue
                    
                elif data_type == 'float':
                    error_type = 'number'
                    user_input = float(user_input)
                return user_input
            except:
                print(f"{RED}ERROR: Please enter the {ask} as a {error_type}{NORMAL}")
    
    def validYearsToDelete(self):
        db = sqlite3.connect(f'{self.dataDir}/Expenses.db')
        cursor = db.cursor()
        query = """SELECT DISTINCT year FROM expenses;"""
        cursor.execute(query)
        valid_years = cursor.fetchall()

        # Closing db
        cursor.close()
        db.close()

        return valid_years
    
    def possibleYears(self, returnYears=False):
        possible_years = self.validYearsToDelete()
        years = []

        # Change list of tuples to list of int
        for y in possible_years:
            for i in y:
                years.append(i)

        print(f'Possible years to delete: {years}')

        if returnYears:
            return years

    
    def getPossibleExpenses(self, year, month=''):
        db = sqlite3.connect(f'{self.dataDir}/Expenses.db')
        cursor = db.cursor()
        query = ''

        if month != '':
            query = f"""SELECT * FROM expenses WHERE year={year} AND month={month};"""
        else:
            query = f"""SELECT * FROM expenses WHERE year={year};"""

        cursor.execute(query)
        valid_expenses = cursor.fetchall()

        # Closing db
        cursor.close()
        db.close()

        return valid_expenses
    
    def askForExpensesToDelete(self):

        continue_asking = True
        # Ask whether to delete ALL expenses
        while(True):
            delete_all = input('Do you want to delete all expenses? ')
            if (delete_all.lower() == 'y' or delete_all.lower() == 'yes'):
                continue_asking = False
                break
            elif (delete_all.lower() == 'n' or delete_all.lower() == 'no'):
                break

        # Ask whether to delete all expenses for specific years
        if continue_asking:
            yearsToDelete = []
            yearAdded = False

            while(True):
                deleteInYear = ''
                if yearAdded:
                    deleteInYear = input('Do you also want to delete all expenses in another year? ')
                else:
                    deleteInYear = input('Do you want to delete all expenses in a specific year? ')

                if (deleteInYear.lower() == 'y' or deleteInYear.lower() == 'yes'):
                    continue_asking = False

                    # Ask for year to delete
                    while(True):
                        years = self.possibleYears(True)
                        year = self.askUser('year', 'int')
                        if year in years:
                            continue_asking = False
                            yearsToDelete.append(year)
                            yearAdded = True
                            break

                    
                elif (deleteInYear.lower() == 'n' or deleteInYear.lower() == 'no'):
                    break

            # Delete all expenses in specific years
            print(f'yearsToDelete: {yearsToDelete}')
            if len(yearsToDelete) > 0:
                self.delete_expenses(False, yearsToDelete)

        # Ask for specific expenses to delete
        if continue_asking:
            expnsesToDelete = []

            while(True):
                deleteExpense = input('Do you want to delete a specific expense? ')
                if (deleteExpense.lower() == 'y' or deleteExpense.lower() == 'yes'):
                    while(True):
                        id_known = input('Do you know the id of the expense you wish to delete? ')
                        if (id_known.lower() == 'y' or id_known.lower() == 'yes'):
                            expense_id = self.askUser('id', 'int')
                            expnsesToDelete.append(expense_id)
                            break
                        elif (id_known.lower() == 'n' or id_known.lower() == 'no'):
                            print()
                            self.possibleYears()
                            print('Please enter the year of the expense below.')
                            # Ask for year and month
                            year = self.askUser('year', 'int')
                            month = ''

                            while(True):
                                monthKnown = input('Do you know the month of the expense place? ')
                                if (monthKnown.lower() == 'y' or monthKnown.lower() == 'yes'):
                                    month = self.askUser('month', 'int')
                                elif (monthKnown.lower() == 'n' or monthKnown.lower() == 'no'):
                                    break

                            # Get possible expenses to delete and save them in text file
                            output_list = self.getPossibleExpenses(year, month)
                            output = f'====== {year} Expenses ======\n'
                            output += 'id, year, month, category, cost\n\n'

                            # Generate output from output list
                            for expense in output_list:
                                for i in expense:
                                    output += str(i) + ', '
                                output += '\n'
                            filename = f'{self.dataDir}/possibleExpenses.txt'
                            with open(filename, 'w') as outfile:
                                outfile.write(output)

                            print(f'Printing all expenses in given date. Please check {filename} for the id.')
                        
                    
                elif (deleteExpense.lower() == 'n' or deleteExpense.lower() == 'no'):
                    break

    
    def askForExpenses(self):
        '''Ask user to enter expenses, delete a specific expense, delete all expenses, or continue'''

        # TODO: Ask user whether to delete a specific expense or whether to delete all expenses
        BOLD = '\033[1m'
        NORMAL = '\033[0m'
        continue_asking = True
        while(continue_asking):
            year = ''
            month = ''
            category = ''
            cost = -1

            # Ask user if they want to enter expenses, delete expenses, or continue
            while(True):
                task_input = input(f'\nDo you want to {BOLD}add{NORMAL} expenses, {BOLD}delete{NORMAL} expenses, or {BOLD}continue{NORMAL}? ')
                if task_input.lower() == 'add':
                    entering_expenses = True
                    break
                elif task_input.lower() == 'del' or task_input.lower() == 'delete':
                    entering_expenses = False
                    self.askForExpensesToDelete()
                    break
                elif task_input.lower() == 'continue' or task_input.lower() == '':
                    continue_asking = False
                    entering_expenses == False
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