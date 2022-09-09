import Expense 
import collections

expenses = Expense.Expenses()
expenses.read_expenses('data\spending_data.csv')
spending_catagories = []

for expense in expenses.list:
    spending_catagories.append(expense.category)

spending_counter = collections.Counter(spending_catagories)
print(spending_counter)


