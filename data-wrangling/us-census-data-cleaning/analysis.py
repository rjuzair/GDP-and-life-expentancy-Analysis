"""US Census data cleaning.

Combines state-level census extracts spread across many CSV files, cleans
messy string columns (currency, combined gender counts, percentages),
imputes missing values, removes duplicates and visualises the result.

Data: data/states*.csv
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
RACE_COLUMNS = ["Hispanic", "White", "Black", "Native", "Asian", "Pacific"]


def load_census():
    files = sorted(DATA_DIR.glob("states*.csv"))
    return pd.concat((pd.read_csv(f) for f in files), ignore_index=True)


def clean_census(us_census):
    # "$43,296.36" -> 43296.36
    us_census["Income"] = pd.to_numeric(
        us_census.Income.replace(r"[\$,]", "", regex=True))

    # "2341093M_2489527F" -> Men = 2341093, Women = 2489527
    split = us_census.GenderPop.str.split("_")
    us_census["Men"] = pd.to_numeric(split.str.get(0).str.replace("M", "", regex=False))
    us_census["Women"] = pd.to_numeric(split.str.get(1).str.replace("F", "", regex=False))

    # Missing women counts can be recovered from the total population
    us_census["Women"] = us_census.Women.fillna(us_census.TotalPop - us_census.Men)

    duplicates = us_census.duplicated(subset=["State"]).sum()
    print(f"Duplicate state rows removed: {duplicates}")
    us_census = us_census.drop_duplicates(subset=["State"])

    # "17.5%" -> 17.5, then impute gaps with the column mean
    for column in RACE_COLUMNS:
        us_census[column] = pd.to_numeric(us_census[column].str.rstrip("%"))
        us_census[column] = us_census[column].fillna(us_census[column].mean())

    return us_census


def plot(us_census):
    plt.scatter(us_census.Women, us_census.Income)
    plt.xlabel("Women")
    plt.ylabel("Average income ($)")
    plt.title("Female population vs average income by state")
    plt.show()

    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    for ax, column in zip(axes.flat, RACE_COLUMNS):
        ax.hist(us_census[column], bins=15)
        ax.set_title(f"{column} (% of population)")
    fig.suptitle("Distribution of race/ethnicity share across states")
    fig.tight_layout()
    plt.show()


def main():
    us_census = clean_census(load_census())
    print(us_census.head())
    plot(us_census)


if __name__ == "__main__":
    main()
