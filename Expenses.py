import datetime
import json
import os

current_date = datetime.datetime.now()

class Expenses:
    def __init__(self):
        self.categories = []
        self.dataDir = './data'
        self.filename = 'expenses.json'
        self.filepath = None

    # Insert a new expense
    def insert_expense(self, category, cost, date=current_date):
        expense = {
            'year': date.year,
            'month': date.month,
            'category': category,
            'cost': cost
        }

        json_dump = json.dumps(expense)
        self.addToJson(json_dump)
        
    # Add new expense to json file for future use
    def addToJson(self, json_dump):
        # Set the filepath if it hasn't been set
        if self.filepath == None:
            self.setFilepath()
            print(f"filepath: {self.filepath}")

        # Read json file
        try:
            with open(self.filepath, 'r+') as infile:
                data = json.load(infile)
                print(data)
        except:
            print(f"ERROR: Failed to load {self.filepath}\n")
            exit()


        # Send new expense to json file
        with open(self.filepath, 'a') as outfile:
            outfile.write(json_dump + ',')
        
        print(f"New expense was added to {self.filename}")

    # Set the filepath using dataDir and the json filename
    def setFilepath(self, filename=None):
        if filename == None:
            filename = self.filename
        
        self.filepath = f"{self.dataDir}/{filename}"