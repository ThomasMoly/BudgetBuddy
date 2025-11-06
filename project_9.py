from library.project_5 import calc_balance
from library.project_5 import financial_status
from library.Classes_9 import Budget
import os

os.system('cls' if os.name == 'nt' else clear)

total_expense = []

print("Hey there, this is BudgetBuddy! Your personal Budgeting Assistant.")

name = input("Enter your name: ")

income = input("Hey " +name+ ", This is BudgetBuddy! Your personal Budgeting Assistant. Can you enter your income?: ")

#general process for any expense:
proceed = True

while proceed:

    budget = Budget()

    budget.add_expenses()

    total_expense.append(budget.get_expenses())

    budget.get_expense_details()
    
    x = input("would you like to continue?").lower()
    if(x == "no"):
        proceed = False
    

balance = calc_balance(income, sum(total_expense))

financial_status(balance)


