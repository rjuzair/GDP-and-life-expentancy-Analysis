"""Startup transformation - where can a struggling startup cut costs?

Visualises revenue and expense trends, breaks down expense categories,
identifies the least productive employees, and explores commute times and
the salary-productivity relationship.

Data: data/financial_data.csv, data/expenses.csv, data/employees.csv
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

DATA_DIR = Path(__file__).parent / "data"
SMALL_CATEGORY = 0.05


def main():
    financial_data = pd.read_csv(DATA_DIR / "financial_data.csv")
    expense_overview = pd.read_csv(DATA_DIR / "expenses.csv")
    employees = pd.read_csv(DATA_DIR / "employees.csv")

    # Revenue vs expenses over time
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.plot(financial_data.Month, financial_data.Revenue)
    ax1.set_title("Revenue")
    ax2.plot(financial_data.Month, financial_data.Expenses, color="tab:red")
    ax2.set_title("Expenses")
    for ax in (ax1, ax2):
        ax.set_xlabel("Month")
        ax.set_ylabel("Amount ($)")
    plt.tight_layout()
    plt.show()

    # Expense breakdown, grouping small categories into "Other"
    expenses = expense_overview.copy()
    expenses.loc[expenses.Proportion < SMALL_CATEGORY, "Expense"] = "Other"
    expenses = expenses.groupby("Expense", as_index=False).Proportion.sum()
    plt.pie(expenses.Proportion, labels=expenses.Expense, autopct="%0.0f%%")
    plt.axis("equal")
    plt.title("Expense categories")
    plt.show()

    largest = expenses.sort_values("Proportion", ascending=False).Expense.iloc[0]
    print(f"Largest expense category: {largest}")

    # Least productive 100 employees - candidates for restructuring
    employees_cut = employees.sort_values("Productivity").head(100)
    print(employees_cut.head())

    # Commute times are right-skewed; a log transform makes them easier to read
    commute_times = employees["Commute Time"]
    print(commute_times.describe())
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.hist(commute_times)
    ax1.set_title("Commute time (minutes)")
    ax2.hist(np.log(commute_times))
    ax2.set_title("Log commute time")
    plt.show()

    # Standardise salary and productivity to compare on a common scale
    scaled = StandardScaler().fit_transform(employees[["Salary", "Productivity"]])
    plt.scatter(scaled[:, 0], scaled[:, 1], alpha=0.5)
    plt.xlabel("Salary (standardised)")
    plt.ylabel("Productivity (standardised)")
    plt.title("Salary vs productivity")
    plt.show()


if __name__ == "__main__":
    main()
