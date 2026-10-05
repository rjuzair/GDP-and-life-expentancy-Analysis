# Data Analysis & Visualization in Python

Exploratory data analysis, data cleaning and interactive dashboards built with **pandas, matplotlib, seaborn and Plotly Dash**.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly%20Dash-3F4F75?logo=plotly&logoColor=white)

## Featured
| Project | Description |
|---|---|
| [**GDP vs Life Expectancy**](exploratory-analysis/gdp-vs-life-expectancy) | How economic growth relates to life expectancy across six countries (2000–2015) — growth rates, correlation and distribution analysis. |
| [**US Airline Performance Dashboard**](dashboards/us-airline-performance-dashboard) | Interactive Plotly Dash app reporting cancellations, diversions, flight volumes and delay causes by airline and year. |
| [**Roller Coaster Rankings**](exploratory-analysis/roller-coaster-rankings) | Reusable visualisation functions exploring Golden Ticket Award rankings and 2,800+ coasters' statistics. |

## Exploratory analysis
| Project | Description |
|---|---|
| [Startup cost reduction](exploratory-analysis/startup-cost-reduction) | Revenue/expense trends, expense breakdown and employee productivity to guide cost cuts |
| [London weather variance](exploratory-analysis/london-weather-variance) | Annual and monthly temperature variance and standard deviation |
| [Automobile evaluation](exploratory-analysis/automobile-evaluation-summary) | Frequencies, proportions and ordinal medians for categorical car data |

## Data wrangling
| Project | Description |
|---|---|
| [US census data cleaning](data-wrangling/us-census-data-cleaning) | Combine multi-file census data; parse currency, split columns, impute and de-duplicate |
| [E-commerce funnel analysis](data-wrangling/ecommerce-funnel-analysis) | Join event logs to measure drop-off at each step of the purchase funnel |
| [Garden inventory analysis](data-wrangling/garden-inventory-analysis) | Filtering and feature creation on a retail inventory |
| [Medical insurance records](data-wrangling/medical-insurance-records) | Core Python data structures for patient records |

## Getting started
```bash
pip install -r requirements.txt
jupyter notebook exploratory-analysis/gdp-vs-life-expectancy/life_expectancy_gdp.ipynb
python dashboards/us-airline-performance-dashboard/app.py
```
The notebooks ship with their data. The script-based projects read from a local `data/` folder; those datasets come from the [Codecademy](https://www.codecademy.com/) Data Science path and are not redistributed here.
