# Startup Transformation — Cost Reduction Analysis

A struggling startup needs to cut costs. Using financial, expense and employee data, this analysis visualises revenue vs expense trends, shows that **salaries are the largest expense category**, identifies the 100 least productive employees, explores commute times (with a log transform for skewed data) and standardises salary vs productivity for comparison.

**Techniques:** matplotlib line/pie/histogram/scatter plots · log transformation · `StandardScaler`

```bash
python analysis.py   # expects data/financial_data.csv, data/expenses.csv, data/employees.csv
```
