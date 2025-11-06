class Budget():
    def __init__(self):
        self.category = []
        self.expenses = []
    def add_expenses(self):
        while True:
            user_input = input("Enter expense as 'Type Cost' (e.g., Milk 10): ")

            try:
                type_cost_of_expense = user_input.split()

                expense_type = type_cost_of_expense[0]
                expense_cost = int(type_cost_of_expense[1])

                self.category.append(expense_type)
                self.expenses.append(expense_cost)

                break

            except ValueError:
                print("\n Error: Please enter in the correct format: Type Cost (e.g., Rent 1200)\n")
            except:
                print("\n Unexpected error. Try again.\n")
                
    def get_expenses(self):
        return sum(self.expenses)

    def get_expense_details(self):
        print("Expense Details")
        for i in range(len(self.category)):
            print(f"{self.category[i]}: ${self.expenses[i]}")
