import os


os.system('cls' if os.name == 'nt' else 'clear')

name = input("What's your name? ")
print(f"Hey {name}, this is BudgetBuddy! Let's check your finances.")

income = float(input("Please enter your monthly income: "))

num_expenses = int(input("How many number of expenses you want to enter?:"))

expenses = []
for i in range(num_expenses):
    e = float(input(f"Enter expense {i+1} (numbers only):"))
    expenses.append(e)

raw_expense_total = sum(expenses)
print(f"\nYou entered {num_expenses} expenses totaling ${raw_expense_total:.2f}")




print(f"\nYou entered {num_expenses} expenses totaling")
