class Budget():
    def __init__(self, type_of_expense: str):
        self.type_of_expense = type_of_expense
    
    def add_expenses(self):
        num_expenses = int(input(f"Enter how many {self.type_of_expense} expenses you want to add: "))
        num_expenses = int(input(f"Enter how many {self.type_of_expense} expenses you want to add: "))
        self.expenses = []
        for i in range(num_expenses):
            x = int(input('add an expense: '))
            self.expenses.append(x)
        
    def get_expenses(self):
        return sum(self.expenses)
        