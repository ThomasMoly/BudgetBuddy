from library.project_5 import calc_balance
from library.project_5 import financial_status
from library.Classes_9 import Budget
import os

os.system('cls' if os.name == 'nt' else clear)

Type_cost = []

print("Hey there, this is BudgetBuddy! Your personal Budgeting Assistant.")

name = input("Enter your name: ")

income = input("Hey " +name+ ", This is BudgetBuddy! Your personal Budgeting Assistant. Can you enter your income?: ")


proceed = True

while proceed:
    
    type_of_expense = input("Enter what type of expense you will be adding: ")

    budget = Budget(type_of_expense)

    budget.add_expenses()

    Type_cost.append(budget.get_expenses())
    
    x = input("would you like to continue?").lower()
    if(x == "no"):
        proceed = False
    

balance = calc_balance(income, sum(Type_cost))

financial_status(balance)


