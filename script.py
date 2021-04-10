import codecademylib3
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')
expense_overview = pd.read_csv("expenses.csv")
employees = pd.read_csv("employees.csv")

# code goes here
print(financial_data.head()) 
print(expense_overview.head())
print(employees.head())

month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses


plt.plot(month, revenue)
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.title("Revenue")
plt.show()

plt.clf()
plt.plot(month, expenses)
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.title("Expenses")
plt.show()

expense_categories = expense_overview.Expense
proportions = expense_overview.Proportion

plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.axis('Equal')
plt.tight_layout()
plt.show()

"""mask = expense_overview.isin(proportions[proportions < 0.05].index)
expense_overview[mask] = 'other'
print(expense_overview)"""

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()

expense_cut = 'Salaries'

sorted_data = employees.sort_values(by = ['Productivity'])
#print(sorted_data)

employees_cut = sorted_data.head(100)
print(employees_cut)

commute_times = employees['Commute Time']
print(commute_times.describe())

plt.clf()
plt.hist(commute_times)
plt.show()

commute_times_log = np.log(commute_times)
plt.clf
plt.hist(commute_times_log)
plt.show()

#salaries = employees.Salary
#productivity = employees.Productivity
#print(salaries)
n_produc = employees[['Productivity']].to_numpy()
n_salry = employees[['Salary']].to_numpy()#print(n_employees)

plt.clf
plt.plot(employees.Salary, employees.Productivity)
plt.show()

scaler = StandardScaler()
stand_salry = scaler.fit_transform(n_salry)
stand_produc = scaler.fit_transform(n_produc)

plt.clf()
plt.plot(stand_salry, stand_produc)
plt.show()
