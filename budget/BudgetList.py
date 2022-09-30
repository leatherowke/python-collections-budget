def __main__():
    from . import Expense

    expenses = Expense.Expenses()
    expenses.read_expenses('data\spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    
    print('the count of all expenses: ' + str(len(myBudgetList)))

    for entry in myBudgetList:
        print(entry)
    

class BudgetList:
    def __init__(self, budget ):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses = item + self.sum_expenses
        else:
            self.overages.append(item)
            self.sum_overages = self.sum_overages + item
    
    def __len__(self):
        return len(self.expenses) + len(self.overages)


    def __iter__(self):
        iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    def __next__(self) :
        try:
            return next(self.iter_o)
        except StopIteration:
            return next(self.iter_o)

myBudgetList = BudgetList(1200)
myBudgetList


 
if __name__ == __main__ :
    __main__()
    

__main__() 