import datetime

current_date = datetime.datetime.now()

class Expenses:
    def __init__(self):
        self.categories = []

    # Insert a new expense
    def insert_expense(self, category, cost, date=current_date):
        print(f'{date.month}/{date.day}/{date.year}')