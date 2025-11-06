from library.project_5 import calc_balance
from library.project_5 import financial_status
import os


os.system('cls' if os.name == 'nt' else clear)

print("Hey there, this is BudgetBuddy! Your personal Budgeting Assistant.")

name = input("Enter your name: ")

income = input("Hey " +name+ ", This is BudgetBuddy! Your personal Budgeting Assistant. Can you enter your income?: ")

expenses = []

num_expenses = int(input('How many expenses will you add?: '))

for i in range(num_expenses):
    expense = int(input('Add an expense: '))
    expenses.append(expense)

total_expenses = sum(expenses)

balance = calc_balance(income, total_expenses)
financial_status(balance)


