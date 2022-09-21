

  #  def __next__(self) :
   #     try:
    #        return __next__(self_e)
from pickle import APPEND
from typing_extensions import Self


def __main__():
    from . import Expense

    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.value)
    

class BudgetList:
    def __init__(self, budget ):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = {}
        self.sum_overages = 0
        self.overages = {}

    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            return item + self.sum_expenses
        else:
            self.overages.append(item)
            return self.overages + item
    
    def __len__(self):
        return len(self.expenses) + len(self.overages)


   # def __iter__(self):
    #    iter(self.expenses)
     #   self.iter_o = iter(self.overages)
      #  return self

    

myBudgetList = BudgetList(1200)
myBudgetList
print('the count of all expenses: ' + str(len(myBudgetList)))

 
if __name__ == __main__ :
    __main__()
    print('the count of all expenses: ' + str(len(myBudgetList)))


